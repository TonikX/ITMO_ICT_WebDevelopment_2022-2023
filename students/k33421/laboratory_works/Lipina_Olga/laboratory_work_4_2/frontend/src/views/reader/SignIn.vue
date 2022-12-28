<template>
  <div class="signIn">
    <h2>Авторизация</h2>
    <v-form
      @submit.prevent="signIn"
      ref="signInForm"
      class="my-2">
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Логин"
            v-model="signInForm.username"/>
          <v-text-field
            label="Пароль"
            v-model="signInForm.password"
            type="password"/>
          <v-btn type="submit" color="primary" dark>Войти</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15">Ещё нет аккаунта?<br>
      <router-link to="/library/signup">Зарегистрироваться</router-link></p>
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
        const response = await this.axios.post('http://127.0.0.1:8000/auth/token/login', this.signInForm)
        this.$refs.signInForm.reset()
        localStorage.setItem('auth_token', response.data.auth_token)
        await this.$router.push({ name: 'home' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert('Неверный логин или пароль.')
        } else if (e.response.data.password || e.response.data.username) {
          alert('Поля "логин" и "пароль" должны быть заполнены.')
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
