<template>
  <base-layout>
    <nav-bar />
    <retrieve-room :review_room="review" :number_room="number" :status_room="status"
                   :des_rt="des" :price_rt="price" :type_rt="type"
                   :name_hotel="nameHotel"/>
    <button @click="goToRegOrAuth()">Choose</button>
    <h3>Comments:</h3>
    <div v-for="comment in comments" :key="comment.id">
      <comment-room v-if="comment.room_com.rt_r.id === room.id" :username="comment.user_com.username"
                    :rating_com="comment.rating_com" :review_com="comment.review_com"
                    :check_in_com="comment.check_in_com" :check_out_com="comment.check_out_com"/>
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

export default {
  name: "RetrieveRoomPage",

  components: { NavBar, RetrieveRoom, CommentRoom, BaseLayout },

  data() {
    return {
      review: "",
      number: 0,
      status: "",
      des: "",
      price: 0,
      type: "",
      nameHotel: ""
    }
  },

  props: {
    id: {
      type: String,
      required: true
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
    }
  },

  async mounted() {
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

</style>