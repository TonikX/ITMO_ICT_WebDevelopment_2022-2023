<template>
  <section style="margin-top: 50px;">
    <div class="card container-xxl col-5 p-5">
      <h2 class="text-center">Log in to Eventika</h2>

      <form class="mt-5">

        <div class="mb-4">
          <label for="email" class="form-label">Enter your email</label>
          <input type="email" class="form-control" id="email" name="email" v-model="email" placeholder="name@example.com">
        </div>

        <div class="mb-4">
          <label for="password" class="form-label">Enter your password</label>
          <input type="password" class="form-control" id="password" name="password" v-model="password" placeholder="Password">
        </div>

        <button type="submit" class="btn btn-dark w-100 py-3 mt-4" @click.prevent="LogIn">Log in</button>

        <p class="text-center text-muted mt-5">Not a member?  <a href="sign_up.html" class="fw-bold text-body"><u>Register</u></a></p>

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
          alert("No user found")
        }
      }else{
        alert("Please fill all the input blocks")
      }


    }
  }
}
</script>

<style scoped>

</style>