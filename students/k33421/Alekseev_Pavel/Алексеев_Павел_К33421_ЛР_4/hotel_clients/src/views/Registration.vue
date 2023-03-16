<template>
  <v-layout column justify-center align-center>
    <v-form v-model="valid"
    >
      <v-text-field
        v-model="username"
        label="Username"
        :rules="[v => !!v || 'Username is required']"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Password"
        type="Password"
        :rules="[v => !!v || 'Password is required']"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        label="Email"
        type="email"
        :rules="emailRules"
        required
      ></v-text-field>

      <v-btn
        color="blue"
        @click="submit"
        :disabled="!valid"
      >
        Login
      </v-btn>
    </v-form>
  </v-layout>
</template>

<script>
export default {
  name: 'Registration',
  data: () => ({
    username: '',
    password: '',
    email: '',
    emailRules: [
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
    ]
  }),
  methods: {
    async submit () {
      const body = {
        valid: false,
        username: this.username,
        password: this.password,
        email: this.email
      }
      const response = await this.axios.post(this.$hostname + 'auth/users/', body)
      if (response.status === 201) {
        this.$router.push({ name: 'Login' })
      } else {
        alert('Something went wrong')
      }
    }
  }
}
</script>

<style scoped>
</style>
