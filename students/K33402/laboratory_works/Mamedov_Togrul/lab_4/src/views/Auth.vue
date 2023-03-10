<template>
  <div class="container">
    <h1 class="mt-5">Login</h1>
    <div v-if="isLoggedIn">You're already logged in!</div>
    <div v-else>
      <form class="mt-4" @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label" for="username">Username:</label>
          <input id="username" v-model="username" class="form-control" required type="text">
        </div>
        <div class="mb-3">
          <label class="form-label" for="password">Password:</label>
          <input id="password" v-model="password" class="form-control" required type="password">
        </div>
        <button class="btn btn-primary" type="submit">Login</button>
      </form>
  </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  computed: {
    isLoggedIn() {
      return localStorage.getItem('accessToken');
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8001/jwt/create/', {
              username: this.username,
              password: this.password,
            },
            {
              headers: {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': 'qLPcRBcn40VgMGedRMMMybZTJCicmmuv4wvbh3o60LBo4uhSiirKpoPYY1KAlNpQ'
              }
            });
        const accessToken = response.data.access;
        localStorage.setItem('accessToken', accessToken);
        location.reload(); // Reload the page
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>
