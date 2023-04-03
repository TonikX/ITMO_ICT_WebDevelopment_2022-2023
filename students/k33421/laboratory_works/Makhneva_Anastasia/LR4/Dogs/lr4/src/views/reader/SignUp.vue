<template>
  <div class="signup">
    <h2>регистрация</h2>
    <form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2">

          <input type="text"
            label="логин" placeholder="логин" v-model="login" name="login">

          <input
            label="пароль"
            placeholder="пароль"
            v-model="password"
            name="password"
            type="password">

          <button type="submit">зарегистрироваться</button>

    </form>
    <p class="mt-15">уже зарегистрированы? <router-link to="/show/signin" style="text-decoration: none; color: #2e061a">войти</router-link></p>
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
                alert("спасибо за то что присоединились к нам!")
                //this.$router.push({ name: 'signin' })
            });
    }
  }
}
</script>

<style>
</style>