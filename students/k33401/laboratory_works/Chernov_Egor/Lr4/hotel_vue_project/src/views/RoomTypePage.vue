<template>
  <base-layout>
    <nav-bar />
    <div id="roomTypePage">
      <div class="container col-7 justify-content-center py-4">
        <h1 class="text-center">{{ hotel_room_types.name_hotel }}</h1>
        <ul class="navbar-nav p-3">
          <li class="nav-item" v-for="room_type in hotel_room_types.hotel_room_type" :key="room_type.id">
            <room-type-item class="mx-0 px-0" :type_rt="room_type.type_rt" :rating_rt="room_type.rating_rt" :price_rt="room_type.price_rt" :des_rt="room_type.des_rt" />
            <p class="d-flex justify-content-center" id="lookButton">
              <RouterLink class="nav-link btn-text w-100 text-center fs-5" :to="{name: 'rooms', params: {id: room_type.id}}">Look</RouterLink>
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
import RoomTypeItem from "@/components/RoomTypeItem.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "RoomTypePage",

  components: { NavBar, RoomTypeItem, BaseLayout },

  props: {
    id: {
      type: String,
      required: true
    }
  },

  computed: {
    ...mapState(useHotelsStore, ['hotel_room_types'])
  },

  methods: {
    ...mapActions(useHotelsStore, ['loadHotelRoomTypes'])
  },

  mounted() {
    this.loadHotelRoomTypes(this.id)
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

#roomTypePage {
  min-height: 100vh;
}
</style>