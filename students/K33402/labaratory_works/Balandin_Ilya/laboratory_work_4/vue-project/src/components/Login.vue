<template>
  <div class="modal fade" id="loginModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
       aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="loginEmail" class="form-label">Username</label>
            <input type="text" class="form-control" id="loginEmail" v-model="username">
          </div>
          <div class="mb-3">
            <label for="loginPassword" class="form-label">Password</label>
            <input type="password" class="form-control" v-model="password" id="loginPassword">
          </div>
          <button type="submit" class="btn btn-primary" v-on:click="loginform()">Submit</button>
          <p class="text-end">
            <RouterLink to="/register">Register</RouterLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBazzarStore from "@/stores/bazzar";

export default {
  name: "Login",

  computed: {
    ...mapState(useBazzarStore, ['user', 'token'])
  },

  data() {
    return {
      username: "",
      password: "",
    }
  },

  methods: {
    ...mapActions(useBazzarStore, ['login', 'loadUser']),
    loginform: async function () {
      const response = await this.login(this.username, this.password)
      document.location.reload()
    }
  }
}
</script>

