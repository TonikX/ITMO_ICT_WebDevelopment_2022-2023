<template>
  <div class="signup">
    <h2>Регистрация</h2>
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

          <button type="submit">Зарегистрироваться</button>

    </form>
    <p class="mt-15">Уже зарегистрированы? <router-link to="/cosplays/signin">Войти</router-link></p>
  </div>
</template>

<script>
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
                this.$router.push({ name: 'signin' })
            });
    }
  }
}
</script>

<style>
</style>