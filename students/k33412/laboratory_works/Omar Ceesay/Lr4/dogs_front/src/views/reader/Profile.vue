<template>
  <div class="edit">
    <h2>Personal carbinet</h2>
    <h3>Welcome, {{ login() }} </h3>
    <v-card>
      <v-card-text display: block style="margin-top:1cm">
        <a @click.prevent="goRegister" style="text-decoration: none; color: #ff6347">Register dog</a> <br>
        <a @click.prevent="goEdit" style="text-decoration: none; color: #ff6347">Edit profile</a> <br>
        <a @click.prevent="goHome" style="text-decoration: none; color: #ff6347">Go to Main</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
import $ from "jquery";

export default {
  name: 'Profile',
  data() {
    return {
      userme: Object,
      first_name: '',
      last_name: '',
      telephone: '',
    }
  },
  created() {
    this.loadReaderData()
  },

  methods: {

    async loadReaderData() {
      const response = await this.axios
          .get('http://127.0.0.1:8000/auth/users/me/', {
            headers: {
              Authorization: `Token ${sessionStorage.getItem('auth_token')}`
            }
          })
      this.first_name = response.data.first_name
      this.last_name = response.data.last_name
      this.telephone = response.data.telephone
    },

    goHome() {
      this.$router.push({name: 'home'})
    },

    goRegister() {
      this.$router.push({name: 'regdog'})
    },

    goEdit() {
      this.$router.push({name: 'profile_edit'})
    },

    login() {
      return (sessionStorage.getItem('username'))
    }
  }
}
</script>

<style>

</style>