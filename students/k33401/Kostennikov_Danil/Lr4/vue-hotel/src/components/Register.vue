<template>
  <form ref="registerForm" @submit.prevent="registerForm">
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />
    </div>
    <div>
      <label for="email">Email:</label>
      <input type="text" id="email" v-model="email" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />
    </div>
    <div>
      <button type="submit" class="btn btn-primary">Register</button>
    </div>
  </form>
</template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";
export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      email: "",
    };
  },
  methods: {
    ...mapActions(usersStore, ["register", "login"]),
    async registerForm() {
      try {
        const response = await this.register({
          username: this.username,
          email: this.email,
          password: this.password,
        });
        this.$refs.registerForm.reset();

        await this.login({
          username: this.username,
          password: this.password,
        });
        this.$router.push("Navbar");
      } catch (error) {
        alert("something went wrong");
      }
    },
  },
};
</script>
