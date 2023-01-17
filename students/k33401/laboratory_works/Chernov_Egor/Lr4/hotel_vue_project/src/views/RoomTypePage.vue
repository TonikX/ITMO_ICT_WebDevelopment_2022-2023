<template>
  <base-layout>
    <h1>{{ hotel_room_types.name_hotel }} room types:</h1>
    <ul class="">
      <li class="row" v-for="room_type in hotel_room_types.hotel_room_type" :key="room_type.id">
        <room-type-item class="col" :type_rt="room_type.type_rt" :rating_rt="room_type.rating_rt" :price_rt="room_type.price_rt" :des_rt="room_type.des_rt" />
        <RouterLink :to="{name: 'rooms', params: {id: room_type.id}}">Look</RouterLink>
      </li>
    </ul>
  </base-layout>
</template>

<script>
import {mapActions, mapState} from "pinia";

import useHotelsStore from "@/stores/hotels";

import BaseLayout from "@/layouts/BaseLayout.vue";
import RoomTypeItem from "@/components/RoomTypeItem.vue";

export default {
  name: "RoomTypePage",

  components: {RoomTypeItem, BaseLayout },

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

</style>