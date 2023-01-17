<template>
  <base-layout>
    <h1>{{ rooms.hotel_rt.name_hotel }}</h1>
    <h2>{{ rooms.type_rt }} type rooms:</h2>
    <h3>Price for room is {{ rooms.price_rt }}</h3>
    <ul class="">
      <li class="row" v-for="room in rooms.rt_room" :key="room.id">
        <room-item class="col" :number_room="room.number_room" :status_room="room.status_room" :review_room="room.review_room" />
        <RouterLink to="/hotel/room_type/{{ room.id }}/">Look</RouterLink>
      </li>
    </ul>
  </base-layout>
</template>

<script>
import {mapActions, mapState} from "pinia";

import useHotelsStore from "@/stores/hotels";

import BaseLayout from "@/layouts/BaseLayout.vue";
import RoomItem from "@/components/RoomItem.vue";

export default {
  name: "RoomPage",

  components: { RoomItem, BaseLayout },

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

  mounted() {
    this.loadRooms(this.id)
  }
}
</script>

<style scoped>

</style>