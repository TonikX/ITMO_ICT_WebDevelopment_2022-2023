<template>
  <div class="container">
    <h3 class="row my-2">{{ nameHotel }} {{ checkIn }} - {{ checkOut }}</h3>
    <h4 class="row my-2">{{ roomType }} - {{ price }}</h4>
    <h4 class="row my-2">Room number {{ roomNumber }}</h4>
    <p class="row my-2">Status registration: {{ statusReg }}</p>
    <p class="row my-2">Status payment: {{ statusPay }}</p>
    <p class="row my-2">Booked: {{ booking }}</p>
  </div>
</template>

<script>
export default {
  name: "RegItem",

  props: {
    nameHotel: {
      type: String,
      required: true
    },
    checkIn: {
      type: String,
      required: true
    },
    checkOut: {
      type: String,
      required: true
    },
    roomType: {
      type: String,
      required: true
    },
    price: {
      type: Number,
      required: true
    },
    roomNumber: {
      type: Number,
      required: true
    },
    statusReg: {
      type: String,
      required: true
    },
    statusPay: {
      type: String,
      required: true
    },
    booking: {
      type: String,
      required: true
    },
  }
}
</script>

<style scoped>

</style>