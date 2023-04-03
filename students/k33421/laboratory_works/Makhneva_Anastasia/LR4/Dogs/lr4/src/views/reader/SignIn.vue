<template>
  <div class="signIn">
    <h2>авторизация</h2>
    <form
      @submit.prevent="setLogin"
      ref="signInForm"
      class="my-2">
          <input type="text"
                 label="логин"
                 placeholder="логин"
                 v-model="login"
                 name="login">
          <input
            label="пароль"
            placeholder="пароль"
            v-model="password"
            name="password"
            type="password">
          <button type="submit">авторизоваться</button>
    </form>
    <p class="mt-15">ещё нет аккаунта?<br>
      <router-link to="/show/signup" style="text-decoration: none; color: #2e061a">зарегистрироваться</router-link></p>
  </div>
</template>

<script>
/* eslint-disable */

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
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem("auth_token", response.auth_token)
                        sessionStorage.setItem("username", this.login)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("логин или пароль не верны")
                        }
                    }
                })
            }
      }
    }
</script>

<style>
</style>
