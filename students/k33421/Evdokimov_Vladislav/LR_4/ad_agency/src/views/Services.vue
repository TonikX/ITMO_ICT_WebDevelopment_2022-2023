<template>
  <h1>Услуги агенства</h1>
  <div v-for="service in services" :key="service.id">
    <h1>{{ service.title }}</h1>
    <div><strong>Описание: </strong> {{ service.description_service }}</div>
    <div><strong>Цена: </strong> {{ service.price }}</div>
    <div><strong> &nbsp;</strong></div>
  </div>
  <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/`)">На главную</v-btn>
</template>

<script>
import axios from "axios";
/* eslint-disable */
export default {

 data() {
   return {
     services: [],
   }
 },
 methods: {
   async getServices () {
     try {
       const response = await axios.get('http://127.0.0.1:8000/services/')
       console.log(response.data)
       this.services = response.data
     } catch (e) {
       alert('ERROR')
     }
   }
 },
 mounted() {
   this.getServices()
 }
}
</script>
