<template>
  <div class="container w-75 mt-5">
    <h1 class="mb-5">Update / create </h1>
    <div class="row">
      <div class="col col-6 mb-3">
        <label for="game" class="form-label fw-bold">Game</label>
        <select class="form-select bg-secondary-own text-main-own" aria-label="Platform" id="game">

        </select>
      </div>
      <div class="col col-3 mb-3">
        <label for="platform" class="form-label fw-bold">Platform</label>
        <select class="form-select bg-secondary-own text-main-own" aria-label="Platform" id="platform"
        ></select>
      </div>
      <div class="col col-3 mb-3">
        <label for="price" class="form-label fw-bold">Price</label>
        <input class="form-control bg-secondary-own text-main-own" type="number" v-model="price" id="price">
      </div>
      <div class="col col-3 mb-3">
        <label for="count" class="form-label fw-bold">Count</label>
        <input class="form-control bg-secondary-own text-main-own" type="number" id="count" v-model="count">
      </div>
    </div>
    <button type="submit" class="btn btn-primary" v-on:click="updateGame()">Submit</button>
  </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBazzarStore from "@/stores/bazzar";

export default {
  name: "Product",
  computed: {
    ...mapState(useBazzarStore, ['games', 'token'])
  },
  data() {
    return {
      product: null,
      count: 0,
      price: 0
    }
  },
  methods: {
    ...mapActions(useBazzarStore, ['loadProduct', 'updateProduct', 'loadGames', 'createProduct', 'loadPlatforms']),
    updateGame: async function () {
      const params = new URLSearchParams(window.location.search)
      if (params.has('productId')) {
        const id = params.get('productId')
        const response = await this.updateProduct(id, this.token, this.count)
      } else {
        const game = document.getElementById('game').value
        const platform = document.getElementById('platform').value
        const response = await this.createProduct(this.token, Number(game), Number(platform), this.price, this.count)
      }
      document.location = document.location.origin
    }
  },
  async mounted() {
    const resp1 = await this.loadGames()
    for (const g of resp1.data) {
      document.getElementById('game').innerHTML += `<option value="${g.id}">${g.name}</option>`
    }
    const resp2 = await this.loadPlatforms()
    for (const g of resp2.data) {
      document.getElementById('platform').innerHTML += `<option value="${g.id}">${g.name}</option>`
    }
    const params = new URLSearchParams(window.location.search)
    if (params.has('productId')) {
      const response = await this.loadProduct(params.get('productId'))
      this.product = await response.data
      this.count = this.product['count']
      this.price = this.product.price
      document.getElementById('game').value = this.product.game.id
      document.getElementById('platform').value = this.product.platform.id
      document.getElementById('game').disabled = true
      document.getElementById('platform').disabled = true
      document.getElementById('price').disabled = true
    }

  }
}
</script>


<style scoped>

</style>