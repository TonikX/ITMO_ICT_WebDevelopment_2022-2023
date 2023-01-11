<template>
  <h1>Информация о пользователе</h1>
  <div><strong>Фамилия: </strong> {{ this.organizer.org_surname }}</div>
  <div><strong>Имя: </strong> {{ this.organizer.org_name }}</div>
  <div><strong>Отчество: </strong> {{ this.organizer.org_patronymic }}</div>
  <div><strong>Номер телефона: </strong> {{ this.organizer.org_phone_number }}</div>
  <div><strong>Паспортные данные: </strong> {{ this.organizer.org_passport }}</div>
  <div><strong>Электронная почта: </strong> {{ this.organizer.org_email }}</div>
  <div class="d-flex align-center flex-column flex-md-row">
    <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/profile/change/`)">Изменить</v-btn></div><br>
  <div class="d-flex align-center flex-column flex-md-row">
    <v-btn variant="outlined"  color="warning" rounded="lg" @click="goBack">Назад</v-btn></div>
</template>

<script>
import axios from "axios";
export default {
  name: 'Profile',

  data () {
    return {
      organizer: Object
    }
  },
  // created () {
  //   this.loadOrganizerData()
  // },
  methods: {
    async loadOrganizerData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
        console.log(response.data)
        this.organizer = response.data
      } catch (e) {
        alert('Error')
      }
    },
    goBack() {
      this.$router.push({ name: 'home'})
    }
  },
  mounted() {
    this.loadOrganizerData()
  }
}
</script>

