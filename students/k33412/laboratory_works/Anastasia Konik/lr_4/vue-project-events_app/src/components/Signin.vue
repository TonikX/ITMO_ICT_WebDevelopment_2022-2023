<template>
  <main class="container-xl p-5 mb-5">
    <h1 class="row mb-4 mt-4 justify-content-center">Sign in</h1>
    <form>
      <div class="form-floating">
        <div class="row mt-3 justify-content-center">
          <div class="col-sm-3 col-md-4">
            <input
                v-model="username"
                type="text"
                class="form-control"
                name="username"
                placeholder="Username"
                id="floatingUsername"
                required>
            <label for="floatingUsername"></label>
          </div>
        </div>
      </div>
      <div class="form-floating">
        <div class="row justify-content-center">
          <div class="col-sm-3 col-md-4 text-center">
            <input
                v-model="password"
                type="password"
                class="form-control"
                name="password"
                id="floatingPassword"
                placeholder="Password"
                required>
            <label for="floatingPassword"></label>
          </div>
        </div>
      </div>
      <p
          v-if="err"
          class="login-error text-danger text-center">
        <strong>{{ err }}</strong>
      </p>
      <div class="row justify-content-center">
        <div class="col-xl-1 col-lg-1 col-md-2 col-sm-2 text-center">
          <button type="button" @click="signin" class="btn btn-primary" aria-pressed="true" id="register">Login</button>
        </div>
      </div>
    </form>
    <div class="row mt-3">
      <router-link to="/signup">Register</router-link>
    </div>

  </main>

</template>

<script>
import {mapActions} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  name: "Signin",
  data() {
    return {
      username: "",
      password: "",
      err: ""
    };
  },
  methods: {
    ...mapActions(useUsersStore, ['login']),
    async signin() {
      this.err = ''
      if (!this.username || !this.password) {
        this.err = 'Error! Enter username and password!'
        return
      }
      try {
        await this.login({
          username: this.username,
          password: this.password
        })
      } catch (e) {
        this.err = 'Wrong password or username! Try again!'
        return
      }
      this.$router.push('/main')
    }
  }
}
</script>

<style scoped>

</style>