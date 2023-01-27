import { defineStore } from 'pinia'
import { ordersAPI, cartItemsAPI } from '@/api'

const useOrdersStore = defineStore('orders', {
  state: () => ({
    orders: [],
    cartItems: [],
  }),

  actions: {
    async fetchOrders(token) {
      const response = await ordersAPI.fetchOrders(token)

      this.orders = response.data.orders
      return response
    },
    async fetchCartItems(token) {
      const response = await cartItemsAPI.fetchCartItems(token)

      this.cartItems = response.data.cart_items
      return response
    },
    async createOrder(token) {
      const response = await ordersAPI.createOrder(token)
      return response
    },
    async createCartItem(product, quantity, token) {
      const response = await cartItemsAPI.createCartItem({ product, quantity }, token)
      return response
    },
    async removeCartItem(id, token) {
      const response = await cartItemsAPI.removeCartItem(id, token)
      return response
    },
  }
})

export default useOrdersStore
