<template>
  <base-layout>
    <nav-bar />
    <div id="roomPage">
      <div class="container col-7 justify-content-center py-4">
        <h1 class="text-center">{{ nameHotel }}</h1>
        <div class="row">
          <div class="col-6">
            <p class="fs-2 text-center">Type: <span class="fs-3">{{ typeRoom }}</span></p>
            <p class="fs-2 text-center">Price: <span class="fs-3">{{ price }} rub</span></p>
          </div>
          <div class="col-6">
            <p class="fs-2 text-center">Description:
              <span v-if="des" class="fs-3">{{ des }}</span>
              <span v-else class="fs-3">We don't have any descriptions...</span>
            </p>
          </div>
        </div>
        <ul class="navbar-nav">
          <li class="nav-item" v-for="room in rooms.rt_room" :key="room.id">
            <room-item class="mx-0 px-0" :number_room="room.number_room" :status_room="room.status_room" :review_room="room.review_room" />
            <p class="d-flex justify-content-center" id="lookButton">
              <RouterLink class="nav-link btn-text w-100 text-center fs-5" :to="{name: 'room', params: {id: room.id}}">Look</RouterLink>
            </p>
          </li>
        </ul>
      </div>
    </div>
  </base-layout>
</template>

<script>
import {mapActions, mapState} from "pinia";

import useHotelsStore from "@/stores/hotels";

import BaseLayout from "@/layouts/BaseLayout.vue";
import RoomItem from "@/components/RoomItem.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "RoomPage",

  components: { NavBar, RoomItem, BaseLayout },

  data() {
    return {
      nameHotel: "",
      typeRoom: "",
      rating: "",
      price: "",
      des: ""
    }
  },

  props: {
    id: {
      type: String,
      required: true
    }
  },

  computed: {
    ...mapState(useHotelsStore, ['rooms'])
  },

  methods: {
    ...mapActions(useHotelsStore, ['loadRooms'])
  },

  async mounted() {
    await this.loadRooms(this.id)
    this.nameHotel = this.rooms.hotel_rt.name_hotel
    this.typeRoom = this.rooms.type_rt
    this.rating = this.rooms.rating_rt
    this.price = this.rooms.price_rt
    this.des = this.rooms.des_rt
  }
}
</script>

<style scoped>
h1 {
  color: black;
}

.btn-text {
  color: black !important;
}

#lookButton {
  background-color: #E0E7E9;
  border-radius: 0px 0px 8px 8px;
}

#roomPage {
  min-height: 100vh;
}
</style>