<template>
  <main>
    <div class="container col-md-6 p-5">
      <form>
        <div class="mb-3">
          <label for="email" class="form-label">Введите свой e-mail:</label>
          <input type="email" class="form-control" id="email" name="email" v-model="email">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Введите пароль:</label>
          <input type="password" class="form-control" id="password" name="password" v-model="password">
        </div>
        <p v-if="error" class="error text-danger">
          <strong>{{ error }}</strong>
        </p>
        <div class="p-4 d-flex justify-content-center">
          <button type="button" class="btn btn-success mb-3" @click="logIn">Войти</button>
        </div>
      </form>
      <div class="container d-flex">
        <p class="text-black">Еще нет аккаунта?</p>
        <a href="#" class="ms-2 text-success" @click="$router.push('/registration/')">Зарегистрируйся</a>
      </div>
    </div>
  </main>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import router from '@/router'
import useUserStore from '@/stores/user'

export default {
  name: "LogIn",

  data(){
    return {
      email : "",
      password : "",

      error: ""
    }
  },

  methods: {
    ...mapActions(useUserStore, ['login']),

    async logIn() {
      if (!this.email || !this.password) {
        this.error = 'Ошибка! Введите email и пароль.'
        return
      }
      try {
        await this.login({
          username: this.email,
          password: this.password
        })
      } catch (e) {
        this.error = 'Ошибка! Неверно указан email или пароль.'
        return
      }
      this.$router.push('/lk')
    },
  }

}
</script>
