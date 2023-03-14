<template>
  <tr class="" v-for="coin in coins" :key="coin.id">
    <td>
      <div class="d-flex align-items-center logo-item p-0">
        <img :src="coin.image" alt="" style="width: 30px; height: 30px"
             class="rounded-circle"/>
        <div class="ms-2">
          <p class="fw-bold p-0 mb-0">{{ coin.name }}</p>
          <p class="text-muted p-0 mb-0">{{ coin.symbol.toUpperCase() }}</p>
        </div>
      </div>
    </td>
    <td>
      <p class="fw-normal p-0 mb-0">RUB {{ coin.current_price }}</p>
    </td>
    <td class="amount">
      {{ coin.amount }}
    </td>
    <td>
      <span class="total p-0">
        RUB {{ (coin.current_price * coin.amount).toFixed(2) }}
      </span>
    </td>
    <td class="">
      <div class="d-flex justify-content-center">
        <buy-button @click="buyEvent(coin.id)"/>
      </div>
    </td>
    <td>
      <div class="d-flex justify-content-center">
        <sell-button @click="sellEvent(coin.id, coin.amount)"/>
      </div>
    </td>
  </tr>
</template>

<script>

export default {
  props: {
    coins: {
      type: Array,
      required: true,
    }
  },
  emits: ['buyEvent', 'sellEvent'],
  data() {
    return {
      coin: {
        id: Number,
        name: String,
        symbol: String,
        image: String,
        current_price: Number,
        amount: Number,
      }
    }
  },
  methods: {
    buyEvent(id) {
      let amount;
      while (true) {
        amount = prompt("Сколько хотите купить?")
        if (!amount) {
          break
        } else if (isNaN(amount)) {
          alert("Количество должно быть числом")
        } else if (amount <= 0) {
          alert("Количество должно быть положительным")
        } else {
          this.$emit('buyEvent', id, parseFloat(amount))
          break
        }
      }
    },
    sellEvent(id, currentAmount) {
      let amount;
      while (true) {
        amount = prompt("Сколько хотите продать?")
        if (!amount) {
          break
        } else if (isNaN(amount)) {
          alert("Количество должно быть числом")
        } else if (amount <= 0) {
          alert("Количество должно быть положительным")
        } else if (amount > currentAmount) {
          alert("У вас нет столько")
        } else if (amount == currentAmount) {
          if (confirm("Хотите продать все?")) {
            this.$emit('sellEvent', id, parseFloat(amount))
            break;
          }
        } else {
          this.$emit('sellEvent', id, parseFloat(amount))
          break;
        }
      }
    }
  },

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Tahoma', sans-serif
}

.logo-item {
  padding-left: 15px;
}

.table thead th {
  padding: 30px;
  font-weight: normal;
}

::placeholder {
  color: black;
  font-weight: 600;
}

.table tbody td {
  padding: 30px;
  margin: 0;
}

body, thead, tbody {
  background-color: var(--bg-color);
  color: var(--text-color);
  border-color: var(--card-color) !important;
}

tbody {
  border-top: var(--card-color);
}

tr {
  border-color: var(--card-color);
}


</style>