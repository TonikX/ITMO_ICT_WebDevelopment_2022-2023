<template>
  <section class="mt-5 mb-5 py-5">
    <div class="card container-xxl col-5 p-5">
      <form>
        <h1 class="text-center ">Meetings</h1>
        <p class="login-text-size text-center mb-5">Вход</p>

        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" name="email" v-model="email" placeholder="name@example.com">
        </div>

				<div class="mb-4">
          <label for="password" class="form-label">Пароль</label>
          <input type="password" class="form-control" id="password" name="password" v-model="password" placeholder="* * * * * * * *">
        </div>

        <button type="submit" class="btn btn-dark w-100 py-3 mt-4" @click.prevent="LogIn">Войти</button>

        <p class="text-center mt-3">Не зарегистрированы?  <router-link :to="{name: 'register'}" class="fw-bold text-body"><u>Регистрация</u></router-link></p>
      </form>
    </div>
  </section>
</template>

<script>
  import axios from "axios";
  import { useStateStore } from '../store/UserStatus.js'
  export default {
    name: "Login",
    data: function (){
      return{
        email: '',
        password: '',
      }
    },
    methods:{
      async LogIn(){
        if(this.email !== "" && this.password !== ""){
          const res = await axios.get(`http://localhost:3000/users?email=${this.email}&password=${this.password}`)
          if(res.status==200 && res.data.length>0){
            localStorage.setItem('userInfo', JSON.stringify(res.data));
            await this.$router.push({name: "Main"})
            const { StateChecker } = useStateStore()
            StateChecker(true);
          }else{
            alert("Ошибка, попробуйте еще раз")
          }
        }else{
          alert("Пожалуйста заполните все строки")
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