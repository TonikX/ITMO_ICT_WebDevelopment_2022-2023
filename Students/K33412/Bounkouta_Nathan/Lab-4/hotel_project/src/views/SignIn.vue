<template>
  <div class="signin">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/")' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Войти</h2>
    <br>
    <v-form
        @submit.prevent="logIn"
        ref="form"
        class="my-2"
        id="check-login-form"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
              label="Никнейм"
              v-model="username"
          />

          <v-text-field
              label="Пароль"
              v-model="password"
              type="password"
          />

          <v-btn type="submit" color="primary">Войти</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: () => ({
    password: null,
    username: null
  }),
  methods: {
    logIn () {
      try {
        this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', {
            password: this.password,
            username: this.username
          }).then(response => {
            this.setLogIn(response)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    setLogIn (response) {
      console.log(this.password)
      console.log(this.username)
      localStorage.setItem('token', response.data.auth_token)
      this.$bus.$emit('logged', 'User logged')
      this.$router.push('/main/')
    }
  }
}
</script>