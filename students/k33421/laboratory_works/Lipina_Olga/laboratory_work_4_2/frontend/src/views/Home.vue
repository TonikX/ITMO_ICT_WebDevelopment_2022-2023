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
          <a v-if="this.authorized" @click="goProfile">Личный кабинет</a>
          <a v-else @click="goSignIn">Войти</a>
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
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },

  methods: {
    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goProfile () {
      this.$router.push({ name: 'reader_profile' })
    },

    goSignIn () {
      this.$router.push({ name: 'signin' })
    }
  }
}
</script>
