<template>
  <div class="free-rooms-count">
    <h5 class="free-rooms-title">For the date {{ date }}</h5>
    <h5 class="free-rooms-count">Amount of free rooms: {{ text }}</h5>
  </div>
</template>

<script>
export default {
  name: "FreeRooms",
  props: {
    text: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },
};
</script>
