<template>
  <div class="row" id="roomTypeItem">
    <div class="col-6 text-center">
      <p class="fs-2">Type {{ type_rt }}</p>
      <p class="fs-4">Price: <span class="fs-5">{{ price_rt }}</span></p>
      <p class="fs-4">Rating: <span class="fs-5">{{ rating_rt }}</span></p>
    </div>
    <div class="col-6 text-center">
      <p class="fs-2">Description:</p>
      <p v-if="des_rt" class="fs-5">{{ des_rt }}</p>
      <p v-else class="fs-5">We don't have any description...</p>
    </div>
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
      type: Number,
      required: true
    },
    price_rt: {
      type: Number,
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
#roomTypeItem {
  background-color: rgba(253, 246, 236, 0.4);;
  border-radius: 8px 8px 0px 0px;
  color: black;
}
</style>