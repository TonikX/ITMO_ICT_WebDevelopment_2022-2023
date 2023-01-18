<template>
  <button @click="check" class="col ms-0 mb-4">Check</button>
  <div v-if="!isLogin" class="container ps-0">
    <button @click="login" class="col me-2">Login</button>
    <button @click="register" class="col">Register</button>
  </div>
  <div v-else class="container ps-0">
    <button @click="goToMainPage" class="col me-2">Main page</button>
    <button @click="getRegs" class="col me-2">Registrations</button>
    <button @click="getComs" class="col me-5">Comments</button>
    <button @click="goToAcc" class="col ms-5 me-2">My profile</button>
    <button @click="logout" class="col me-2">Logout</button>
    <input v-model="password" class="col" type="password" placeholder="password" >
    <button @click="updateToken" class="col">Update connection</button>
  </div>
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

      this.isLogin = 0
      this.$router.push({name: "hotels"})
    },

    updateToken() {
      const username = localStorage.getItem('username')
      this.loadUserToken(username, this.password)
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

</style>