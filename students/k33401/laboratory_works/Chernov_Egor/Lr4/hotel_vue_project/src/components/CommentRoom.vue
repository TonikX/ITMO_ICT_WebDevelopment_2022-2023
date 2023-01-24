<template>
  <div class="container my-2" id="commentRoom">
    <div class="row pt-1 px-4" id="commentHeader">
      <p class="col fs-3 text-start">User: <span class="fs-4">{{ username }}</span></p>
      <p class="col fs-3 text-end">Date: <span class="fs-4">{{ check_in_com }} - {{ check_out_com }}</span></p>
    </div>
    <p class="fs-3 px-4 pt-2">Rating: <span class="fs-4">{{ rating_com }}</span></p>
    <p class="fs-3 px-4 pb-2">Review:
      <span v-if="review_com" class="fs-4">{{ review_com }}</span>
      <span v-else class="fs-4">User didn't write a review...</span>
    </p>
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
#commentHeader {
  background-color: #E0E7E9;
  border-radius: 8px 8px 0px 0px;
}

#commentRoom {
  background-color: rgba(253, 246, 236, 0.4);;
  border-radius: 8px 8px 8px 8px;
  color: black;
}
</style>