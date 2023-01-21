<template>
  <base-layout>
    <nav-bar />
    <h1>{{ nameHotel }}</h1>
    <h2>{{ typeRoom }} type rooms:</h2>
    <h3>Price for room is {{ price }}</h3>
    <ul class="">
      <li class="row" v-for="room in rooms.rt_room" :key="room.id">
        <room-item class="col" :number_room="room.number_room" :status_room="room.status_room" :review_room="room.review_room" />
        <RouterLink :to="{name: 'room', params: {id: room.id}}">Look</RouterLink>
      </li>
    </ul>
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
      price: ""
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
    this.price = this.rooms.price_rt
  }
}
</script>

<style scoped>

</style>