<template>
	<form @submit.prevent="login">
		<div class="form-group row justify-content-center pt-5"> 
			<div class="col-md-4 mb-3">
				<label for="email">Почта</label>
				<input type="email" class="form-control" id="email" v-model="form.email" name="email" aria-describedby="emailHelp" placeholder="Enter email">
			</div>
		</div>
		<div class="form-group row justify-content-center">
			<div class="col-md-4 mb-3">
				<label for="password">Пароль</label>
				<input type="password" class="form-control" v-model="form.password" id="password" name="password" placeholder="Password">
			</div>
		</div>
		<div class="row justify-content-center">
			<div class="col-md-4 mb-3">
				<div class="form-check">
					<input type="checkbox" class="form-check-input" id="exampleCheck1">
					<label class="form-check-label" for="exampleCheck1">Запомнить меня</label>
				</div>
				<button type="submit" class="btn btn-primary">Войти</button>
				<a role="button" href="#" @click="$router.push('/registration/')" class="btn btn-primary">Зарегистрироваться</a>
			</div>
		</div>
	</form>
</template>

<script>
import { mapActions, mapState } from 'pinia' 
import router from '@/router' 

import useLoginStore from '../stores/login'

export default {
	name: 'EnterBlock', 

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

		localStorage.accessToken ? router.push('/') : router.push('/enter')
	}
}
}
</script>