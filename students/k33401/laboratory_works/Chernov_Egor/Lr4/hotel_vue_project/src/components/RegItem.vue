<template>
  <div class="container my-2" id="regItem">
    <div class="row"  id="regHeader">
      <p class="col fs-3 text-start mt-1 mb-1">{{ nameHotel }}</p>
      <p class="col fs-3 text-end mt-1 mb-1">{{ checkIn }} - {{ checkOut }}</p>
    </div>
    <p class="fs-3">{{ roomType }}: <span class="fs-4">{{ price }}</span></p>
    <p class="fs-3">Room number: <span class="fs-4">{{ roomNumber }}</span></p>
    <p class="fs-3">Status registration: <span class="fs-4">{{ statusReg }}</span></p>
    <p class="fs-3">Status payment: <span class="fs-4">{{ statusPay }}</span></p>
    <div class="row text-center" id="regFooter">
      <p class="fs-3 mt-1 mb-1">Booked: <span class="fs-4">{{ booking }}</span></p>
    </div>
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
#regHeader {
  background-color: #E0E7E9;
  border-radius: 8px 8px 0px 0px;
}

#regItem {
  background-color: rgba(253, 246, 236, 0.4);;
  border-radius: 8px 8px 8px 8px;
  color: black;
}

#regFooter {
  background-color: #E0E7E9;
  border-radius: 0px 0px 8px 8px;
}
</style>