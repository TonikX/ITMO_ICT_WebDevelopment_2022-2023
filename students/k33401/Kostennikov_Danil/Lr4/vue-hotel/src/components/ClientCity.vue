<template>
  <div class="free-rooms-count">
    <h5 class="free-rooms-title">For the city of {{ city }}</h5>
    <h5 class="free-rooms-count">Amount of clients: {{ count }}</h5>
  </div>
</template>

<script>
export default {
  name: "ClientCity",
  props: {
    city: {
      type: String,
      required: true,
    },
    count: {
      type: String,
      required: true,
    },
  },
};
</script>
