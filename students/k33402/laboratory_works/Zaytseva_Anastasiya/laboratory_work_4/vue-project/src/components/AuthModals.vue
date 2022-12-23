<script>
import { mapActions } from 'pinia';
import useUsersStore from '@/stores/users'

export default {
  name: 'AuthModal',
  data() {
    return {
      loginEmail: '',
      loginPassword: '',
      loginError: '',

      regEmail: '',
      regPassword: '',
      regError: '',
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['login', 'signUp']),
    async onLoginSubmit() {
      this.loginError = ''

      if (!this.loginEmail || !this.loginPassword) {
        this.loginError = 'Ошибка! Введите email и пароль.'
        return
      }

      try {
        await this.login({
          username: this.loginEmail,
          password: this.loginPassword
        })
      } catch (e) {
        this.loginError = 'Ошибка! Неверно указан email или пароль.'
        return
      }

      this.$refs.closeLoginModal.dispatchEvent(new Event('click'))
      this.$router.push('/profile')
    },
    async onRegSubmit() {
      this.regError = ''

      if (!this.regEmail || !this.regPassword) {
        this.regError = 'Ошибка! Введите email и пароль.'
        return
      }

      let result
      try {
        result = await this.signUp({
          username: this.regEmail,
          email: this.regEmail,
          password: this.regPassword
        })
      } catch (e) {
        this.regError = 'Ошибка! Неверно указан email или пароль.'
        return
      }

      if (result?.status === 201) {
        this.$refs.closeRegModal.dispatchEvent(new Event('click'))

        await this.login({
          username: this.regEmail,
          password: this.regPassword
        })

        this.$router.push('/profile')
      }
    }
  }
}
</script>

<template>
<div>
<div class="modal fade" id="auth" tabindex="-1" aria-labelledby="authModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="authModalLabel">Вход</h1>
        <button ref="closeLoginModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body p-5">
        <form>
          <img class="img-fluid mb-4" src="/img/logo.png" alt="Fabiana Filippi">
          <div class="form-floating mb-3">
            <input
              v-model="loginEmail"
              type="email"
              class="form-control"
              name="login_email"
              id="floatingInput"
              placeholder="name@example.com"
            >
            <label for="floatingInput">Email</label>
          </div>
          <div class="form-floating mb-3">
            <input
              v-model="loginPassword"
              type="password"
              class="form-control"
              name="login_password"
              id="floatingPassword"
              placeholder="Password"
            >
            <label for="floatingPassword">Пароль</label>
          </div>
          <p
            v-if="loginError"
            class="login-error text-danger"
          >
            <strong>{{ loginError }}</strong>
          </p>
          <button
            class="login-button w-100 btn btn-lg btn-dark mb-3"
            type="button"
            @click="onLoginSubmit"
          >Войти</button>
          <button class="w-100 btn btn-lg btn-outline-dark" type="button" data-bs-target="#regModal" data-bs-toggle="modal">Регистрация</button>
        </form>
      </div>
    </div>
  </div>
</div>
<div class="modal fade" id="regModal" tabindex="-1" aria-labelledby="regModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="regModalLabel">Регистрация</h1>
        <button ref="closeRegModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body p-5">
        <form class="signup-form" action="http://localhost:3000/users" method="POST">
          <img class="img-fluid mb-4" src="/img/logo.png" alt="Fabiana Filippi">
          <div class="form-floating mb-3">
            <input
              v-model="regEmail"
              type="email"
              name="email"
              class="form-control"
              id="floatingInputSignup"
              placeholder="name@example.com"
            >
            <label for="floatingInputSignup">Email</label>
          </div>
          <div class="form-floating mb-3">
            <input
              v-model="regPassword"
              type="password"
              name="password"
              class="form-control"
              id="floatingPasswordSignup"
              placeholder="Password"
            >
            <label for="floatingPasswordSignup">Пароль</label>
          </div>
          <p
            v-if="regError"
            class="login-error text-danger"
          >
            <strong>{{ regError }}</strong>
          </p>
          <button
            class="signup-button w-100 btn btn-lg btn-dark mb-2"
            type="button"
            @click="onRegSubmit"
          >Зарегистрироваться</button>
        </form>
      </div>
    </div>
  </div>
</div>
</div>
</template>
