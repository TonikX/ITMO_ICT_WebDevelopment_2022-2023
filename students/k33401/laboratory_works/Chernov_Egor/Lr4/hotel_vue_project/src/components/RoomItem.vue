<template>
  <div>
    <h3 class="">Number: {{ number_room }}</h3>
    <h4 class="">Status: {{ status_room }}</h4>
    <p v-if="review_room">Review: {{ review_room }}</p>
  </div>
</template>

<script>
export default {
  name: "RoomItem",

  props: {
    number_room: {
      type: String,
      required: true
    },
    status_room: {
      type: String,
      required: true
    },
    review_room: {
      type: String,
      required: false
    }
  }
}
</script>

<style scoped>

</style>