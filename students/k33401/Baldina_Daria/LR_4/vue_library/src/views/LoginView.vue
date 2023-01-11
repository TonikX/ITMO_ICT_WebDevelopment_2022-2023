<template>
    <v-app>
      <bar-layout>
          <LoginBar />
        </bar-layout>
        <v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
        <br><br><br><br><br>
        <h1 style="text-align: center;" > Вход в учетную запись  </h1>
        <br>
        <v-col cols="4" class="mx-auto">
        <v-card max-width = 600 color = "#f7f4ef">
          <v-row class = "py-2">
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Username"
                v-model="username"
                name="username"
                placeholder="username"
              />
            </v-col>
            </v-row>
          <v-row>
            <v-col cols="5" class="mx-auto">
              <v-text-field
                label="Password"
                v-model="password"
                name="password"
                type = password
              />
            </v-col>
          </v-row>
          <v-col cols="5" class="mx-auto">
          <v-btn block color = "blue" @click.prevent = "login()"> Войти </v-btn>
          </v-col>
        </v-card>
      </v-col>
        </v-main>
        </v-app>
  </template>
  
  <script>
  import BarLayout from '@/layouts/BarLayout.vue'
  import LoginBar from '@/components/LoginBar.vue'
  import axios from 'axios'
  export default {
    name: 'LogIn',
    components:{ BarLayout, LoginBar},
    data () { 
          return {
                  username: '',
                  password: '',
              }
      
          }
        ,
        methods: {
    async login() {
        const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
              {
                username: this.username,
                password: this.password,
              })
        if (response.data.auth_token) {
            localStorage.auth_token = response.data.auth_token
            window.location = '/home'
            
        }
          }
    
        }
      }
  </script>
