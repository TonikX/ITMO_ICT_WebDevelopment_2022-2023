<template>
  <main>
    <h1>Библиотека</h1>
    <button @click="goLogin">Вход</button>
  </main>
</template>

<script>
export default {
  name: "Home",
  methods: {
    goLogin() {
      this.$router.push({name: "login"})
    }
  }
}
</script>

