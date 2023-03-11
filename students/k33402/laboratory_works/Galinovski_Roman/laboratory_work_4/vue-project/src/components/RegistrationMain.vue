<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <section class="form-signin">
      <b-form  @submit.prevent="Registration" ref="RegistrationForm"  @submit="makeRegistration" class="my-2">
        <centered-heading text="Регистрация" />
  
        <b-form-input
          v-model="RegistrationForm.username"
          label="Login"
          class="input"
          type="text"
          placeholder="Login"/>
        <b-form-input
        v-model="RegistrationForm.password"
        label="Password"
        class="input"
        type="text"
        placeholder="Password"/>
        <b-form-input
        v-model="RegistrationForm.surname"
        label="Surname"
        class="input"
        type="text"
        placeholder="Surname"/>
        <b-form-input
        v-model="RegistrationForm.name"
        label="Name"
        class="input"
        type="text"
        placeholder="Name"/>
        <b-form-input
        v-model="RegistrationForm.patronymic"
        label="Patronymic"
        class="input"
        type="text"
        placeholder="Patronymic"/>
        <b-form-input
        v-model="RegistrationForm.phone_number"
        label="Phone"
        class="input"
        type="tel"
        placeholder="Phone"/>
        <b-form-input
        v-model="RegistrationForm.phone_number"
        label="Phone"
        class="input"
        type="tel"
        placeholder="Phone"/>
        <b-form-input
        v-model="RegistrationForm.passport"
        label="Passport"
        class="input"
        type="number"
        placeholder="Passport"/>
        <b-form-input
        v-model="RegistrationForm.mail"
        label="E-mail"
        class="input"
        type="email"
        placeholder="E-mail"/>
        <big-button text="Зарегистрироваться" />
      </b-form>
      </section>
    </main>
  </template>
  
  <script>
  import $ from "jquery"
  import CenteredHeading from "./CenteredHeading.vue"
  import CenteredFormInput from "./CenteredFormInput.vue"
  import Checkbox from "./Checkbox.vue"
  import BigButton from "./BigButton.vue"
  export default {
    name: "RegistrationMain",
    components: {
      CenteredHeading,
      CenteredFormInput,
      Checkbox,
      BigButton
    },
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
  .form-signin {
    max-width: 400px;
    padding: 15px;
    margin: auto;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  #registerPasswordInput {
    margin-bottom: -1px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  #rePasswordInput {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  </style>
  