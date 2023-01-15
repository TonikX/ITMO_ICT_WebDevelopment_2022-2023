<template>
  <base-layout>
    <h1>Mountain hotels:</h1>
    <div class="">
      <div class="row" v-for="hotel in hotels" :key="hotel.id">
        <hotel-item :name_hotel="hotel.name_hotel" :address_hotel="hotel.address_hotel" :des_hotel="hotel.des_hotel" />
      </div>
    </div>
  </base-layout>
</template>

<script>
import { mapActions, mapState } from 'pinia'

import useHotelsStore from "@/stores/hotels";

import BaseLayout from "@/layouts/BaseLayout.vue";
import HotelItem from "@/components/HotelItem.vue";


export default {
  name: "HotelPage",

  components: { BaseLayout, HotelItem },

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