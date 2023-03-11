<template>
  <div class="card bg-secondary-own">
    <img :src="image" class="img img-fluid" alt="game image">
    <div class="card-body">
      <router-link class="card-title h3 text-decoration-none" :to="link" >{{ name }}</router-link>
      <p class="card-text">{{ description }}</p>
      <p class="h5">${{ price }} / {{ count }} left</p>
    </div>
    <div class="card-body">
      <a class="text-decoration-none">{{ genre }}</a>
      /
      <a class="text-decoration-none">{{ platform }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductCard",
  props: {
    image: {
      required: true
    },
    id: {
      required: true
    },
    name: {
      required: true
    },
    description: {
      required: true
    },
    price: {
      required: true
    },
    count: {
      required: true
    },
    genre: {
      required: true
    },
    platform: {
      required: true
    }
  },
  data() {
    return {
      link: "/product"
    }
  },
  mounted() {
    this.link += `?productId=${this.id}`
  }
}
</script>

<style scoped>

</style>