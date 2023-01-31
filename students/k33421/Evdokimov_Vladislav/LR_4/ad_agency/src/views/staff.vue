<template>
  <h1>Сотрудники Агенства</h1>
  <div v-for="staff in staffs" :key="staff.id">
    <h1> {{ staff.full_name }}</h1>
    <div><strong>Номер телефона: </strong> {{ staff.phone_num }}</div>
    <div><strong>Специализация: </strong> {{ staff.specialty }}</div>
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
     staffs: [],
   }
 },
 methods: {
   async getStaff () {
     try {
       const response = await axios.get('http://127.0.0.1:8000/staff/')
       console.log(response.data)
       this.staffs = response.data
     } catch (e) {
       alert('Ошибка')
     }
   }
 },
 mounted() {
   this.getStaff()
 }
}
</script>