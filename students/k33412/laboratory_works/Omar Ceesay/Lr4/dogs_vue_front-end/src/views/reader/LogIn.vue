<template>
  <div class="container" :class="signup">
    <div class="overlay-container">
      <div class="overlay">
        <div class="wrapper">
          <div class="signIn signIn__wrapper">
            <h2>Login to Start</h2>
            <form
                @submit.prevent="setLogin"
                ref="signInForm"
                class="my-2 signUp__form">
              <v-text-field
                  label="login"
                  v-model="login"
                  name="login"
                  type="text"
              ></v-text-field>
              <v-text-field
                  label="password"
                  v-model="password"
                  name="password"
                  type="password"
              ></v-text-field>
              
              
              <v-btn depressed elevation="2" type="submit">Login</v-btn>
            </form>
          </div>
        </div>
      </div>
    </div>
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
          alert("Authorization completed")
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
.signUp__form{
  display: flex;
  align-items: center;
  flex-direction: column;
  row-gap: 14px;

}
.signIn__wrapper{
  background: rgb(29, 29, 29);
  display: flex;
  align-items: center;
  flex-direction: column;
  row-gap: 12px;
  border-radius: 12px;
  padding: 12px;
}
.wrapper{
  padding: 24px;
  background: rgb(211, 252, 255);
  border-radius: 12px;
}

.input{
  padding: 6px;
  border: 1px solid rgb(235, 235, 235);
  border-radius: 16px;
}
.btn{
  background-color:rgb(211, 252, 255);
  border: none;
  color: rgb(0, 0, 0);
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
h2 {
  font-size: 24px;
  color: #fff
}

button {
  background-color: rgb(211, 252, 255);
  border: none;
  color: rgb(0, 0, 0);
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>
