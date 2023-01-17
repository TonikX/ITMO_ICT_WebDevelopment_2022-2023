<template>
  <div>
    <h1>{{ name_hotel }}</h1>
    <h2>Room number: {{ number_room }}</h2>
    <h3>{{ type_rt }}</h3>
    <h4>Status: {{ status_room }}</h4>
    <p>Price: {{ price_rt }}</p>
    <p v-if="des_rt">Description: {{ des_rt }}</p>
    <p v-if="review_room">Review: {{ review_room }}</p>
  </div>
</template>

<script>
export default {
  name: "RetrieveRoom",

  props: {
    name_hotel: {
      type: String,
      required: true
    },
    type_rt: {
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
    },
    status_room: {
      type: String,
      required: true
    },
    number_room: {
      type: String,
      required: true
    },
    review_room: {
      type: String,
      required: false
    },
  }
}
</script>

<style scoped>

</style>