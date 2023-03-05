<template>
    <div class="app">
      <h1>Registration</h1>
      <v-form @submit.prevent="Registration" ref="RegistrationForm" class="my-0">
        <v-row>
          <v-col class="mx-auto">
            <v-text-field
                v-model="RegistrationForm.username"
                label="Login"
                class="input"
                type="text"
                placeholder="Login"/>
            <v-text-field
                v-model="RegistrationForm.password"
                label="Password"
                class="input"
                type="text"
                placeholder="Password"/>
            <v-text-field
                v-model="RegistrationForm.surname"
                label="Surname"
                class="input"
                type="text"
                placeholder="Surname"/>
            <v-text-field
                v-model="RegistrationForm.name"
                label="Name"
                class="input"
                type="text"
                placeholder="Name"/>
            <v-text-field
                v-model="RegistrationForm.patronymic"
                label="Patronymic"
                class="input"
                type="text"
                placeholder="Patronymic"/>
            <v-text-field
                v-model="RegistrationForm.phone_number"
                label="Phone"
                class="input"
                type="tel"
                placeholder="Phone"/>
            <v-text-field
                v-model="RegistrationForm.passport"
                label="Passport"
                class="input"
                type="number"
                placeholder="Passport"/>
            <v-text-field
                v-model="RegistrationForm.mail"
                label="E-mail"
                class="input"
                type="email"
                placeholder="E-mail"/>
            <v-btn variant="tonal" color="error" rounded="pill" @click="makeRegistration">Sign up</v-btn>
          </v-col>
        </v-row>
      </v-form>
      <br>
      <p class="mt-0">Have registered yet?<br>
        <router-link to="/login/">Log in</router-link></p>
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
          surname: '',
          name: '',
          patronymic: '',
          phone_number: '',
          passport: '',
          mail: ''
        }
      }),
      methods: {
        makeRegistration() {
          $.ajax({
            url: "http://127.0.0.1:8000/auth/users/",
            type: "POST",
            data: {
              username: this.RegistrationForm.username,
              password: this.RegistrationForm.password,
              surname: this.RegistrationForm.surname,
              name: this.RegistrationForm.name,
              patronymic: this.RegistrationForm.patronymic,
              phone_number: this.RegistrationForm.phone_number,
              passport: this.RegistrationForm.passport,
              mail: this.RegistrationForm.mail
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
              } else if (response.data.surname) {
                alert("Фамилия: " + response.data.surname)
              } else if (response.data.name) {
                alert("Имя: " + response.data.name)
              } else if (response.data.patronymic) {
                alert("Отчество: " + response.data.patronymic)
              } else if (response.data.phone_number) {
                alert("Номер телефона: " + response.data.phone_number)
              } else if (response.data.passport) {
                alert("Паспорт: " + response.data.passport)
              } else if (response.data.mail) {
                alert("Электронная почта: " + response.data.mail)
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