<template>
  <v-spacer></v-spacer>
  <v-btn v-if="!auth" @click="goLogin()"
         text
  >
    <span class="mr-2">Регистрация</span>
  </v-btn>

</template>

<script>
export default {
  name: 'LoginNavigationBar',
  methods: {
    goLogin() {
      this.$router.push({name: 'Registration'})
    },
  }
}

</script>

<style>
</style>
