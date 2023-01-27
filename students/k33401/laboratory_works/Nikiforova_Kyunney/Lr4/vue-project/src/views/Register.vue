<template>
  <section style="margin-top: 50px;">
    <div class="card container-xxl col-5 p-5">
      <h2 class="text-center">Create an account</h2>

      <form class="mt-5">

        <div class="mb-4">
          <label for="firstname" class="form-label" >First name</label>
          <input type="text" class="form-control"  v-model="firstname" id="firstname" placeholder="Your first name">
        </div>

        <div class="mb-4">
          <label for="lastname" class="form-label">Last name</label>
          <input type="text" class="form-control" v-model="lastname" id="lastname"  placeholder="Your last name">
        </div>

        <div class="mb-4">
          <label for="email" class="form-label">Email address</label>
          <input type="email" class="form-control" v-model="email" id="email" placeholder="name@example.com">
        </div>

        <div class="mb-4">
          <label for="password" class="form-label">Password</label>
          <input type="password" class="form-control"  v-model="password" id="password"  placeholder="Your password">
        </div>

        <button type="submit" class="btn btn-dark w-100 py-3 mt-4" @click.prevent="Reg">Register</button>

        <p class="text-center text-muted mt-5">Have already an account? <router-link :to="{name: 'login'}" class="fw-bold text-body"><u>Log in here</u></router-link></p>

      </form>

    </div>
  </section>
</template>

<script>
import axios from "axios";
// import router from "@/router";
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
        alert('Please fill all the input fields')
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
      },
  }


}
</script>

<style scoped>

</style>