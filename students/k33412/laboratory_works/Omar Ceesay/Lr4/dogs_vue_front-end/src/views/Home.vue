<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="containers-2" >
     
      <v-card-title class="test-1">
        <h2>Welcome to  the dog showcase show</h2>
        </v-card-title>  
      <v-card-text class="test-1">
        <dev class="">
          <v-card-subtitle><h3>This is the best annual dog show in the city. This year 2023 is speacial.</h3></v-card-subtitle>
          
          <template  v-if="this.authorized">
            <a @click="goProfile" style="text-decoration: none; color: #198754">Personal information</a><br>
            <a href="/experts" style="text-decoration: none; color: #198754">Experts</a><br>
            <a href="/participants" style="text-decoration: none; color: #198754">Paticipants</a> <br>
            <a @click="goLogOut" style="text-decoration: none; color: #198754">Logout</a><br>
          </template>

          <template v-else >
            <a class="singinn" @click="goLogIn" style="text-decoration: none; color: #198754">login</a><br>
            <router-link to="/signup" style="text-decoration: none; color: #198754" class="register">Register</router-link>
          </template>
        </dev>
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
 // for Authorization function
 created() {
  if (sessionStorage.getItem('auth_token')) {
    if (sessionStorage.getItem('auth_token') !== '-1') {
      this.authorized = true;
      console.log('Authorized user: ' + sessionStorage.getItem('username'));
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

    goLogIn () {
      this.$router.push({ name: 'login' })
    }

  }
}
</script>
<style>
  
  .test-1 {
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

h3{
  margin-bottom: 10px;
  font-weight: bold;
  color: #444;
}

.signinn, .register {
  width: 50%;
  cursor: pointer;
  margin: 0 auto;
  text-align: center;
  
}
</style>
