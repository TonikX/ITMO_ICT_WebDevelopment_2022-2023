<template>
  <h1>Создание клиента</h1>
  <v-form @submit.prevent class="my-0">
    <v-row>
      <v-col class="mx-auto">
        <v-text-field
            v-model="client.legal_entity"
            label="Юр.лицо"
            class="input"
            type="text"
            placeholder="Название"/>
        <v-text-field
            v-model="client.contact_person"
            label="Контактное лицо"
            class="input"
            type="text"
            placeholder="Инициалы"/>
        <v-text-field
            v-model="client.phone_num"
            label="Номер телефона"
            class="input"
            type="number"
            placeholder="Номер"/>
        <v-text-field
            v-model="client.email"
            label="Почта юр.лица"
            class="input"
            type="email"
            placeholder="Почта"/>
        <v-text-field
            v-model="client.bank_details"
            label="Счёт юр.лица"
            class="input"
            type="number"
            placeholder="Счёт"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createClient">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkClient">Список клиентов</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline"  rounded="lg" @click="goHome">Назад</v-btn></div>

      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from "axios"
export default {
  name: "ClientForm",
  data () {
    return {
      client: {
        legal_entity: '',
        contact_person: '',
        phone_num: '',
        email: '',
        bank_details: '',
      },
    }
  },
  methods: {
    createClient() {
      axios.post('http://127.0.0.1:8000/client/create/', {
        legal_entity: this.client.legal_entity,
        contact_person: this.client.contact_person,
        phone_num: this.client.phone_num,
        email: this.client.email,
        bank_details: this.client.bank_details,
      })
    },
    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkClient() {
      this.$router.push({ name: 'clients'})
    }
  }
}
</script>

<style scoped>
</style>