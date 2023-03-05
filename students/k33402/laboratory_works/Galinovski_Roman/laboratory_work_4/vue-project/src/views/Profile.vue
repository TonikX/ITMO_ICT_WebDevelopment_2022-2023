<template>
    <h1>Information about user</h1>
    <div><strong>Surname: </strong> {{ this.organizer.surname }}</div>
    <div><strong>Name: </strong> {{ this.organizer.name }}</div>
    <div><strong>Patronymic: </strong> {{ this.organizer.patronymic }}</div>
    <div><strong>Phone: </strong> {{ this.organizer.phone_number }}</div>
    <div><strong>Passport data: </strong> {{ this.organizer.passport }}</div>
    <div><strong>E-mail: </strong> {{ this.organizer.mail }}</div>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="tonal" rounded="pill" @click="$router.push(`/profile/change/`)">Edit</v-btn></div><br>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="tonal" color="error"  rounded="pill" @click="goBack">Back</v-btn></div>
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