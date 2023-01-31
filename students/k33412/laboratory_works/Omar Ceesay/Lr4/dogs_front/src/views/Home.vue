<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Welcome to  the dog showcase show</h2>
      </v-card-title>  
      <v-card-text class="test">
        <h2>
          <a href="/experts" style="text-decoration: none; color: #198754">Experts</a><br>
          <a href="/participants" style="text-decoration: none; color: #198754">Paticipants</a> <br>
          <template  v-if="this.authorized">
            <a @click="goProfile" style="text-decoration: none; color: #198754">Personal carbinet</a><br>
            <a @click="goLogOut" style="text-decoration: none; color: #198754">Logout</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn" style="text-decoration: none; color: #198754">login</a><br>
            <router-link to="/show/signup" style="text-decoration: none; color: #198754">Register</router-link>
          </template>
        </h2>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src
/* eslint-disable */

export default {
  name: 'Home',

  data: () => ({
    authorized: false
  }),

  created () {
    console.log('hehe' + ' ' + sessionStorage.getItem('auth_token'))
    console.log('hehe' + ' ' + sessionStorage.getItem('username'))
    if (sessionStorage.getItem('auth_token')) {
      if (sessionStorage.getItem('auth_token') !== '-1') {
        this.authorized = true
      }
    }
  },

  methods: {

    goProfile () {
      this.$router.push({ name: 'profile' })
    },

    goLogOut () {
      this.$router.push({ name: 'logout' })
    },

    goSignIn () {
      this.$router.push({ name: 'signin' })
    }
  }
}
</script>

