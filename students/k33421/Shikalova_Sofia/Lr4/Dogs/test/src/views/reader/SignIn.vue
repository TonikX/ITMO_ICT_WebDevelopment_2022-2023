<template>
  <div class="signIn">
    <h2>Sign In</h2>
    <form
      @submit.prevent="setLogin"
      ref="signInForm"
      class="my-2">
          <input type="text"
                 label="Login"
                 placeholder="Login"
                 v-model="login"
                 name="login">
          <input
            label="Password"
            placeholder="Password"
            v-model="password"
            name="password"
            type="password">
          <button type="submit">Sign In</button>
    </form>
      <router-link to="/show/signup" style="text-decoration: none; color: #283593">I don't have an account</router-link></p>
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
                        alert("Sign in succeed")
                        sessionStorage.setItem("auth_token", response.auth_token)
                        sessionStorage.setItem("username", this.login)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Login or password is incorrect")
                        }
                    }
                })
            }
      }
    }
</script>

<style>
</style>
