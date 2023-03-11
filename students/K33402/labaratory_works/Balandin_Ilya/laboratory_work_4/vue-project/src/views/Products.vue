<template>
  <div class="container w-75">
    <h1 class="m-5">Catalog</h1>
    <filter-products></filter-products>
    <div class="row justify-content-evenly mt-5" id="productsPage">
      <div class="col col-md-4 my-4" v-for="p in products">
        <product-card :name="p.game.name" :id="p.id" :description="p.game.description"
        :platform="p.platform.name" :count="p.count" :price="p.price" :genre="p.game.genre.name" :image="p.game.image"></product-card>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import FilterProducts from "@/components/Filter.vue";
import useBazzarStore from "@/stores/bazzar";
import ProductCard from "@/components/ProductCard.vue";


export default {
  name: "Products",
  components: {ProductCard, FilterProducts},
  computed: {
    ...mapState(useBazzarStore, ['products'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['loadProducts'])
  },
  mounted() {
    const params = new URLSearchParams(window.location.search)
    if (params.has('genre')){
      document.getElementById('genre').value = params.get('genre')
    }
    if (params.has('platform')){
      document.getElementById('platform').value = params.get('platform')
    }
    this.loadProducts(window.location.search)
  }
}
</script>

<style scoped>

</style>