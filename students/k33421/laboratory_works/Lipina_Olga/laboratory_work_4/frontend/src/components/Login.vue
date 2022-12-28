<template>
<div>
  <input v-model="login" type="text" placeholder="Login"/>
  <input v-model="password" type="password" placeholder="Password"/>
  <button @click="setLogin">Войти</button>
  <br>
</div>
</template>

<script>
import $ from 'jquery'
export default {
  name: "Login",
  data() {
    return {
      login: '',
      password: '',
    }
  },
  methods: {
    setLogin() {
      $.ajax({
        // url: 'http://localhost:8000/auth/jwt/create/',
        url: 'http://localhost:8000/api/token/',
        type: "POST",
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          alert('Спасибо что вы с нами!')
          console.log(response)
        },
        error: (response) => {
          alert('Неверные данные!')
          sessionStorage.set_item("auth_token", response.auth_token )
           console.log(response.data.attributions.auth_token)
        }
      })
    },
  }
}
</script>

<style scoped>

</style>