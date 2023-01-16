<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Добро пожаловать на шоу собак!</h2>
      </v-card-title>  
      <v-card-text>
        <h2>
          <a href="/participation" style="text-decoration: none; color: #4E342E">Участия</a><br>
          <a href="/experts" style="text-decoration: none; color: #4E342E">Эксперты</a><br>
          <a href="/participants" style="text-decoration: none; color: #4E342E">Участники</a> <br>
          <template  v-if="this.authorized">
            <a @click="goProfile" style="text-decoration: none; color: #4E342E">Личный кабинет</a><br>
            <a @click="goLogOut" style="text-decoration: none; color: #4E342E">Выйти</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn" style="text-decoration: none; color: #4E342E">Войти</a><br>
            <router-link to="/show/signup" style="text-decoration: none; color: #4E342E">Зарегистрироваться</router-link>
          </template>
        </h2>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src
/* eslint-disable */

export default {
  name: 'Home',

  data: () => ({
    authorized: false
  }),

  created () {
    console.log('hehe' + ' ' + sessionStorage.getItem('auth_token'))
    console.log('hehe' + ' ' + sessionStorage.getItem('username'))
    if (sessionStorage.getItem('auth_token')) {
      if (sessionStorage.getItem('auth_token') !== '-1') {
        this.authorized = true
      }
    }
  },

  methods: {

    goProfile () {
      this.$router.push({ name: 'profile' })
    },

    goLogOut () {
      this.$router.push({ name: 'logout' })
    },

    goSignIn () {
      this.$router.push({ name: 'signin' })
    }
  }
}
</script>
