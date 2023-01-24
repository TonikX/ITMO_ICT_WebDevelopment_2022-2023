<template>
<!--  <button @click="check" class="col my-4">Check</button>-->
<!--  <div v-if="!isLogin" class="container ps-0">-->
<!--    <button @click="login" class="col me-2">Login</button>-->
<!--    <button @click="register" class="col">Register</button>-->
<!--  </div>-->
<!--  <div v-else class="container ps-0">-->
<!--    <button @click="goToMainPage" class="col me-2">Main page</button>-->
<!--    <button @click="getRegs" class="col me-2">Registrations</button>-->
<!--    <button @click="getComs" class="col me-5">Comments</button>-->
<!--    <button @click="goToAcc" class="col ms-5 me-2">My profile</button>-->
<!--    <button @click="logout" class="col me-2">Logout</button>-->
<!--    <input v-model="password" class="col" type="password" placeholder="password">-->
<!--    <button @click="updateToken" class="col">Update connection</button>-->
<!--  </div>-->

  <nav class="navbar navbar-expand-lg bg-body-tertiary nav-background">
    <div class="container">
      <a class="navbar-brand nav-text">Mountains</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link nav-text" aria-current="page" @click="goToMainPage">Home</a>
          </li>
          <li v-if="isLogin" class="nav-item">
            <a class="nav-link nav-text" @click="getRegs">Registrations</a>
          </li>
          <li v-if="isLogin" class="nav-item">
            <a class="nav-link nav-text" @click="getComs">Comments</a>
          </li>
        </ul>
        <ul v-if="isLogin" class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link nav-text" aria-current="page" @click="goToAcc">Profile</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-text" @click="logout">Logout</a>
          </li>
        </ul>
        <ul v-else class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link nav-text" aria-current="page" @click="login">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-text" @click="register">Register</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useUserStore from "@/stores/user";

export default {
  name: "NavBar",

  data() {
    return {
      isLogin: localStorage.getItem('idUser'),
      password: ""
    }
  },

  computed: {
    ...mapState(useUserStore, ['tokens', 'users'])
  },

  methods: {
    ...mapActions(useUserStore, ['loadUserToken', 'loadUsers']),

    goToMainPage() {
      this.$router.push({name: "hotels"})
    },

    goToAcc() {
      this.$router.push({name: "profile"})
    },

    check() {
      console.log(localStorage)
    },

    logout() {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('idBookRoom')
      localStorage.removeItem('idUser')
      localStorage.removeItem('username')
      localStorage.removeItem('pinia_hotels')
      localStorage.removeItem('pinia_regCom')
      localStorage.removeItem('pinia_user')
      localStorage.removeItem('isStaff')

      this.isLogin = 0
      this.$router.push({name: "hotels"})
    },

    async updateToken() {
      const username = localStorage.getItem('username')
      await this.loadUserToken(username, this.password)
      const accessToken = this.tokens.access
      localStorage.setItem('accessToken', accessToken)
    },

    login() {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('idBookRoom')
      localStorage.removeItem('idUser')
      localStorage.removeItem('username')
      localStorage.removeItem('pinia_hotels')
      localStorage.removeItem('pinia_regCom')
      localStorage.removeItem('pinia_user')
      localStorage.removeItem('isStaff')

      this.isLogin = 0
      this.$router.push({name: "login"})
    },

    register() {
      this.$router.push({name: "login"})
    },

    getRegs() {
      this.$router.push({name: "registrations"})
    },

    getComs() {
      this.$router.push({name: "comments"})
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
}

.nav-text {
  color: black !important;
}

.nav-background {
  background: linear-gradient(#dab88b, #dab88b);
}
</style>