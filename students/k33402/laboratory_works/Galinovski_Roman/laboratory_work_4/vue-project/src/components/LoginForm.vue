<template>
    <form @submit.prevent="Login" ref="LoginForm">
      <div style="font-size: 20px; color: royalblue">
        <div class="t"><strong>Log in: </strong>
          <input
              v-model="LoginForm.username"
              class="input"
              type="text"
              placeholder="Log in"/>
        </div>
      </div>
      <div style="font-size: 20px; color: royalblue">
        <div class="t"><strong>Password: </strong>
          <input
              v-model="LoginForm.password"
              class="input"
              type="text"
              placeholder="Password"/>
        </div>
      </div>
      <button class="btn" type="submit">Log in</button>
    </form>
      <p class="mt-15">No account yet?<br>
        <router-link to="/registration/">Sign in</router-link></p>
  </template>
  
  <script>
  export default {
    name: 'Login',
    data: () => ({
      LoginForm: {
        username: '',
        password: ''
      }
    }),
    methods: {
      async Login () {
        try {
          const response = await this.axios.post('http://127.0.0.1:8000/auth/token/login', this.LoginForm)
          this.$refs.LoginForm.reset()
          localStorage.setItem('auth_token', response.data.auth_token)
          await this.$router.push({ name: 'home' })
        } catch (e) {
          if (e.response.data.non_field_errors) {
            alert('Invalid Login or Password.')
          } else if (e.response.data.password || e.response.data.username) {
            alert('Space of "Login" and space of "password" must be filled.')
          } else {
            console.error('API error:', e.message)
          }
        }
      }
    }
  }
  </script>
  
  <style>
  </style>