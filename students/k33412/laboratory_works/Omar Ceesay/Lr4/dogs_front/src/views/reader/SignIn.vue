<template>
  <div class="signIn">
    <h2>Login to Start</h2>
    <form
      @submit.prevent="setLogin"
      ref="signInForm"
      class="my-2">
          <input type="text" label="login" placeholder="login" v-model="login" name="login">
          <input label="password" placeholder="password" v-model="password" name="password" type="password">
          <button type="submit">Login</button>
    </form>
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
                        alert("Appreciate your interest")
                        sessionStorage.setItem("auth_token", response.auth_token)
                        sessionStorage.setItem("username", this.login)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Incorrect Pasword")
                        }
                    }
                })
            }
      }
    }
</script>

<style>
  h2{
    font-size: 24px;
  }
  button{
  background-color:rgb(211, 252, 255);
    border: none;
    color: rgb(0, 0, 0);
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
  }
</style>
