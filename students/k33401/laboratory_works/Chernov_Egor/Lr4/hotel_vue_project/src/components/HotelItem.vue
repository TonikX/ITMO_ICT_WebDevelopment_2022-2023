<template>
  <div class="">
    <h3 class="">Name: {{ name_hotel }}</h3>
    <h4 class="">Address: {{ address_hotel }}</h4>
    <p class="">Description: {{ des_hotel }}</p>
  </div>
</template>

<script>
export default {
  name: "HotelItem",

  props: {
    name_hotel: {
      type: String,
      required: true
    },
    address_hotel: {
      type: String,
      required: true
    },
    des_hotel: {
      type: String,
      required: false
    }
  }
}
</script>

<style scoped>

</style>