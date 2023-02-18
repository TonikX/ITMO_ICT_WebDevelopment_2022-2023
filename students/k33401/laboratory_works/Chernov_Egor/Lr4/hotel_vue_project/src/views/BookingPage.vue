<template>
  <base-layout>
    <nav-bar />
    <div id="bookingPage">
      <div class="container col-3 py-4">
        <h1 class="text-center mb-4">Registration</h1>
        <reg-form :idHotel="room.hotel_r.id" :nameHotel="room.hotel_r.name_hotel" :idRoomType="room.rt_r.id" :typeRoom="room.rt_r.type_rt" :numberRoom="room.number_room" />
      </div>
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import RegForm from "@/components/RegRoomForm.vue";
import {mapActions, mapState} from "pinia";
import useHotelsStore from "@/stores/hotels";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "BookingPage",

  components: { NavBar, RegForm, BaseLayout },

  computed: {
    ...mapState(useHotelsStore, ['room'])
  },

  methods: {
    ...mapActions(useHotelsStore, ['loadRoom']),
  },

  mounted() {
    this.loadRoom(localStorage.getItem('idBookRoom'))
  }
}
</script>

<style scoped>
#bookingPage {
  min-height: 100vh;
}
</style>