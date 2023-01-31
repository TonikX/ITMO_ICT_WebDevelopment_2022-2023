<template>
  <div class="test-3">
    <h2>Personal information</h2>
    <h3>Welcome, {{ login() }} </h3>
    <v-card>
      <v-card-text class="test-3">
        <a @click.prevent="goRegister" style="text-decoration: none; color: #198754">Register dog</a> <br>
        <a @click.prevent="goEdit" style="text-decoration: none; color: #198754">Edit profile</a> <br>
        <a @click.prevent="goHome" style="text-decoration: none; color: #198754">Go to Main</a>
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
      this.$router.push({name: 'registerdog'})
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
  
  .test-3 {
  width: 100%;
  height: auto;
  margin: 0 auto;
  padding: 20px 0;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: dodgerblue;
}


.text, .text-1 {
  width: 50%;
  cursor: pointer;
  margin: 0 auto;
  text-align: center;
  
}
</style>