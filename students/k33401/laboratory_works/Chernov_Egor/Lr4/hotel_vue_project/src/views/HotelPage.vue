<template>
  <base-layout>
    <nav-bar />
    <div id="hotelPage">
      <div class="container col-8 py-4">
        <h1 class="text-center">Our hotels</h1>
        <ul class="navbar-nav p-3">
          <li class="nav-item" v-for="hotel in hotels" :key="hotel.id">
            <hotel-item class="mx-0 px-0" :name_hotel="hotel.name_hotel" :address_hotel="hotel.address_hotel" :des_hotel="hotel.des_hotel" />
            <p class="d-flex justify-content-center" id="lookButton">
              <RouterLink class="nav-link btn-text w-100 text-center fs-5" :to="{name: 'room_types', params: {id: hotel.id}}">Look</RouterLink>
            </p>
          </li>
        </ul>
      </div>
    </div>
  </base-layout>
</template>

<script>
import { mapActions, mapState } from 'pinia'

import useHotelsStore from "@/stores/hotels";

import BaseLayout from "@/layouts/BaseLayout.vue";
import HotelItem from "@/components/HotelItem.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "HotelPage",

  components: { BaseLayout, HotelItem, NavBar },

  computed: {
    ...mapState(useHotelsStore, ['hotels'])
  },

  methods: {
    ...mapActions(useHotelsStore, ['loadHotels'])
  },

  mounted() {
    this.loadHotels()
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

#hotelPage {
  min-height: 100vh;
}
</style>