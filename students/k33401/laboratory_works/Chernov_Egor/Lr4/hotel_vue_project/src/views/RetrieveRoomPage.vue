<template>
  <base-layout>
    <retrieve-room :review_room="room.review_room" :number_room="room.number_room" :status_room="room.status_room"
                   :des_rt="room.rt_r.des_rt" :price_rt="room.rt_r.price_rt" :type_rt="room.rt_r.type_rt"
                   :name_hotel="room.hotel_r.name_hotel"/>
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

export default {
  name: "RetrieveRoomPage",

  components: {RetrieveRoom, CommentRoom, BaseLayout},

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

  mounted() {
    this.loadRoom(this.id)

    this.loadComments()
  }
}
</script>

<style scoped>

</style>