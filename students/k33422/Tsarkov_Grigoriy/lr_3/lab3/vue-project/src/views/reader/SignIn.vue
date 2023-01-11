<template>
  <div class="signIn">
    <h2>Авторизация</h2>
    <form
      @submit.prevent="setLogin"
      ref="signInForm"
      class="my-2">
          <input type="text"
                 label="Логин"
                 placeholder="Логин"
                 v-model="login"
                 name="login">
          <input
            label="Пароль"
            placeholder="Пароль"
            v-model="password"
            name="password"
            type="password">
          <button type="submit">Авторизоваться</button>
    </form>
    <p class="mt-15">Ещё нет аккаунта?<br>
      <router-link to="/cosplays/signup">Зарегистрироваться</router-link></p>
  </div>
</template>

<script>

import $ from "jquery";
import axios from "axios";
    export default {
      name: "AuthModals",
      data() {
        return {
          login: '',
          password: '',
        }
      },
      methods: {
        setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Авторизация успешна")
                        sessionStorage.setItem("auth_token", response.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Неверный логин или пароль!")
                        }
                    }
                })
            }
      }
    }
</script>

<style>
</style>
