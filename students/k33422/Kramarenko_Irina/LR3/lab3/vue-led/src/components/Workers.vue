<template>
   <div class="app">
     <h1>Работники</h1>
       <a href="/">Главная</a><br><br>
     <button v-on:click="fetchWorker">Вывести список работников</button>

     <workers-list
         v-bind:workers="workers"
     > 
     </workers-list>
   </div>
</template>

<script>

import WorkersList from "./WorkersList.vue";
import axios from "axios";

export default {
 components: {
   WorkersList
 },

 data() { 
   return {
     workers: [],
   }
 },
 methods: { 
   async fetchWorker () {
     try {
       const response = await axios.get('http://localhost:8000/airport/workers/?format=json')
       console.log(response.data)
       this.workers = response.data
     } catch (e) {
       alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchWorker()

 }
}
</script>