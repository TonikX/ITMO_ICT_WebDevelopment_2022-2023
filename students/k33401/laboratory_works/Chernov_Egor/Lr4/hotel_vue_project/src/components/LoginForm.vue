<template>
  <div class="container">
    <h1 class="row">Login</h1>
    <input class="row my-2" v-model="username" type="text" placeholder="E-mail" />
    <input class="row my-2" v-model="password" type="password" placeholder="Password" />
    <button class="row my-2" @click="login">Login</button>
    <p class="row my-2" v-if="isValid">Write username and password!</p>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useUserStore from "@/stores/user";

export default {
  name: "LoginForm",

  data() {
    return {
      username: "",
      password: "",
      isValid: false
    }
  },

  computed: {
    ...mapState(useUserStore, ['tokens', 'users'])
  },

  methods: {
    ...mapActions(useUserStore, ['loadUserToken', 'loadUsers']),
    login() {
      if (this.username && this.password) {
        this.isValid = false

        this.loadUserToken(this.username, this.password)
        const accessToken = this.tokens.access
        this.loadUsers(accessToken)
        let idUser = ""
        let username = ""
        for (const user of this.users) {
          if (user.username === this.username) {
            idUser = user.id
            username = user.username
          }
        }
        if (idUser === "null" || idUser === "") {
          alert('Try again.')
          return
        }
        localStorage.setItem('idUser', idUser)
        localStorage.setItem('username', username)
        localStorage.setItem('accessToken', accessToken)

        if (localStorage.getItem('idBookRoom')) {
          this.$router.push({name: "booking"})
        } else {
          this.$router.push({name: "hotels"})
        }
      } else {
        this.isValid = true
      }
    }
  }
}
</script>

<style scoped>

</style>