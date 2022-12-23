<template>
<div class="col-12 col-sm-6 col-md-4 col-lg-3">
  <RouterLink :to="`/products/${id}`" class="text-black nav-link">
    <div class="card border border-0">
      <img
        :src="photo"
        class="card-img-top img-fluid"
        :alt="name"
        width="306"
        height="391"
      >
      <div class="card-body px-0">
        <h4 class="card-title h6">{{ name }}</h4>
        <p class="card-text">{{ price }}</p>
      </div>
    </div>
  </RouterLink>
</div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
    id: {
      type: Number,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    price: {
      type: String,
      required: true
    },
    photo: {
      type: String,
      required: true
    }
  }
}
</script>