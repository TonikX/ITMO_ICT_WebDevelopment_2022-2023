<template>
  <div class="app">
    <h1>Experts for this year's show</h1>
    <a href="/" style="text-decoration: none; color: #198754">Go back to Main</a><br><br>
    <!--<button v-on:click="fetchExperts">Get a list of experts'</button> The button calls the function for getting a list of data (the fetchWarriors function is declared in the block "methods") -->

    <expert-list
        v-bind:experts="experts"
    >
      <!-- Embedding a component that calls a list of objects. v-bind - the directive is used for the so-called data binding - data binding (data is declared in the data () block (see code below)). -->
    </expert-list>
  </div>
</template>



<script>
/* eslint-disable */

import ExpertList from "./ExpertList.vue";
import axios from "axios";

export default {
 components: {
   ExpertList
 },

 data() { // data - is a function that returns an object with data
   return {
     experts: [], // An array of data (passed to the WarriorList component, retrieved data using the fetchWarriors function
   }
 },
 methods: { // methods. This is an object that contains a list of Javascript functions that should be executed depending on what actions the user performs.
   async fetchExperts () { // async function to get data
     try {
       for (let i = 1; i < 4; i++) {
          const response = await axios.get('http://127.0.0.1:8000/experts/' + String(i) + '?format=json') // Making a GET request to the Backend server. The request will return JSON.
          console.log(response.data)
          this.experts.push(response.data)
       }
        
     } catch (err) {
       alert('Error')
     }
   }

 },
 mounted() {
   this.fetchExperts() // Vue calls the mount() hook when the component is added to the DOM. In this example, it takes longer to load
 }
}
</script>

<style>


</style>