<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <section class="form-signin">
      <b-form  @submit.prevent="Login" ref="LoginForm"  @submit="setLogin" class="my-2">
        <centered-heading text="Вход в аккаунт" />
  
        <b-form-input
        v-model="LoginForm.username"
        labelText="Login"
        class="input"
        type="text"
        placeholder="Login"/>
        <b-form-input
        v-model="LoginForm.password"
        class="input"
        labelText="Password"
        type="password"
        placeholder="Password"/>
        <big-button text="Войти"/>
      </b-form>
    </section>
    </main>
  </template>
  
  <script>
  import $ from "jquery"
  import CenteredHeading from "./CenteredHeading.vue"
  import CenteredFormInput from "../components/CenteredFormInput.vue"
  import Checkbox from "../components/Checkbox.vue"
  import BigButton from "./BigButton.vue"
  export default {
    name: "LoginMain",
    components: {
      CenteredHeading,
      CenteredFormInput,
      Checkbox,
      BigButton
    },
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
                this.$router.push({name: 'Index'})
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
  .form-signin {
    max-width: 330px;
    padding: 15px;
    margin: auto;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  </style>