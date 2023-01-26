<template>
  <div class="signup">
    <h2>Sign Up</h2>
    <form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2">

          <input type="text"
            label="login" placeholder="login" v-model="login" name="login">

          <input
            label="password"
            placeholder="password"
            v-model="password"
            name="password"
            type="password">

          <button type="submit">Sign Up</button>

    </form>
    <router-link to="/show/signin" style="text-decoration: none; color: #283593">I already have an account</router-link></p>
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
                alert("Sign up succeed")
                //this.$router.push({ name: 'signin' })
            });
    }
  }
}
</script>

<style>
</style>