<template>
    <div class="app">
      <h1>Editing user data</h1>
      <v-form @submit.prevent class="my-0">
        <v-row>
          <v-col class="mx-auto">
            <v-text-field
              label="Surname"
              class="input"
              type="text"
              v-model="profileChangeForm.surname"/>
            <v-text-field
              label="Name"
              class="input"
              type="text"
              v-model="profileChangeForm.name"/>
            <v-text-field
              label="Patronymic"
              class="input"
              type="text"
              v-model="profileChangeForm.patronymic"/>
            <v-text-field
              label="Phone"
              class="input"
              v-model="profileChangeForm.phone_number"
              type="tel"/>
            <v-text-field
              label="Passport"
              class="input"
              v-model="profileChangeForm.passport"
              type="number"/>
            <v-text-field
              label="E-mail"
              class="input"
              v-model="profileChangeForm.mail"
              type="email"/>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" rounded="pill" @click="changeProfile">Edit</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
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
        surname: '',
        name: '',
        patronymic: '',
        phone_number: '',
        passport: '',
        mail: ''
      }
    }),
    methods: {
      async loadOrganizerData() {
        const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
        console.log(response.data)
        this.profileChangeForm.surname = response.data.surname
        this.profileChangeForm.name = response.data.name
        this.profileChangeForm.patronymic = response.data.patronymic
        this.profileChangeForm.phone_number = response.data.phone_number
        this.profileChangeForm.passport = response.data.passport
        this.profileChangeForm.mail = response.data.mail
      },
      changeProfile() {
        axios.patch(`http://127.0.0.1:8000/auth/users/me/`, {
          surname: this.profileChangeForm.surname,
          name: this.profileChangeForm.name,
          patronymic: this.profileChangeForm.patronymic,
          phone_number: this.profileChangeForm.phone_number,
          passport: this.profileChangeForm.passport,
          mail: this.profileChangeForm.mail,
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