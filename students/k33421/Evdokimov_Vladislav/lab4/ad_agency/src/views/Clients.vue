<template>
  <h1>Клиенты Агенства</h1>
  <div v-for="client in clients" :key="client.id">
    <h1> {{ client.legal_entity }}</h1>
    <div><strong>Контактное лицо: </strong> {{ client.contact_person }}</div>
    <div><strong>Номер телефона: </strong> {{ client.phone_num }}</div>
    <div><strong>Электронный адрес: </strong> {{ client.email }}</div>
    <div><strong>Банковские реквизиты: </strong> {{ client.bank_details }}</div>
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
     clients: [],
   }
 },
 methods: {
   async getClients () {
     try {
       const response = await axios.get('http://127.0.0.1:8000/client/')
       console.log(response.data)
       this.clients = response.data
     } catch (e) {
       alert('ERROR')
     }
   }
 },
 mounted() {
   this.getClients()
 }
}
</script>