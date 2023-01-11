<template>
  <div class="app">
    <h1>Регистрация</h1>
<!--    <form @submit.prevent="Registration" ref="RegistrationForm">-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Логин: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.username"-->
<!--              class="input"-->
<!--              type="text"-->
<!--              placeholder="Логин"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Пароль: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.password"-->
<!--              class="input"-->
<!--              type="password"-->
<!--              placeholder="Пароль"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Фамилия организатора: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.org_surname"-->
<!--              class="input"-->
<!--              type="text"-->
<!--              placeholder="Фамилия"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Имя организатора: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.org_name"-->
<!--              class="input"-->
<!--              type="text"-->
<!--              placeholder="Имя"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Отчество организатора: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.org_patronymic"-->
<!--              class="input"-->
<!--              type="text"-->
<!--              placeholder="Отчество"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Номер телефона: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.org_phone_number"-->
<!--              class="input"-->
<!--              type="tel"-->
<!--              placeholder="Телефон"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Паспорт: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.org_passport"-->
<!--              class="input"-->
<!--              type="number"-->
<!--              placeholder="Паспорт"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Электронная почта: </strong>-->
<!--          <input-->
<!--              v-model="RegistrationForm.org_email"-->
<!--              class="input"-->
<!--              type="email"-->
<!--              placeholder="Адрес почты"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <button class="btn" type="submit" v-on:click="makeRegistration">Зарегистрироваться</button>-->
<!--    </form>-->
    <v-form @submit.prevent="Registration" ref="RegistrationForm" class="my-0">
      <v-row>
        <v-col class="mx-auto">
          <v-text-field
              v-model="RegistrationForm.username"
              label="Логин"
              class="input"
              type="text"
              placeholder="Логин"/>
          <v-text-field
              v-model="RegistrationForm.password"
              label="Пароль"
              class="input"
              type="text"
              placeholder="Пароль"/>
          <v-text-field
              v-model="RegistrationForm.org_surname"
              label="Фамилия"
              class="input"
              type="text"
              placeholder="Фамилия"/>
          <v-text-field
              v-model="RegistrationForm.org_name"
              label="Имя"
              class="input"
              type="text"
              placeholder="Имя"/>
          <v-text-field
              v-model="RegistrationForm.org_patronymic"
              label="Отчество"
              class="input"
              type="text"
              placeholder="Отчество"/>
          <v-text-field
              v-model="RegistrationForm.org_phone_number"
              label="Номер телефона"
              class="input"
              type="tel"
              placeholder="Номер телефона"/>
          <v-text-field
              v-model="RegistrationForm.org_passport"
              label="Паспортные данные"
              class="input"
              type="number"
              placeholder="Паспорт"/>
          <v-text-field
              v-model="RegistrationForm.org_email"
              label="Адрес электронной почты"
              class="input"
              type="email"
              placeholder="Электроная почта"/>
          <v-btn variant="outlined" color="primary" rounded="lg" @click="makeRegistration">Зарегистрироваться</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <br>
    <p class="mt-0">Уже зарегистрированы?<br>
      <router-link to="/login/">Войти</router-link></p>
  </div>
</template>

<script>
  import $ from "jquery"
  export default {
    name: 'Registration',
    data: () => ({
      RegistrationForm: {
        username: '',
        password: '',
        org_surname: '',
        org_name: '',
        org_patronymic: '',
        org_phone_number: '',
        org_passport: '',
        org_email: ''
      }
    }),
    methods: {
      // async signUp () {
      //   try {
      //     await this.axios.post('http://127.0.0.1:8000/auth/users/', this.RegistrationForm)
      //     this.$refs.RegistrationForm.reset()
      //     await this.$router.push({ name: 'login' })
      //   } catch (e) {
      //     if (e.response.data.non_field_errors) {
      //       alert(e.response.data.non_field_errors)
      //     } else if (e.response.data.username) {
      //       alert('Логин: ' + e.response.data.username)
      //     } else if (e.response.data.password) {
      //       alert('Пароль: ' + e.response.data.password)
      //     } else if (e.response.data.name) {
      //       alert('Имя: ' + e.response.data.name)
      //     } else if (e.response.data.library_pass) {
      //       alert('Номер билета: ' + e.response.data.library_pass)
      //     } else if (e.response.data.birth_date) {
      //       alert('Дата рождения: ' + e.response.data.birth_date)
      //     } else if (e.response.data.education_level) {
      //       alert('Образование: ' + e.response.data.education_level)
      //     } else if (e.response.data.degree) {
      //       alert('Учёная степень: ' + e.response.data.degree)
      //     } else if (e.response.data.address) {
      //       alert('Адрес: ' + e.response.data.address)
      //     } else if (e.response.data.phone_number) {
      //       alert('Телефон: ' + e.response.data.phone_number)
      //     } else {
      //       console.error(e.message)
      //     }
      //   }
      // }
      makeRegistration() {
        $.ajax({
          url: "http://127.0.0.1:8000/auth/users/",
          type: "POST",
          data: {
            username: this.RegistrationForm.username,
            password: this.RegistrationForm.password,
            org_surname: this.RegistrationForm.org_surname,
            org_name: this.RegistrationForm.org_name,
            org_patronymic: this.RegistrationForm.org_patronymic,
            org_phone_number: this.RegistrationForm.org_phone_number,
            org_passport: this.RegistrationForm.org_passport,
            org_email: this.RegistrationForm.org_email
          },
          success: (response) => {
            console.log(response)
            alert("Вы успешно зарегистрировались")
            this.$router.push({name: 'login'})
          },
          error: (response) => {
            if (response.data.username) {
              alert("Логин: " + response.data.username)
            } else if (response.data.password) {
              alert("Пароль: " + response.data.password)
            } else if (response.data.org_surname) {
              alert("Фамилия: " + response.data.org_surname)
            } else if (response.data.org_name) {
              alert("Имя: " + response.data.org_name)
            } else if (response.data.org_patronymic) {
              alert("Отчество: " + response.data.org_patronymic)
            } else if (response.data.org_phone_number) {
              alert("Номер телефона: " + response.data.org_phone_number)
            } else if (response.data.org_passport) {
              alert("Паспорт: " + response.data.org_passport)
            } else if (response.data.org_email) {
              alert("Электронная почта: " + response.data.org_email)
            } else {
              alert(response.message)
            }
          }
        })
      }
    }
  }
</script>

<style>
</style>


