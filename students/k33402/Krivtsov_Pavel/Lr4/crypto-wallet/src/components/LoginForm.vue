<template>
  <form method="post" @submit.prevent="login">
    <div class="container pb-4">
      <router-link class="logo-link" to="/">
        <img class="filter-logo" src="@/assets/wallet2.svg" alt="Wallet" width="50" height="50">
        <p class="fs-3">crypto wallet</p>
      </router-link>
    </div>

    <div class="form-floating mb-2">
      <input v-model="username" name="username" class="form-control" id="floatingInput" placeholder="username">
      <label for="floatingInput">Username</label>
    </div>

    <div class="form-floating pb-5">
      <input v-model="password" type="password" name="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <button class="w-100 btn btn-lg btn-main mb-3" type="submit">Sign in</button>

    Нет аккаунта? <router-link to="/register" class="link-side">Зарегистрироваться</router-link>
  </form>
</template>

<script>
import $ from "jquery"

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    login() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login",
        type: "POST",
        data: {
          username: this.username,
          password: this.password
        },
        success: (response) => {
          localStorage.setItem("auth_token", response.auth_token)
          $.ajaxSetup({headers: {'Authorization': "Token" + " " + response.auth_token}})
          this.$router.push({name: "welcome"})
        },
        error: (response) => {
          alert(Object.values(response.responseJSON)[0])
          this.password = ""
        }
      })
    }
  }
}
</script>

<style>

</style>