<template>
<div class="modal fade" id="cart" tabindex="-1" aria-labelledby="cartModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="cartModalLabel">Корзина</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <h5
          v-if="isCartEmpty"
          class="text-uppercase text-center text-muted"
        >
          Корзина пуста
        </h5>
        <div
          v-for="item in cartItems"
          :key="item.id"
          class="row justify-content-between align-items-stretch mb-3">
          <div class="col-auto">
            <img
              :src="item.product.photo"
              :alt="item.product.name"
              width="140"
              height="140"
            >
          </div>
          <div class="col">
            <h5>{{ item.product.name }}</h5>
            <h6>{{ COLORS[item.product.color] }}</h6>
            <div class="btn-group btn-group" role="group" aria-label="amount">
              <!-- <button type="button" class="btn btn-outline-dark">-</button> -->
              <button type="button" class="btn btn-outline-dark" disabled>{{ item.quantity }}</button>
              <!-- <button type="button" class="btn btn-outline-dark">+</button> -->
            </div>
          </div>
          <div class="col-auto">
            <div class="d-flex justify-content-between align-items-end flex-column" style="height:100%">
              <button
                type="button"
                class="btn-close"
                aria-label="Close"
                @click="removeItem(item.id)"
              ></button>
              <small>{{ item.product.price }}</small>
            </div>
          </div>
          <hr>
        </div>
      </div>
      <div class="modal-footer">
        <div class="row justify-content-between" style="width: 100%">
          <div class="col-auto">
            <strong>ПРОМЕЖУТОЧНЫЙ ИТОГ</strong>
          </div>
          <div class="col-auto">
            <strong>{{ totalPriceFormatted }},00 RUB</strong>
          </div>
        </div>
        <div class="d-grid w-100">
          <button
            type="button"
            class="btn btn-dark btn-lg"
            data-bs-dismiss="modal"
            :disabled="isCartEmpty"
            @click="makeOrder"
          >ЗАКАЗАТЬ</button>
        </div>
        <div class="row text-sm">
          <small class="col">
            Комиссия, доставка и скидки рассчитываются на шаге “Оформление заказа”.
          </small>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapState, mapActions } from 'pinia';
import useOrdersStore from '@/stores/orders'
import useUsersStore from '@/stores/users'
import { COLORS } from '@/const/lang'

export default {
  name: 'CartModal',
  data() {
    return {
      COLORS
    }
  },
  computed: {
    ...mapState(useOrdersStore, ['cartItems']),
    ...mapState(useUsersStore, ['token']),
    totalPrice() {
      return this.cartItems.length
        ? this.cartItems.reduce((acc, item) => acc + +(/([\d.]+),/.exec(item.product.price)[1].replace('.','')), 0)
        : 0
    },
    totalPriceFormatted() {
      const totalPriceString = String(this.totalPrice)
      return totalPriceString.length > 3
        ? totalPriceString.slice(0,totalPriceString.length - 3) + '.' + totalPriceString.slice(-3)
        : totalPriceString
    },
    isCartEmpty() {
      return !this.cartItems.length
    }
  },
  methods: {
    ...mapActions(useOrdersStore, ['removeCartItem', 'fetchCartItems', 'createOrder']),
    removeItem(id) {
      this.removeCartItem(id, this.token).then(() => {
        this.fetchCartItems(this.token)
      })
    },
    makeOrder() {
      this.createOrder(this.token).then(() => {
        this.$router.push('/profile')
      })
    }
  }
}
</script>