<template>
  <v-btn v-if="auth" @click="go_to_home()"
         text
  >
    <span class="mr-2">Домашняя страница</span>
  </v-btn>

  <v-btn v-if="auth" @click="go_to_all_books()"
         text
  >
    <span class="mr-2">Книги</span>
  </v-btn>

  <v-spacer></v-spacer>

  <v-btn v-if="auth" @click="go_to_reader_info()"
         text
  >
    <span class="mr-2">Личный кабинет</span>
  </v-btn>

  <v-btn v-if="auth" @click="logout()"
         text
  >
    <span class="mr-2">Выйти</span>
  </v-btn>
</template>

<script>
export default {
  name: 'DefaultNavigationBar',
  computed: {
    auth() {
      var auth
      if (localStorage.auth_token) {
        auth = true
      }
      return auth
    }
  },
  methods: {
    logout() {
      localStorage.clear()
      this.$router.push({name: 'Login'})
    },
    go_to_home() {
      this.$router.push({name: 'Home'})
    },
    go_to_all_books() {
      this.$router.push({name: 'Books'})
    },
    go_to_reader_info() {
      this.$router.push({name: 'Reader'})
    }
  }
}
</script>
