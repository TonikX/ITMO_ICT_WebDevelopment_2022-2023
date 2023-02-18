<template>
  <div class="row px-2 py-2" id="roomItem">
    <p class="col text-start ms-5 fs-3">Number: <span class="fs-4">{{ number_room }}</span></p>
    <p class="col text-end me-5 fs-3">Status: <span class="fs-4">{{ status_room }}</span></p>
    <span class="fs-3">Review:</span>
    <p v-if="review_room" class="fs-4">{{ review_room }}</p>
    <p v-else class="fs-4">We don't have any reviews...</p>
  </div>
</template>

<script>
export default {
  name: "RoomItem",

  props: {
    number_room: {
      type: Number,
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
#roomItem {
  background-color: rgba(253, 246, 236, 0.4);;
  border-radius: 8px 8px 0px 0px;
  color: black;
}
</style>