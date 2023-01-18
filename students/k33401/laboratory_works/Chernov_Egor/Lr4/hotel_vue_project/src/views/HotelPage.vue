<template>
  <base-layout>
    <nav-bar />
    <h1>Mountain hotels:</h1>
    <ul class="">
      <li class="row" v-for="hotel in hotels" :key="hotel.id">
        <hotel-item class="col" :name_hotel="hotel.name_hotel" :address_hotel="hotel.address_hotel" :des_hotel="hotel.des_hotel" />
        <RouterLink :to="{name: 'room_types', params: {id: hotel.id}}">Look</RouterLink>
      </li>
    </ul>
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

</style>