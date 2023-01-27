
<template>
  <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #20c997;">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="./icons/logo.PNG" alt="Лого" width="30" height="24" class="d-inline-block align-text-top">
        EventMap
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-link active" aria-current="page" href="#" @click="$router.push('/')">Поиск мероприятий</a>
        </div>
      </div>
      <form v-if="!token" class="justify-content-end">
        <a  class="btn btn-light me-2" href="#" role="button" id="enter" @click="$router.push('/login/')">Вход</a>
        <a class="btn btn-sm btn-outline-light" role="button" id="registr" href="#" @click="$router.push('/registration/')">Регистрация</a>
      </form>
      <form v-else class="justify-content-end">
        <a class="btn btn-light me-2" href="#" role="button" id="enterlk" @click="$router.push('/lk/')">Личный кабинет</a>
        <a class="btn btn-sm btn-outline-light" href="#" role="button" id="logout" @click="Logout">Выход</a>
      </form>
    </div>
  </nav>
</template>

<script>
import { mapState, mapActions } from 'pinia';
import useUserStore from '@/stores/user'

export default {
  name: 'Header',
  computed: {
    ...mapState(useUserStore, ['token'])
  },
  mounted() {
    this.setToken(window.localStorage.getItem('token'))
  },
  methods: {
    ...mapActions(useUserStore, ['setToken', 'logout']),
    async Logout() {
      await this.logout()
      this.$router.push('/')
    }
  }
}
</script>

