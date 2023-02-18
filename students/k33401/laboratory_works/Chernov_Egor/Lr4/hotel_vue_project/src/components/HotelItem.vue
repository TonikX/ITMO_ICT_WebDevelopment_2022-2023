<template>
  <div class="row" id="hotelItem">
    <div class="col-6">
      <p class="fs-2">{{ name_hotel }}</p>
      <p class="fs-4">Address: <span class="fs-5">{{ address_hotel }}</span></p>
    </div>
    <div class="col-6">
      <p class="fs-2">Description:</p>
      <p v-if="des_hotel" class="fs-5">{{ des_hotel }}</p>
      <p v-else class="fs-5">We don't have any descriptions...</p>
    </div>
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
#hotelItem {
  background-color: rgba(253, 246, 236, 0.4);
  border-radius: 8px 8px 0px 0px;
  color: black;
}
</style>