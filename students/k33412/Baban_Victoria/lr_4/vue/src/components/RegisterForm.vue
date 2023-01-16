<template>
  <main>
    <div class="container col-md-6 p-5">
      <form @submit.prevent="register">
        <div class="mb-3">
          <label for="first_name" class="form-label">Имя:</label>
          <input type="text" class="form-control" id="first_name" name="first_name" v-model="first_name">
        </div>
        <div class="mb-3">
          <label for="last_name" class="form-label">Фамилия:</label>
          <input type="text" class="form-control" id="last_name" name="last_name" v-model="last_name">
        </div>
        <!--
        <div class="mb-3">
          <label for="username" class="form-label">Придумайте никнейм:</label>
          <input type="text" class="form-control" id="username" name="username" v-model="form.username">
        </div>
        -->
        <div class="mb-3">
          <label for="email" class="form-label">Введите свой e-mail:</label>
          <input type="email" class="form-control" id="email" name="email" v-model="email">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Придумайте пароль:</label>
          <input type="password" class="form-control" id="password" name="password" v-model="password">
        </div>
        <p v-if="error" class="error text-danger">
          <strong>{{ error }}</strong>
        </p>
        <div class="p-4 d-flex justify-content-center">
          <button type="button" class="btn btn-success mb-3" @click="reg">Зарегистрироваться</button>
        </div>
      </form>
      <div class="container d-flex">
        <p class="text-black">Уже есть аккаунт?</p>
        <a href="#" class="ms-2 text-success" @click="$router.push('/login/')">Войти</a>
      </div>
    </div>
  </main>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import router from '@/router'

import useUserStore from '@/stores/user'
export default {
  name: 'RegisterForm',

  data() {
    return {

      first_name: "",
      last_name: "",
      email: "",
      username: "",
      password: "",

      error: ""
    };
  },

  methods: {
    ...mapActions(useUserStore, ['register', 'login']),

    async reg() {
      this.error = ''
      if (!this.email || !this.password) {
        this.error =  'Ошибка! Введите email и пароль.'
        return
      }
      let result
      try {
        result = await this.register({
          last_name: this.last_name,
          first_name: this.first_name,
          username: this.email,
          email: this.email,
          password: this.password
        })
      } catch (e) {
        this.error =  'Ошибка! Неверно указан email или пароль.'
        return
      }
      if (result?.status === 201) {
        await this.login({
          username: this.email,
          password: this.password
        })
        this.$router.push('/lk')
      }
    }
  }

}
</script>
