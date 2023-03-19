<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <LoginNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Вход </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Логин"
                v-model="this.username"
                name="first_name"
                placeholder="SuperDeveloper3000"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Password"
                v-model="this.password"
                name="password"
                type=password
              />
            </v-col>
          </v-row>

          <v-col cols="7" class="mx-auto">
            <v-btn block color="blue" @click.prevent="login()"> Войти </v-btn>
          </v-col>

          <br>
        </v-card>
      </v-col>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import LoginNavigationBar from '@/components/LoginNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'LoginView',
  components: { BarLayout, LoginNavigationBar },
  data() { return { username: '', password: '' } },
  methods: {
    async login() {
      const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
        { username: this.username, password: this.password, }
      )

      if (response.data.auth_token) {
        localStorage.auth_token = response.data.auth_token
        window.location = '/home'
      }
    }
  }
}
</script>
