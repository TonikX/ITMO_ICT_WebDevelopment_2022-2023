<template>
  <div class="app">
    <h1>Редактирование данных пользователя</h1>
    <v-form @submit.prevent class="my-0">
      <v-row>
        <v-col class="mx-auto">
          <v-text-field
            label="Фамилия"
            class="input"
            type="text"
            v-model="profileChangeForm.org_surname"/>
          <v-text-field
            label="Имя"
            class="input"
            type="text"
            v-model="profileChangeForm.org_name"/>
          <v-text-field
            label="Отчество"
            class="input"
            type="text"
            v-model="profileChangeForm.org_patronymic"/>
          <v-text-field
            label="Номер телефона"
            class="input"
            v-model="profileChangeForm.org_phone_number"
            type="tel"/>
          <v-text-field
            label="Паспортные данные"
            class="input"
            v-model="profileChangeForm.org_passport"
            type="number"/>
          <v-text-field
            label="Электронная почта"
            class="input"
            v-model="profileChangeForm.org_email"
            type="email"/>
          <div class="d-flex align-center flex-column flex-md-row">
            <v-btn variant="outlined" color="success" rounded="lg" @click="changeProfile">Изменить</v-btn></div><br>
          <div class="d-flex align-center flex-column flex-md-row">
            <v-btn variant="outlined" color="warning" rounded="lg" @click="goBack">Назад</v-btn></div>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: 'ProfileChange',
  data: () => ({
    profileChangeForm: {
      org_surname: '',
      org_name: '',
      org_patronymic: '',
      org_phone_number: '',
      org_passport: '',
      org_email: ''
    }
  }),
  // created () {
  //   this.loadOrganizerData()
  // }
  methods: {
    async loadOrganizerData() {
      const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
        headers: {
          Authorization: `Token ${sessionStorage.getItem('auth_token')}`
        }
      })
      console.log(response.data)
      this.profileChangeForm.org_surname = response.data.org_surname
      this.profileChangeForm.org_name = response.data.org_name
      this.profileChangeForm.org_patronymic = response.data.org_patronymic
      this.profileChangeForm.org_phone_number = response.data.org_phone_number
      this.profileChangeForm.org_passport = response.data.org_passport
      this.profileChangeForm.org_email = response.data.org_email
    },
    changeProfile() {
      axios.patch(`http://127.0.0.1:8000/auth/users/me/`, {
        org_surname: this.profileChangeForm.org_surname,
        org_name: this.profileChangeForm.org_name,
        org_patronymic: this.profileChangeForm.org_patronymic,
        org_phone_number: this.profileChangeForm.org_phone_number,
        org_passport: this.profileChangeForm.org_passport,
        org_email: this.profileChangeForm.org_email,
      }, {
        headers: {
          Authorization: `Token ${sessionStorage.getItem('auth_token')}`
        }
      })
      this.$router.push({ name: 'profile' })
    },
    goBack() {
      this.$router.push({ name: 'profile'})
    }
  },
  mounted() {
    this.loadOrganizerData()
  }
}
</script>


