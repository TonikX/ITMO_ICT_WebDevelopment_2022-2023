<template>
  <v-btn v-if="auth" @click="LK()" text> Личный кабинет </v-btn>
  <v-btn v-if="auth" @click="Home()" text>
    <span class="mr-2">Домашняя страница</span>
  </v-btn>

  
  <v-spacer></v-spacer>
  <v-btn v-if="auth" @click="Logout()" text>
    <span class="mr-2">Выйти</span>
  </v-btn>
</template>

<script>
export default {
  name: "AllBooks",
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
      this.$router.push({ name: "Login" });
    },
    Home() {
      this.$router.push({ name: "Home" });
    },
    LK() {
      this.$router.push({ name: "Reader" });
    },
  },
};
</script>
