<template>
	<main class="container pt-5">
		<form @submit.prevent="register">
			<div class="form-row" >
				<div class="col-md-4 mb-3">
					<label for="first_name">Имя</label>
					<input type="text" class="form-control" v-model="form.first_name" id="first_name" name="first_name" placeholder="Светлана" required>
				</div>
				<div class="col-md-4 mb-3">
					<label for="last_name">Фамилия</label>
					<input type="text" class="form-control" id="last_name" v-model="form.last_name" name="last_name" placeholder="Кулагина" required>
				</div>
				<div class="col-md-4 mb-3">
					<label for="email">Почта</label>
					<input type="email" class="form-control" id="email" name="email" v-model="form.email" placeholder="kulagina@mail.com" required>
				</div>
				<div class="col-md-4 mb-3">
					<label for="username">Имя пользователя</label>
					<div class="input-group">
						<div class="input-group-prepend">
							<span class="input-group-text" id="inputGroupPrepend2">@</span>
						</div>
						<input type="text" class="form-control" id="username" v-model="form.username" name="username" placeholder="ras_svet" aria-describedby="inputGroupPrepend2" required>
					</div>
				</div>
				<div class="col-md-4 mb-3">
					<label for="password">Пароль</label>
					<input type="password" class="form-control" id="password" v-model="form.password" name="password" required>
				</div>
			</div>
			<button class="btn btn-primary" type="submit" id="reg">Зарегистрироваться</button>
		</form>
	</main>
</template>

<script>
import { mapActions, mapState } from 'pinia' 
import router from '@/router' 
 
import useRegisterStore from '../stores/register'

export default {
	name: 'RegBlock', 
 
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