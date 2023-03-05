<template>
    <div>
      <v-card
        class="mx-auto"
        width="700"
        height="700"
        variant="plain"
      >
        <template v-slot:title>
          <h1>Dog Exhibition</h1>
        </template>
        <v-card-text>
            <template v-if="auth">
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal" rounded="pill" @click="myProfile">Profile</v-btn></div><br>
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal"  rounded="pill" @click="goDog">Dog List</v-btn></div><br>
             <div class="d-flex align-center flex-column flex-md-row">
               <v-btn variant="tonal"  rounded="pill" @click="goDogCreate">Add new dog</v-btn></div><br>
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal"  rounded="pill" @click="goRegistered">List of participation</v-btn></div><br>
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal" rounded="pill" @click="goRegisteredCreate">Add new registered dog</v-btn></div><br>
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal" color="error" rounded="pill" @click="goLogout">Log out</v-btn></div>
            </template>
            <template v-else>
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal" color="warning" rounded="pill" @click="goLogin">Log in</v-btn></div><br>
              <div class="d-flex align-center flex-column flex-md-row">
                <v-btn variant="tonal" color="error" rounded="pill" @click="goRegistration">Sign in</v-btn></div>
            </template>
        </v-card-text>
      </v-card>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
    data: () => ({
      authorized: false
    }),
    computed: {
      auth() {
         if (sessionStorage.getItem('auth_token')) {
           return true
         }
      }
    },
    methods: {
      myProfile () {
        this.$router.push({ name: 'profile'})
      },
      goDog () {
        this.$router.push({ name: 'dogs' })
      },
      goRegistered () {
        this.$router.push({ name: 'dog_registered' })
      },
      goLogout () {
        sessionStorage.removeItem("auth_token")
        alert("You are logged out")
        window.location = '/'
      },
      goLogin () {
        this.$router.push({ name: 'login' })
      },
      goRegistration () {
        this.$router.push({ name: 'registration' })
      },
      goDogCreate () {
        this.$router.push({ name: 'dogs_create' })
      },
      goRegisteredCreate () {
        this.$router.push({ name: 'dog_registered_create'})
      }
    }
  }
  </script>
  