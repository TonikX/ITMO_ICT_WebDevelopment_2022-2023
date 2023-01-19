<template>
  <form method="post" @submit.prevent="register">
    <div class="container pb-4">
      <router-link class="logo-link" to="/">
        <img class="filter-logo" src="@/assets/wallet2.svg" alt="Wallet" width="50" height="50">
        <p class="fs-3">crypto wallet</p>
      </router-link>
    </div>

    <div class="input-group mb-2">
      <span class="input-group-text bg-side text-light">@</span>
      <div class="form-floating">
        <input v-model="username" type="text" name="username" class="form-control" id="floatingInputGroup1" placeholder="Username">
        <label for="floatingInputGroup1">Username</label>
      </div>
    </div>

    <div class="form-floating mb-2">
      <input v-model="email" type="email" name="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>

    <div class="form-floating pb-5">
      <input v-model="password" type="password" name="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <button class="w-100 btn btn-lg btn-main mb-3" type="submit">Зарегистрироваться</button>

    Уже есть аккаунт? <router-link to="/login" href="signin.html" class="link-side">Войти</router-link>
  </form>
</template>

<script>
import $ from "jquery";

export default {
  name: "RegisterForm",
  data() {
    return {
      username: "",
      email: "",
      password: ""
    }
  },
  methods: {
    register() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/",
        type: "POST",
        data: {
          username: this.username,
          email: this.email,
          password: this.password
        },
        success: () => {
          alert("Вы успешно зарегистрировались!")
          this.$router.push({name: "login"})
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