<template>
  <form @submit.prevent="Login" ref="LoginForm">
    <div style="font-size: 20px; color: royalblue">
      <div class="t"><strong>Логин: </strong>
        <input
            v-model="LoginForm.username"
            class="input"
            type="text"
            placeholder="Логин"/>
      </div>
    </div>
    <div style="font-size: 20px; color: royalblue">
      <div class="t"><strong>Пароль: </strong>
        <input
            v-model="LoginForm.password"
            class="input"
            type="text"
            placeholder="Пароль"/>
      </div>
    </div>
    <button class="btn" type="submit">Войти</button>
  </form>
    <p class="mt-15">Ещё нет аккаунта?<br>
      <router-link to="/registration/">Зарегистрироваться</router-link></p>
  </div>
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

