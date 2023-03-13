<template>
  <section class="mt-5 mb-5 py-5">
		<div class="card container-xxl col-5 p-5">
			<form>
        <h1 class="text-center ">Meetings</h1>
        <p class="login-text-size text-center mb-5">Регистрация</p>

        <div class="mb-3">
          <label for="firstname" class="form-label">Имя</label>
          <input type="text" class="form-control" id="firstname" v-model="firstname" placeholder="Иван">
        </div>

        <div class="mb-3">
          <label for="lastname" class="form-label">Фамилия</label>
          <input type="text" class="form-control" id="lastname" v-model="lastname" placeholder="Иванов">
        </div>

        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" v-model="email" placeholder="name@example.com">
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Пароль</label>
          <input type="password" class="form-control" id="password" v-model="password" placeholder="* * * * * * * *">
        </div>

        <button type="submit" class="btn btn-dark w-100 py-3 mt-4" @click.prevent="Reg">Зарегистрироваться</button>
        
        <p class="text-center mt-3">Уже есть профиль?  <router-link :to="{name: 'login'}" class="fw-bold text-body"><u>Войти</u></router-link></p>
	    </form>
		</div>
	</section>
</template>

<script>
import axios from "axios";
import { useStateStore } from '../store/UserStatus.js'
export default {
  name: "Register",
  data: function (){
    return{
        email: '',
        password: '',
        lastname: '',
        firstname: ''
    }
  },
  methods:{
    async Reg(){
      if(this.email === '' && this.password === '' && this.lastname === '' && this.firstname === ''){
        alert('Пожалуйста заполните все строки')
      }else{
        const result = await axios.post(`http://localhost:3000/users`, {
          email: this.email,
          password: this.password,
          lastname: this.lastname,
          firstname: this.firstname
        });
        console.log(result);
        if(result.status == 201){
          console.log(result.status)
          // await this.$router.push({name: "Main"});
          localStorage.setItem('userInfo', JSON.stringify(result.data));
          await this.$router.push({name: "Main"})
          const { StateChecker } = useStateStore()
            StateChecker(true);
        }
      }
    }
  }
}
</script>

<style scoped>
  .login-text-size {
    font-size: large;
    font-weight: 500;
  }
</style>