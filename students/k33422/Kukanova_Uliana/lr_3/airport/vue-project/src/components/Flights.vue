<template>
   <div class="app">
     <h1>Рейсы</h1>
       <a href="/">Главная</a><br><br>
     <button v-on:click="fetchFlights">Получить список рейсов'</button>

     <flight-list
         v-bind:flights="flights"
     >
     </flight-list>
   </div>
</template>

<script>

import FlightList from "./FlightList.vue";
import axios from "axios";

export default {
 components: {
   FlightList
 },

 data() {
   return {
     flights: [],
   }
 },
 methods: {
   async fetchFlightAsScheduled () {
     try {
       const response = await axios.get('http://127.0.0.1:8000/schedule/?format=json')
       console.log(response.data)
       this.flights = response.data
       } catch (e) {
         alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchFlightAsScheduled()

 }
}
</script>