<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Добро пожаловать в библиотеку!</h2>
      </v-card-title>
      <v-card-text>
        <h3><a @click="goCatalogue">Каталог</a><br>
          <template  v-if="this.authorized">
            <a @click="goProfile">Личный кабинет</a><br>
            <a @click="goLogOut">Выйти</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn">Войти</a><br>
            <router-link to="/library/signup">Зарегистрироваться</router-link>
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
    // const response = this.axios.get('http://127.0.0.1:8000/lib/readers/list/')
    console.log('hehe' + ' ' + localStorage.getItem('auth_token'))
    if (localStorage.getItem('auth_token')) {
      if (localStorage.getItem('auth_token') !== '-1') {
        this.authorized = true
      }
    }
  },

  methods: {
    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goProfile () {
      this.$router.push({ name: 'reader_profile' })
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
