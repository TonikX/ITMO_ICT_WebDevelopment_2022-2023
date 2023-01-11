<template>
  <v-app>
    <bar-layout> 
      <v-btn v-if="auth" @click="LK()"
        text
      > Личный кабинет
    </v-btn>
      <v-spacer></v-spacer>
    <v-btn v-if="auth" @click="Books()"
        text
      > Книги
    </v-btn>
      <v-btn v-if="auth" @click="goLogout()"
        text
      > Выход
    </v-btn>
      </bar-layout>
      <v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
      <br><br>
      <HomePage />
      </v-main>
      </v-app>
</template>

<script>
    import BarLayout from '@/layouts/BarLayout.vue'
    import HomePage from '@/components/HomePage.vue'
    export default {
    name: 'HomeView',
    components:{ BarLayout, HomePage},
    computed: {
    auth () {
      var auth
      if (localStorage.auth_token) {
        auth = true
      }
      return auth
    }},
    methods: {
    goLogout () {
      localStorage.clear()
      this.$router.push({ name: 'Login' })
    },
    Books () {
      this.$router.push({ name: 'Books' })
    },
    LK () {
      this.$router.push({ name: 'Reader' })
    },
}
    }
</script> 