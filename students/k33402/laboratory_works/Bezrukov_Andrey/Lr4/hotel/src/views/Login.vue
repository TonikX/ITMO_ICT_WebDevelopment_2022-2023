<template>
  <v-main class="d-flex align-center text-center">
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar color="teal" dark>
              <v-toolbar-title>Login form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field required v-model="username" name="login" label="Login" type="text"></v-text-field>
                <v-text-field
                  required
                  v-model="password"
                  name="password"
                  label="Password"
                  type="password"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="teal" dark to="/signup">Sign Up</v-btn>
              <v-btn color="teal" dark @click="submit">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: 'Login',

  data: () => ({
    username: null,
    password: null
  }),

  methods: {
    submit () {
      const body = {
        username: this.username,
        password: this.password
      }

      this.axios.post(this.$hostname + 'auth/token/login/', body).then((response) => {
        if (response.status === 200) {
          localStorage.setItem('auth_token', response.data.auth_token)
          this.$router.push({ name: 'Rooms' })
        } else {
          if (response.status === 400) {
            alert('Wrong username or password')
          } else {
            alert('Unknown error')
          }
        }
      })
    }
  }
}
</script>
