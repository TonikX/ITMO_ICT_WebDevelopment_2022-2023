<template>
   <div class="app">
     <h1>Participants</h1>
       <a href="/" style="text-decoration: none; color: #283593">Home</a><br><br>
      <!--<button v-on:click="fetchParticipants">Get list of participants</button>-->

     <participants-list
         v-bind:participants="participants"
     > 
     </participants-list>
   </div>
</template>

<script>


import ParticipantsList from "./ParticipantsList.vue";
import axios from "axios";
/* eslint-disable */
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
       alert('Error')
     }
   }

 },
 mounted() {
   this.fetchParticipants() 

 }
}
</script>