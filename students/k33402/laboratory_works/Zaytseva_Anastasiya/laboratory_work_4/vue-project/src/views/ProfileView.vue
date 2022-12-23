<script>
import { mapState, mapActions } from 'pinia'
import useUsersStore from '@/stores/users'

export default {
  name: 'ProfileView',
  computed: {
    ...mapState(useUsersStore, ['user', 'token']),
  },
  mounted() {
    this.fetchCurrentUser().then(result => {
      if (!result?.email) {
        this.$router.replace({ path:'/' })
      }
    })
  },
  methods: {
    ...mapActions(useUsersStore, ['fetchCurrentUser', 'logout']),
    async onLogout() {
      await this.logout()
      this.$router.push('/')
    }
  }
}
</script>

<template>
<main class="container">
  <nav class="mt-4" aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><RouterLink to="/" class="link-dark">Главная</RouterLink></li>
      <li class="breadcrumb-item active" aria-current="page">Личный кабинет</li>
    </ol>
  </nav>
  <div v-if="user.email" class="row mt-4">
    <div class="col-4">
      <ul class="list-group">
        <li class="list-group-item">ID: {{ user.id }}</li>
        <li class="list-group-item">Email: {{ user.email }}</li>
        <li class="list-group-item">Username: {{ user.username }}</li>
        <li class="list-group-item">Token: {{ token }}</li>
      </ul>
    </div>
    <div class="col">
      <button
        class="btn btn-danger btn-lg"
        @click="onLogout"
      >Выйти</button>
    </div>
  </div>
</main>
</template>

<style scoped>
main.container {
  min-height: 60vh;
}
</style>
