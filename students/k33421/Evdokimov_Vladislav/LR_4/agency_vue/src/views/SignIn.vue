<template>
  <div class="signin">
    <v-form
      @submit.prevent="signIn"
      ref="signInForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите имя пользователя"
            v-model="signInForm.username"
          />
          <v-text-field
            label="Введите пароль"
            v-model="signInForm.password"
            type="password"
          />
          <v-btn type="submit" color="primary" dark>Войти</v-btn>

          <p class="mt-5">Ещё нет аккаунта? <router-link to="/signup">Зарегистрироваться</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignIn',

  data: () => ({
    signInForm: {
      username: '',
      password: ''
    }
  }),

  methods: {
    async signIn () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/token/login/', this.signInForm)
        console.log('SIGN IN RESPONSE', response)
        this.$refs.signInForm.reset()
        localStorage.setItem('token', response.data.auth_token)
        window.location = '/'
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
