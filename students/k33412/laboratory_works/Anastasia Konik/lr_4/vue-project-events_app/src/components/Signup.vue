<template>
  <main class="container-xl p-5 mb-5">
    <h1 class="row mb-4 mt-4 justify-content-center">Sign up</h1>
    <form class="signup-form" action="http://localhost:8000/api/users/list" method="POST">
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
          <div class="col-sm-3 col-md-4">
            <input
                v-model="first_name"
                type="text"
                class="form-control"
                name="first_name"
                placeholder="First name"
                id="floatingName"
                required>
            <label for="floatingName"></label>
          </div>
        </div>
      </div>
      <div class="form-floating">
        <div class="row justify-content-center">
          <div class="col-sm-3 col-md-4">
            <input
                v-model="last_name"
                type="text"
                class="form-control"
                name="last_name"
                placeholder="Last name"
                id="floatingLastname"
                required>
            <label for="floatingLastname"></label>
          </div>
        </div>
      </div>
      <div class="form-floating">
        <div class="row justify-content-center">
          <div class="col-sm-3 col-md-4">
            <input
                v-model="email"
                type="text"
                class="form-control"
                name="email"
                placeholder="Email"
                id="floatingEmail"
                required>
            <label for="floatingEmail"></label>
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
      <div class="form-floating">
        <div class="row justify-content-center">
          <div class="col-sm-3 col-md-4">
            <input
                @change="uploadFile"
                ref="file"
                type="file"
                class="form-control"
                name="img_url"
                placeholder="Place your profile image url"
                id="floatingImage">
            <label for="floatingImage"></label>
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
          <button type="button" @click="signup" class="btn btn-primary" aria-pressed="true" id="register">Register</button>
        </div>
      </div>
    </form>
  </main>
</template>

<script>
import useUsersStore from "@/stores/users";
import {mapActions} from "pinia";

export default {
  name: "Signup",
  data() {
    return {
      username: "",
      password: "",
      first_name: "",
      last_name: "",
      email: "",
      img_url: null,
      err: ""
    };
  },
  methods: {
    ...mapActions(useUsersStore, ['signUp', 'login']),
    uploadFile() {
      this.img_url = this.$refs.file.files[0];
    },
    async signup() {
      this.err = ''
      if (!this.email || !this.password || !this.username || !this.first_name || !this.last_name) {
        this.err = 'Error! Fill in required fields!'
        return
      }
      let result = null
      try {
        result = await this.signUp({
          username: this.username,
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password,
          img_url: this.img_url
        })
      } catch (e) {
        this.err = 'Error!'
        return
      }

      if (result?.status === 201) {
        await this.login({
          username: this.username,
          password: this.password
        })
        this.$router.push('/main')
      }
    }
  }
}
</script>

<style scoped>

</style>