<template>
  <h1>Создание сотрудника</h1>
  <v-form @submit.prevent class="my-0">
    <v-row>
      <v-col class="mx-auto">
        <v-text-field
            v-model="staff.full_name"
            class="input"
            type="text"
            placeholder="ФИО"/>
        <v-text-field
            v-model="staff.phone_num"
            class="input"
            type="text"
            placeholder="Номер телефона"/>
        <v-text-field
            v-model="staff.specialty"
            class="input"
            type="number"
            placeholder="Специализация"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createStaff">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkStaff">Список сотрудников</v-btn></div><br>
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
      staff: {
        full_name: '',
        phone_num: '',
        specialty: '',
      },
    }
  },
  methods: {
    createStaff() {
      axios.post('http://127.0.0.1:8000/staff/create/', {
        title: this.services.title,
        description_service: this.services.description_service,
        price: this.services.price,
      })
    },
    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkStaff() {
      this.$router.push({ name: 'staffList'})
    }
  }
}
</script>

<style scoped>
</style>