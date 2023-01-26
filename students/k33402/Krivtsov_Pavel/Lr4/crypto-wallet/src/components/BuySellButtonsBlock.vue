<template>
  <div class="d-grid gap-2">
    <button type="button" id="buy" class="btn btn-outline-success btn-lg" @click="buyButtonPressed">Купить</button>
  </div>

  <div class="d-grid gap-2">
    <button type="button" id="sell" class="btn btn-outline-danger btn-lg" @click="sellButtonPressed">Продать</button>
  </div>
</template>

<script>
import $ from "jquery"

const TransactionType = {S: 's', B: 'b'}
const currencyCountForTransaction = 1

export default {
  name: "BuySellButtonsBlock",
  data() {
    return {
      ownership: ""
    }
  },
  props: {
    currency: null
  },
  created() {
    if (Object.keys(this.currency).length !== 0) {
      this.getOwnership()
    } else {
      const unwatch = this.$watch('currency', () => {
        this.getOwnership()
        unwatch()
      })
    }
  },
  methods: {
    getOwnership() {
      $.ajax({
        url: `http://127.0.0.1:8000/ownerships/currency/${this.currency.id}`,
        type: "GET",
        success: (response) => {
          this.ownership = response
        }
      })
    },

    createOwnership(count) {
      $.ajax({
        url: "http://127.0.0.1:8000/ownerships/create/",
        type: "POST",
        data: {
          currency: this.currency.id,
          count: count,
        },
        success: (response) => {
          this.ownership = response
          alert(`Покупка ${count} ${this.currency.abbreviation}`)
        },
        error: (response) => {
          alert(Object.values(response.responseJSON)[0])
        }
      })
    },

    changeOwnership(count, type) {
      let operation = ""
      switch (type) {
        case TransactionType.S:
          operation = "Продажа";
          break;
        default:
          operation = "Покупка"
      }

      $.ajax({
        url: `http://127.0.0.1:8000/ownerships/change_count/${this.ownership.id}/`,
        type: "PATCH",
        data: {
          count: count
        },
        success: () => {
          this.getOwnership()
          alert(`${operation} ${currencyCountForTransaction} ${this.currency.abbreviation}`)
        },
        error: (response) => {
          alert(Object.values(response.responseJSON)[0])
        }
      })
    },

    createTransaction(type, count) {
      $.ajax({
        url: "http://127.0.0.1:8000/transactions/create/",
        type: "POST",
        data: {
          currency: this.currency.id,
          transaction_type: type.toString(),
          count: count,
          transaction_amount: count
        },
        error: (response) => {
          console.log(response)
          alert(Object.values(response.responseJSON)[0])
        }
      })
    },

    buyButtonPressed() {
      if (this.ownership) {
        this.changeOwnership(this.ownership.count + currencyCountForTransaction)
      } else {
        this.createOwnership(currencyCountForTransaction)
      }
      this.createTransaction(TransactionType.B, currencyCountForTransaction)
    },

    sellButtonPressed() {
      if (this.ownership) {
        const remainder = this.ownership.count - currencyCountForTransaction
        if (remainder >= 0) {
          this.createTransaction(TransactionType.S, currencyCountForTransaction)
          this.changeOwnership(remainder, TransactionType.S)
        } else {
          alert("Вы пытаетесь продать валюты больше, чем у вас есть")
        }
      } else {
        alert("Чтобы продать валюту, ее нужно сначала приобрести")
      }
    }
  }
}
</script>
