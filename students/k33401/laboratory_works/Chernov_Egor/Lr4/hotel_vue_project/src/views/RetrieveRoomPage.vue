<template>
  <base-layout>
    <nav-bar />
    <div id="retrieveRoomPage">
      <div class="container col-8 justify-content-center py-4">
        <h1 class="text-center">{{ nameHotel }}</h1>
        <retrieve-room :review_room="review" :number_room="number" :status_room="status" :des_rt="des" :price_rt="price" :type_rt="type" />
        <a class="nav-link text-center py-2 fs-5" @click="goToRegOrAuth()" id="actButton">Choose</a>
        <h2 class="text-center py-4">Comments:</h2>
        <div v-for="comment in comments" :key="comment.id">
          <comment-room v-if="comment.room_com.rt_r.id === room.id" :username="comment.user_com.username" :rating_com="comment.rating_com" :review_com="comment.review_com" :check_in_com="comment.check_in_com" :check_out_com="comment.check_out_com"/>
        </div>
        <comment-form v-if="isAuth" :idRoom="idRoom" />
      </div>
    </div>
  </base-layout>
</template>

<script>
import {mapActions, mapState} from "pinia";

import useHotelsStore from "@/stores/hotels";
import useRegComStore from "@/stores/regCom";

import BaseLayout from "@/layouts/BaseLayout.vue";
import RetrieveRoom from "@/components/RetrieveRoom.vue";
import CommentRoom from "@/components/CommentRoom.vue";
import NavBar from "@/components/NavBar.vue";
import CommentForm from "@/components/CommentForm.vue";

export default {
  name: "RetrieveRoomPage",

  components: { NavBar, CommentForm, RetrieveRoom, CommentRoom, BaseLayout },

  props: {
    id: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      isAuth: "",
      review: "",
      number: 0,
      status: "",
      des: "",
      price: 0,
      type: "",
      nameHotel: "",
      idRoom: this.id
    }
  },

  computed: {
    ...mapState(useHotelsStore, ['room']),
    ...mapState(useRegComStore, ['comments'])
  },

  methods: {
    ...mapActions(useHotelsStore, ['loadRoom']),

    ...mapActions(useRegComStore, ['loadComments']),

    goToRegOrAuth() {
      const user = localStorage.getItem('idUser')
      // console.log(localStorage.getItem('api_token'))
      // if (user) {
      //   this.$router.push({name: "bookRoom", params: {id: roomId}})
      // } else {
      //   this.$router.push({name: "regUser", params: {id: roomId}})
      // }
      if (user) {
        localStorage.setItem('idBookRoom', this.id)
        this.$router.push({name: "booking"})
      } else {
        localStorage.setItem('idBookRoom', this.id)
        this.$router.push({name: "login"})
      }
    },

    addComment() {

    }
  },

  async mounted() {
    this.isAuth = localStorage.getItem('idUser')
    await this.loadRoom(this.id)
    this.review = this.room.review_room
    this.number = this.room.number_room
    this.status = this.room.status_room
    this.des = this.room.rt_r.des_rt
    this.price = this.room.rt_r.price_rt
    this.type = this.room.rt_r.type_rt
    this.nameHotel = this.room.hotel_r.name_hotel
    await this.loadComments()
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
}

#actButton {
  background-color: #E0E7E9;
  border-radius: 0px 0px 8px 8px;
}

#retrieveRoomPage {
  min-height: 100vh;
}
</style>