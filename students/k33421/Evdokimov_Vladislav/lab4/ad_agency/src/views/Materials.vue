<template>
  <h1>Материалы</h1>
  <div v-for="material in materials" :key="material.id">
    <h1> {{ material.title }}</h1>
    <div><strong>Описание: </strong> {{ material.description_material }}</div>
    <div><strong>Цена: </strong> {{ material.price }}</div>
    <div><strong> &nbsp;</strong></div>
  </div>
  <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/`)">На главную</v-btn>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
 data() {

   return {
     materials: [],
   }
 },
 methods: {
   async getMaterials () {
     try {
       const response = await axios.get('http://127.0.0.1:8000/materials')
       console.log(response.data)
       this.materials = response.data
     } catch (e) {
       alert('ERROR')
     }
   }
 },
 mounted() {
   this.getMaterials()
 }
}
</script>