<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Выставки собак</h2><br>
        <h3 style='color: black; text-decoration: none'>
        <a href="/participation">Участия</a><br>
        <a href="/experts">Эксперты</a><br>
        <a href="/participants">Участники</a> <br>
        </h3>
      </v-card-title>
      <v-card-text>
        <h3>
          <template  v-if="this.authorized">
            <a @click="goProfile">Личный кабинет</a><br>
            <a @click="goLogOut">Выйти</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn">Войти</a><br>
            <router-link to="/show/signup">Зарегистрироваться</router-link>
          </template>
        </h3>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',

  data: () => ({
    authorized: false
  }),

  created () {
    console.log('hehe' + ' ' + sessionStorage.getItem('auth_token'))
    if (sessionStorage.getItem('auth_token')) {
      if (sessionStorage.getItem('auth_token') !== '-1') {
        this.authorized = true
      }
    }
  },

  methods: {
    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

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
