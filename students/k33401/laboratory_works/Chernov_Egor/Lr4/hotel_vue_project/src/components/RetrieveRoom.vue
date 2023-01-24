<template>
  <div class="px-4 py-3" id="retrieveRoom">
    <p class="fs-2">Room number: <span class="fs-3">{{ number_room }}</span></p>
    <p class="fs-2">Type: <span class="fs-3">{{ type_rt }}</span></p>
    <p class="fs-2">Status: <span class="fs-3">{{ status_room }}</span></p>
    <p class="fs-2">Price: <span class="fs-3">{{ price_rt }}</span></p>
    <p class="fs-3">Description:
      <span v-if="des_rt" class="fs-4">{{ des_rt }}</span>
      <span v-else class="fs-4">We don't have any descriptions...</span>
    </p>
    <p class="fs-3">Review:
      <span v-if="review_room" class="fs-4">{{ review_room }}</span>
      <span v-else>We don't have any reviews...</span>
    </p>
  </div>
</template>

<script>
export default {
  name: "RetrieveRoom",

  props: {
    type_rt: {
      type: String,
      required: true
    },
    price_rt: {
      type: Number,
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
      type: Number,
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
#retrieveRoom {
  background-color: rgba(253, 246, 236, 0.4);;
  border-radius: 8px 8px 0px 0px;
  color: black;
}
</style>