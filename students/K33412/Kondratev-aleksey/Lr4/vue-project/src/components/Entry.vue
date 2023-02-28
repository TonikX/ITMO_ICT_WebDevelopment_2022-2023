<template>
  <main class="container-xl p-5 mb-5">
    <form class="d-flex-column" @submit.prevent="login">
      <h1 class="row mb-5 justify-content-center">Вход</h1>
      <div class="row mb-3 justify-content-center">
        <label for="email" class="col-sm-1 col-form-label">Почта</label>
        <div class="col-sm-3 col-md-4">
          <input type="text" class="form-control" v-model="form.email" name="email" id="email">
        </div>
      </div>
      <div class="row mb-3 justify-content-center">
        <label for="password" class="col-sm-1 col-form-label">Пароль</label>
        <div class="col-sm-3 col-md-4">
          <input type="password" class="form-control" v-model="form.password" name="password" id="password">
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-sm-4 col-md-5">
          <button type="submit" class="btn btn-primary" :to="{ path: '/' }">Войти</button>
          <a class="btn btn-primary" href="./reqistration.html" role="button">Зарегистрироваться</a>
        </div>
      </div>
    </form>
  </main>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import router from '@/router'

import useLoginStore from '../stores/login'

export default {
  name: 'EntryBlock',

  data() {
    return {
      form: {
        email: "",
        password: ""
      }
    };
  },

  methods: {
    ...mapActions(useLoginStore, ['userLogin']),

    async login() {
      const response = await this.userLogin(this.form);

      const { accessToken, user } = response.data

      localStorage.accessToken = accessToken
      localStorage.user = JSON.stringify(user)

      localStorage.accessToken ? router.push('/') : router.push('')
    }
  }
}
</script>
