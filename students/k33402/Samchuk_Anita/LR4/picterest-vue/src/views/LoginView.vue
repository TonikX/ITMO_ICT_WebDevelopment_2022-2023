<template>
  <div class="container">
    <div class="row justify-content-center mt-5 p-5">
      <div class="col-12">
        <div class="login-wrap d-flex">
          <div
            class="login-img w-50"
          ></div>

          <div class="w-50 p-5">
            <h3 class="mb-4">Sign In</h3>

              <div class="form-group mb-3">
                <label class="label" for="name">Email</label>
                <input
                  id="name"
                  type="text"
                  class="form-control"
                  placeholder="Email"
                  v-model="form.email"
                  required
                />
              </div>
              <div class="form-group mb-3">
                <label class="label" for="password">Password</label>
                <input
                  id="password"
                  type="password"
                  class="form-control"
                  placeholder="Password"
                  v-model="form.password"
                  required
                />
              </div>
              <div class="form-group">
                <button
                  @click="login()"
                  class="form-control btn btn-primary submit px-3"
                >
                  Sign In
                </button>
              </div>
              <div class="form-group d-flex">
                <div class="w-50">
                  <label class="checkbox-wrap checkbox-primary mb-0">Remember Me
                    <input type="checkbox" checked="" />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="w-50 text-right">
                  <a href="#">Forgot Password</a>
                </div>
              </div>

            <p class="text-center">
              Not a member? <router-link to="/signup">Sign Up</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',

  data () {
    return {
      form: {
        email: null,
        password: null
      }
    }
  },

  beforeMount () {
    if (localStorage.getItem('accessToken')) {
      this.$router.push('/')
    }
  },

  methods: {
    async login () {
      try {
        const response = await axios.post('http://localhost:3000/login', this.form)

        if (response.status === 200) {
          localStorage.setItem('accessToken', response.data.accessToken)
          localStorage.setItem('user', JSON.stringify(response.data.user))
          this.$router.push('/')
        }
      } catch (e) {
        alert(e.response.data)
      }
    }
  }
}
</script>

<style scoped>
.text-right  {
  text-align: right;
}

.login-img {
  background-image: url("@/assets/img/logo-photo.jpeg");
}
</style>
