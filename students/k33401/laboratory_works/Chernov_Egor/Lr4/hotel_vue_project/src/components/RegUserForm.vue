<template>
  <div class="row p-0 text-center">
    <h1 class="text-center my-4">Registration</h1>
    <input class="my-2 text-center" v-model="email" type="text" placeholder="E-mail" />
    <input class="my-2 text-center" v-model="username" type="text" placeholder="Username" />
    <input class="my-2 text-center" v-model="password" type="password" placeholder="Password" />
    <a class="nav-link py-1 px-2 fs-5" @click="regUser">Create</a>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useUserStore from "@/stores/user";

export default {
  name: "RegUserForm",

  data() {
    return {
      email: "",
      username: "",
      password: ""
    }
  },

  computed: {
    ...mapState(useUserStore, ['tokens', 'users', 'accUser'])
  },

  methods: {
    ...mapActions(useUserStore, ['loadUserToken', 'loadUsers', 'loadAccUser', 'createUser']),

    async regUser() {
      await this.createUser(this.username, this.email, this.password)
      await this.loadUserToken(this.username, this.password)
      const accessToken = this.tokens.access
      await this.loadUsers(accessToken)
      let idUser = ""
      let username = ""
      for (const user of this.users) {
        if (user.username === this.username) {
          idUser = user.id
          username = user.username
        }
      }

      await this.loadAccUser(accessToken, idUser)
      let isStaff = this.accUser.is_staff

      if (idUser === "null" || idUser === "") {
        alert('Try again.')
        return
      }
      localStorage.setItem('idUser', idUser)
      localStorage.setItem('username', username)
      localStorage.setItem('isStaff', isStaff)
      localStorage.setItem('accessToken', accessToken)

      if (localStorage.getItem('idBookRoom')) {
        this.$router.push({name: "booking"})
      } else {
        this.$router.push({name: "hotels"})
      }
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
  background-color: #E0E7E9;
  border-radius: 8px 8px 8px 8px;
  color: black;
}

input {
  background-color: rgba(253, 246, 236, 0.4);
  border-radius: 8px 8px 8px 8px;
  color: black;
}
</style>