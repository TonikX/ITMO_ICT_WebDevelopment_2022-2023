<template>
  <div class="container">
    <div class="row justify-content-center mt-5 p-5">
      <div class="col-12">
        <div class="login-wrap d-flex">
          <div class="w-100 p-5">
            <div class="d-flex">
              <div class="w-100">
                <h3 class="mb-4">Sign Up</h3>
              </div>
            </div>

            <div class="form-group mb-3">
              <label class="label" for="email">Email</label>
              <input
                id="email"
                type="text"
                class="form-control"
                placeholder="Username"
                v-model="form.email"
                required
              />
            </div>
            <div class="form-group mb-3">
              <label class="label" for="name">Username</label>
              <input
                id="name"
                type="text"
                class="form-control"
                placeholder="Username"
                v-model="form.username"
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
            <div class="form-group mb-3">
              <label class="label" for="password-confirm">
                Confirm Password
              </label>
              <input
                v-model="form.password2"
                id="password-confirm"
                type="password"
                class="form-control"
                placeholder="Password"
                required
              />
            </div>

            <div class="form-group">
              <button
                @click="signup()"
                class="form-control btn btn-primary submit px-3 mt-3"
              >
                Sign Up
              </button>
            </div>

            <p class="text-center mt-2">
              Already Singed up?
              <router-link to="/login" data-toggle="tab"> Sign In </router-link>
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
  name: 'SignUpView',

  data () {
    return {
      form: {
        username: null,
        password: null,
        password2: null,
        email: null
      }
    }
  },

  beforeCreate () {
    if (localStorage.getItem('accessToken')) {
      this.$router.push('/')
    }
  },

  methods: {
    async signup () {
      if (this.form.password === this.form.password2 && this.form.password !== null) {
        try {
          const response = await axios.post(
            'http://localhost:3000/signup',
            {
              email: this.form.email,
              password: this.form.password,
              username: this.form.username
            })

          if (response.status === 201) {
            this.$router.push('/login')
          }
        } catch (e) {
          alert(e.response.data)
        }
      } else {
        alert('Пароли не совпадают')
      }
    }
  }
}
</script>

<style scoped></style>
