<template>
       <h1>Заявки Агенства</h1>
  <div v-for="requst in requsts" :key="requst.id">
    <div><strong>Идентификационный номер заказчика: </strong> {{ requst.client }}</div>
    <div><strong>Дата заявки: </strong> {{ requst.req_date }}</div>
    <div><strong>Объем работ: </strong> {{ requst.workload }}</div>
    <div><strong>Дата начала работ: </strong> {{ requst.start_date }}</div>
    <div><strong>Дата окончания работ: </strong> {{ requst.end_date }}</div>
    <div><strong>Итоговая стоимость: </strong> {{ requst.final_price }}</div>
    <div><strong>Состояние: </strong> {{ requst.status }}</div>
    <div><strong>Дата оплаты: </strong> {{ requst.payment }}</div>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/`)">На главную</v-btn></div>
    <div><strong> &nbsp;</strong></div>
  </div>
</template>

<script>
import axios from "axios";
/* eslint-disable */
export default {

 data() {
   return {
     requsts: [],
   }
 },
 methods: {
   async getServices () {
     try {
       const response = await axios.get('http://127.0.0.1:8000/request/')
       console.log(response.data)
       this.requsts = response.data
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
