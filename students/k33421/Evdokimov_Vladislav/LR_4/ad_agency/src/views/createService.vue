<template>
  <h1>Создание услуги</h1>
  <v-form @submit.prevent class="my-0">
    <v-row>
      <v-col class="mx-auto">
        <v-text-field
            v-model="services.title"
            class="input"
            type="text"
            placeholder="Название"/>
        <v-text-field
            v-model="services.description_service"
            class="input"
            type="text"
            placeholder="Описание"/>
        <v-text-field
            v-model="services.price"
            class="input"
            type="number"
            placeholder="Цена"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createService">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkServices">Список услуг</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline"  rounded="lg" @click="goHome">Назад</v-btn></div>

      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from "axios"
export default {
  name: "ServiceForm",
  data () {
    return {
      services: {
        title: '',
        description_service: '',
        price: '',
      },
    }
  },
  methods: {
    createService() {
      axios.post('http://127.0.0.1:8000/services/create/', {
        title: this.services.title,
        description_service: this.services.description_service,
        price: this.services.price,
      })
    },
    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkServices() {
      this.$router.push({ name: 'services'})
    }
  }
}
</script>

<style scoped>
</style>