<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <RegistrationNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Регистрация </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Имя"
                v-model="form.first_name"
                name="first_name"
                placeholder="Ilia"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Фамилия"
                v-model="form.last_name"
                name="last_name"
                placeholder="Chub"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Логин"
                v-model="form.username"
                name="first_name"
                placeholder="SuperDeveloper3000"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Password"
                v-model="form.password"
                name="password"
                type=password
              />
            </v-col>
          </v-row>

          <v-col cols="7" class="mx-auto">
            <v-btn block color="blue" @click.prevent="register()"> Зарегистрироваться </v-btn>
          </v-col>
          <br>
        </v-card>
      </v-col>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import RegistrationNavigationBar from '@/components/RegistrationNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'RegistrationView',
  components: {BarLayout, RegistrationNavigationBar},
  data: () => ({
    form: {
      first_name: '',
      last_name: '',
      username: '',
      password: ''
    },
  }),
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/auth/users/', this.form)

        const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
          {
            username: this.form.username,
            password: this.form.password,
          })

        if (response.data.auth_token) {
          localStorage.auth_token = response.data.auth_token
          window.location = '/finish_complete_info'
        }

        this.$router.push({ name: 'FinishCompleteInfoView' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.username) {
          alert('Логин: ' + e.response.data.username)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.first_name) {
          alert('Имя: ' + e.response.data.first_name)
        } else if (e.response.data.last_name) {
          alert('Фамилия: ' + e.response.data.last_name)
        } else {
          alert(e.error.message)
        }
      }
    }
  }
}
</script>
