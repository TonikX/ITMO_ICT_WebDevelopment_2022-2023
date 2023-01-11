<template>
  <v-layout column justify-center align-center>
    <v-form
    >
      <v-text-field
        v-model="username"
        label="Username"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Password"
        type="Password"
        required
      ></v-text-field>

      <v-btn
        color="success"
        @click="submit"
      >
        Login
      </v-btn>
    </v-form>
  </v-layout>
</template>

<script>
export default {
  name: 'Login',
  data: () => ({
    username: '',
    password: ''
  }),
  methods: {
    async submit () {
      const body = {
        username: this.username,
        password: this.password
      }
      const response = await this.axios.post(this.$hostname + 'auth/token/login/', body)
      if (response.status === 200) {
        localStorage.setItem('auth_token', response.data.auth_token)
        this.$router.push({ name: 'Home' })
      } else {
        if (response.status === 400) {
          alert('Wrong username or password')
        } else {
          alert('Unknown error')
        }
      }
    }
  }
}
</script>

<style scoped>
</style>
