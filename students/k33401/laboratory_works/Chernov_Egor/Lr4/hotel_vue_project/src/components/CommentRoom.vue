<template>
  <div>
    <h4>User: {{ username }}</h4>
    <p>Date: {{ check_in_com }} - {{ check_out_com }}</p>
    <p>Starts: {{ rating_com }}</p>
    <p v-if="review_com">Review: {{ review_com }}</p>
  </div>
</template>

<script>
export default {
  name: "CommentRoom",

  props: {
    username: {
      type: String,
      required: true
    },
    rating_com: {
      type: Number,
      required: true
    },
    review_com: {
      type: String,
      required: false
    },
    check_in_com: {
      type: String,
      required: true
    },
    check_out_com: {
      type: String,
      required: true
    },
  }
}
</script>

<style scoped>

</style>