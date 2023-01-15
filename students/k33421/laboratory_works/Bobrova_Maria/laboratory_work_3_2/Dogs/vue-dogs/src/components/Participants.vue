<template>
   <div class="app">
     <h1>Участники</h1>
       <a href="/">Главная</a><br><br>
     <button v-on:click="fetchParticipants">Получить список участников'</button> 

     <participants-list
         v-bind:participants="participants"
     > 
     </participants-list>
   </div>
</template>

<script>

import ParticipantsList from "./ParticipantsList.vue";
import axios from "axios";

export default {
 components: {
   ParticipantsList
 },

 data() { 
   return {
     participants: [], 
   }
 },
 methods: { 
   async fetchParticipants () { 
     try {
       const response = await axios.get('http://127.0.0.1:8000/participants/?format=json') 
       console.log(response.data)
       this.participants = response.data 
     } catch (e) {
       alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchParticipants() 

 }
}
</script>