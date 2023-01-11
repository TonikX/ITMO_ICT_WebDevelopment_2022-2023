<template>
	<main class="container-xl p-5">
		<form class="d-flex-column" @submit.prevent="register">
			<h1 class="row mb-5 justify-content-center">Регистрация</h1>
			<div class="row mb-3 justify-content-center">
				<label for="inputName3" class="col-sm-1 col-form-label">Имя</label>
				<div class="col-sm-3">
					<input type="text" class="form-control" v-model="form.firstname" name="firstname" id="inputName3" placeholder="Алексей" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputSurname3" class="col-sm-1 col-form-label">Фамилия</label>
				<div class="col-sm-3">
					<input type="text" class="form-control" v-model="form.lastname" name="lastname" id="inputSurname3" placeholder="Кондратьев" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputEmail3" class="col-sm-1 col-form-label">Почта</label>
				<div class="col-sm-3">
					<input type="email" class="form-control" v-model="form.email" name="email" id="inputEmail3" placeholder="example@email.com" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputLogin3" class="col-sm-1 col-form-label">Логин</label>
				<div class="col-sm-3">
					<input type="text" class="form-control" v-model="form.login" name="login" id="inputLogin3" placeholder="9Anpanman" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputPassword3" class="col-sm-1 col-form-label">Пароль</label>
				<div class="col-sm-3">
					<input type="password" class="form-control" v-model="form.password" name="password" id="inputPassword3" required>
				</div>
			</div>
			<div class="row justify-content-center">
				<div class="col-sm-4">
					<button type="submit" class="btn btn-primary">Зарегистрироваться</button>
				</div>
			</div>
		</form>
	</main>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import router from '@/router'

import useRegisterStore from '../stores/register'

export default {
	name: 'RegistrationBlock',

  data() {
    return {
      form: {
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        login: ""
      }
    };
  },

  methods: {
    ...mapActions(useRegisterStore, ['userRegister']),

    async register() {
      const response = await this.userRegister(this.form);

      const { accessToken, user } = response.data

      localStorage.accessToken = accessToken
      localStorage.user = JSON.stringify(user)

      localStorage.accessToken ? router.push('/') : router.push('')
    }
  }
}
</script>
