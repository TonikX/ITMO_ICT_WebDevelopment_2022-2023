<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Добро пожаловать на фестиваль косплеев!</h2>
      </v-card-title>  
      <v-card-text>
        <h3>
          <a href="/participation" style="text-decoration: none;">Участия</a><br>
          <a href="/experts" style="text-decoration: none;">Эксперты</a><br>
          <a href="/participants" style="text-decoration: none;">Участники</a> <br>
          <template  v-if="this.authorized">
            <a @click="goProfile">Личный кабинет</a><br>
            <a @click="goLogOut">Выйти</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn">Войти</a><br>
            <router-link to="/cosplay/signup">Зарегистрироваться</router-link>
          </template>
        </h3>
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
    console.log('token is ' + sessionStorage.getItem('auth_token'))
    console.log('username is ' + sessionStorage.getItem('username'))
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
