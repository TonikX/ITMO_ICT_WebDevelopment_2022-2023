<template>
  <form ref="registerForm" @submit.prevent="loginForm">
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />
    </div>
    <div>
      <button type="submit" class="btn btn-primary">Login</button>
    </div>
  </form>
</template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(usersStore, ["login"]),
    async loginForm() {
      const response = await this.login({
        username: this.username,
        password: this.password,
      });
      this.$refs.registerForm.reset();
    },
  },
};
</script>
