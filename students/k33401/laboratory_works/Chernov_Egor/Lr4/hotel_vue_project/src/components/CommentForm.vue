<template>
  <div class="container text-center mt-4 p-4" id="commentForm">
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="checkIn">Check in</span>
      <input v-model="checkIn" type="date" class="form-control" aria-describedby="checkIn">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="checkOut">Check out</span>
      <input v-model="checkOut" type="date" class="form-control" aria-describedby="checkOut">
    </div>
    <div class="input-group mb-3">
      <label class="input-group-text" style="width: 110px" for="rating">Rating</label>
      <select v-model="rating" class="form-select" id="rating">
        <option selected>How many stars...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
        <option value="4">Four</option>
        <option value="5">Five</option>
        <option value="6">Six</option>
        <option value="7">Seven</option>
        <option value="8">Eight</option>
        <option value="9">Nine</option>
        <option value="10">Ten</option>
      </select>
    </div>
    <div class="input-group">
      <span class="input-group-text" style="width: 110px" id="review">Your review</span>
      <textarea v-model="review" class="form-control" aria-describedby="review"></textarea>
    </div>
    <a class="nav-link py-1 px-2 fs-5 mt-3" @click="addComment" id="postButton">Post</a>
  </div>
</template>

<script>
import { mapActions } from "pinia";
import useRegComStore from "@/stores/regCom";

export default {
  name: "CommentForm",

  props: {
    idRoom: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      checkIn: "",
      checkOut: "",
      rating: "How many stars...",
      review: ""
    }
  },

  methods: {
    ...mapActions(useRegComStore, ['createCom']),

    async addComment() {
      const accessToken = localStorage.getItem('accessToken')
      const idUser = localStorage.getItem('idUser')
      console.log(this.idRoom)
      await this.createCom(accessToken, idUser, this.idRoom, this.checkIn, this.checkOut, this.rating, this.review)
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
}

#commentForm {
  background-color: rgba(253, 246, 236, 0.4);
  border-radius: 8px 8px 8px 8px;
  color: black;
}

#postButton {
  background-color: #E0E7E9;
  border-radius: 8px 8px 8px 8px;
}
</style>