<template>
  <div class="signup">
    <h2>Registration</h2>
    <form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2">

          <input type="text"
            label="Логин" placeholder="Логин" v-model="login" name="login">

          <input
            label="Пароль"
            placeholder="Пароль"
            v-model="password"
            name="password"
            type="password">

          <button type="submit">Register</button>

    </form>
    <p class="mt-15">Already register? <router-link to="/show/signin" style="text-decoration: none; color: #198754">Log in</router-link></p>
  </div>
</template>

<script>
/* eslint-disable */
import $ from "jquery";
export default {
  name: 'SignUp',
  data() {
    return {
      login: '',
      password: '',
    }
  },
  methods: {
    async signUp () {
      console.log("1")
      $.ajax({
                type: "POST",
                data: {
                        username: this.login,
                        password: this.password
                },
                url: "http://127.0.0.1:8000/auth/users/"
            }).done(function () {
                console.log(this.data)
                alert("Спасибо за регистрацию")
                //this.$router.push({ name: 'signin' })
            });
    }
  }
}
</script>

<style>
</style>