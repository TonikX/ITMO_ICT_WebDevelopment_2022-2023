<template>
  <div class="container container-fluid p-5">
    <h1 class="my-5">Staff registration</h1>
    <div class="col-md-12">
      <label for="registerName" class="form-label">Emain</label>
      <input type="email" class="form-control" v-model="email" id="registerName" required>
    </div>
    <div class="col-md-4">
      <label for="registerEmail" class="form-label">Username</label>
      <input type="text" class="form-control" v-model="username" id="registerEmail" required>
    </div>
    <div class="col-md-4">
      <label for="registerPassword1" class="form-label">Password</label>
      <input type="password" class="form-control" v-model="password" id="registerPassword1" required>
    </div>
    <div class="col-md-4">
      <label for="registerPassword2" class="form-label">Confirm Password</label>
      <input type="password" class="form-control" v-model="password2" id="registerPassword2" required>
    </div>
    <div class="col-12 mt-3">
      <button class="btn btn-primary" v-on:click="registerUser()" type="submit">Register</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import useBazzarStore from "@/stores/bazzar";

export default {
  name: "Register",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      password2: ""
    }
  },
  computed: {
    ...mapState(useBazzarStore, ['token'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['register']),
    registerUser: async function () {
      await this.register(this.username, this.email, this.password, this.password2)
      document.location = document.location.origin
    }
  },
  mounted() {
    if (this.token){
      document.location = document.location.origin
    }
  }
}
</script>

<style scoped>

</style>