<template>
  <div class="">
    <h3 class="">Type {{ type_rt }}</h3>
    <h4 class="">Price: {{ price_rt }}</h4>
    <p class="">Rating: {{ rating_rt }}</p>
    <p v-if="des_rt">Description: {{ des_rt }}</p>
  </div>
</template>

<script>
export default {
  name: "RoomTypeItem",

  props: {
    type_rt: {
      type: String,
      required: true
    },
    rating_rt: {
      type: String,
      required: true
    },
    price_rt: {
      type: String,
      required: true
    },
    des_rt: {
      type: String,
      required: false
    }
  }
}
</script>

<style scoped>

</style>