import { defineStore } from 'pinia'
import { productsAPI } from '@/api'

const useProductsStore = defineStore('products', {
  state: () => ({
    products: [],
    productCount: 0,
    productColors: [],
    colorFilter: '',

    product: {}
  }),

  actions: {
    async fetchProduct(id) {
      const response = await productsAPI.fetchProduct(id)

      this.product = response.data

      return response
    },
    async fetchProducts(limit) {
      const response = await productsAPI.fetchProducts(limit)

      this.colorFilter = '';
      this.products = response.data
      this.productColors = this.products
      .map((product) => product.color)
      .filter((c, i, a) => a.indexOf(c) === i);

      return response
    },
    async fetchProductCount() {
      const response = await productsAPI.fetchProductCount()

      this.productCount = response.data.product_count

      return response
    },
    async fetchProductsByColor(color) {
      this.colorFilter = color === this.colorFilter ? '' : color;
      const response = await productsAPI.fetchProductsByColor(this.colorFilter)

      this.products = response.data
      return response
    },
  }
})

export default useProductsStore
