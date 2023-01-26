<template>
  <tr class="coin-wrapper" v-for="coin in coins" style="height: 60px">
    <td class="ps-4">
      <div class="d-flex align-items-center logo-item p-0">
        <img :src="coin.image"
             alt="" style="width: 30px; height: 30px"
             class="rounded-circle"/>
        <div class="ms-2">
          <p class="fw-bold mb-0">{{ coin.name }}</p>
          <p class="text-muted mb-0">{{ coin.symbol.toUpperCase() }}</p>
        </div>
      </div>
    </td>
    <td>
      <p class="fw-normal mb-0 p-0">RUB {{ coin.current_price }}</p>
    </td>
    <td>
      <p class="fw-normal mb-0 p-0" :class="[coin.price_change_percentage_24h >=0 ? 'text-success' : 'text-danger']">
        {{ coin.price_change_percentage_24h.toFixed(2) }} %</p>
    </td>
    <td>
      <span class="start-date p-0">{{ formatDate(coin.atl_date) }}</span>
    </td>
    <td>
      <div class="d-flex justify-content-center align-content-center">
        <buy-button @click="buyEvent(coin.id)"/>
      </div>
    </td>
  </tr>
</template>

<script>
import moment from 'moment'
import router from "@/router";

export default {
  props: {
    coins: {
      type: Array,
      required: true,
    }
  },
  emits: ['buyEvent'],
  data() {
    return {
      coin: {
        id: Number,
        name: String,
        symbol: String,
        price_change_percentage_24h: Number,
        image: String,
        current_price: Number,
        atl_date: String,
      },
      isPositive: 'text-danger',
    }
  },
  methods: {
    formatDate(value) {
      return moment(value).format('DD-MM-YYYY')
    },
    buyEvent(id) {
      if (!localStorage.getItem('pinia_users')) {
        router.push('/login');
      } else {
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
      }
    }
  }
}
</script>

<style>


</style>