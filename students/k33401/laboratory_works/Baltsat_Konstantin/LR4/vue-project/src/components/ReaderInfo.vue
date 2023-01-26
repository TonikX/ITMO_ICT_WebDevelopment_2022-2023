<template>
  <v-btn v-if="auth" @click="Home()" text>
    <span class="mr-2">Домашняя страница</span>
  </v-btn>
  
  <v-btn v-if="auth" @click="Books()" text>
    <span class="mr-2">Книги</span>
  </v-btn>
  <v-spacer></v-spacer>
  <v-btn v-if="auth" @click="Logout()" text>
    <span class="mr-2">Выйти</span>
  </v-btn>
</template>

<script>
export default {
  name: "ReaderInfo",
  computed: {
    auth() {
      var auth;
      if (localStorage.auth_token) {
        auth = true;
      }
      return auth;
    },
  },
  methods: {
    Logout() {
      localStorage.clear();
      this.$router.push({ name: "Login" });
    },
    Home() {
      this.$router.push({ name: "Home" });
    },
    Books() {
      this.$router.push({ name: "Books" });
    },
  },
};
</script>
