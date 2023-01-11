<template>
  <v-app>
    <bar-layout>
        <RegistrationBar />
      </bar-layout>
      <main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
      <br><br><br><br><br>
      <h1 style="text-align: center;" > Регистрация библиотекарей  </h1>
      <br>
      <v-col cols="6" class="mx-auto">
      <v-card max-width = 800 color = "#f7f4ef">
        <v-row class = "py-2">
          <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Логин"
              v-model="signUpForm.username"
              name="username"
              placeholder="dashusik1702"
            />
          </v-col>
          </v-row>
          <v-row>
          <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Имя"
              v-model="signUpForm.first_name"
              name="first_name"
              placeholder="Дарья"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Фамилия"
              v-model="signUpForm.last_name"
              name="last_name"
              placeholder="Балдина"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Номер телефона"
              v-model="signUpForm.phone"
              name="phone"
              placeholder="+796175639020"
            />
          </v-col>
        </v-row>
        <v-row>
        <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Адрес"
              v-model="signUpForm.address"
              name="address"
              placeholder="Простоквашино 1"
            />
          </v-col>
        </v-row>
        <v-row>
        <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Номер читательского билета"
              v-model="signUpForm.card_number"
              name="card_number"
              placeholder="123"
            />
          </v-col>
        </v-row>
        <v-row>
        <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Дата рождения"
              v-model="signUpForm.date_of_birth"
              name="date_of_birth"
              placeholder="2022-02-21"
            />
          </v-col>
        </v-row>
        <v-row>
        <v-col cols="5" class="mx-auto">
          <v-select
            v-model="signUpForm.education"
            :items="educationOptions"
            label="Образование"
          ></v-select>
          </v-col>
        </v-row>
        <v-row>
        <v-col cols="4" class="mx-auto"></v-col>
        <v-checkbox
            v-model="signUpForm.degree"
            :label="'Учёная степень'"
          ></v-checkbox>
        </v-row>
        <v-row>
          <v-col cols="5" class="mx-auto">
            <v-text-field
              label="Password"
              v-model="signUpForm.password"
              name="password"
              type = password
            />
          </v-col>
        </v-row>
        <v-col cols="5" class="mx-auto">
        <v-btn block color = "blue" @click.prevent = "register()"> Register</v-btn>
        </v-col>
      </v-card>
    </v-col>
      </main>
      </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import RegistrationBar from '@/components/RegistrationBar.vue'
import axios from 'axios'
export default {
  name: 'SignUp',
  components:{ BarLayout, RegistrationBar},
  data: () => ({
    signUpForm: {
      username: '',
      password: '',
      first_name: '',
      last_name: '',
      card_number: '',
      date_of_birth: '',
      education: '',
      degree: '',
      passport: '',
      address: '',
      phone: ''
    },
    educationOptions: ['Среднее общее', 'Среднее специальное',
      'Высшее', 'Неоконченное высшее', 'Неоконченное среднее']
  }),
  methods: {
    async register () {
      try {
        await axios.post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        this.$router.push({ name: 'Login' })
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
        } else if (e.response.data.card_number) {
          alert('Номер билета: ' + e.response.data.card_number)
        } else if (e.response.data.date_of_birth) {
          alert('Дата рождения: ' + e.response.data.date_of_birth)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.degree) {
          alert('Учёная степень: ' + e.response.data.degree)
        } else if (e.response.data.passport) {
          alert('Паспортные данные: ' + e.response.data.passport)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone) {
          alert('Телефон: ' + e.response.data.phone)
        } else {
          console.error(e.message)
        }
      
      }
    }
  }
}
</script>