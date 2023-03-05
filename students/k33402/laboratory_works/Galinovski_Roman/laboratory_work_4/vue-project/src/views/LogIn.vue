<template>
    <div class="app">
      <h1>Authorisation</h1>

      <v-form @submit.prevent="Login" ref="LoginForm" class="my-2">
        <v-row>
          <v-col class="mx-auto">
            <v-text-field
                v-model="LoginForm.username"
                label="Login"
                class="input"
                type="text"
                placeholder="Login"/>
            <v-text-field
              v-model="LoginForm.password"
              class="input"
              label="Password"
              type="password"
              placeholder="Password"/>
            <v-btn variant="tonal" color="warning" rounded="pill" @click="setLogin">Log in</v-btn>
          </v-col>
        </v-row>
      </v-form>
      <br>
      <p class="mt-0">No account yet?<br>
        <router-link to="/registration/">Sign in</router-link></p>
    </div>
  </template>
  
  <script>
    import $ from "jquery"
    export default {
      name: 'Login',
      data: () => ({
        LoginForm: {
          username: '',
          password: ''
        }
      }),
      methods: {
        setLogin() {
            $.ajax({
              url: "http://127.0.0.1:8000/auth/token/login/",
              type: "POST",
              data: {
                username: this.LoginForm.username,
                password: this.LoginForm.password,
              },
              success: (response) => {
                console.log(response.auth_token)
                sessionStorage.setItem("auth_token", response.auth_token)
                this.$router.push({name: 'home'})
                alert("You are logged in")
              },
              error: (response) => {
                if (response.status === 400) {
                  alert("Unable to authenticate with such data, please try again")
                }
              }
            })
          }
    }
  }
  </script>
  
  <style>
  </style>