<template>
  <base-layout>
    <nav-bar />
    <div id="loginPage">
      <div class="container col-4 p-0">
        <login-form v-if="isReg" />
        <reg-form v-else />
        <p v-if="isReg" class="mt-4 fs-4 text-center">You don't have an account?</p>
        <a class="nav-link py-1 px-2 text-center fs-5" @click="reg" v-if="isReg">Register</a>
      </div>
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import LoginForm from "@/components/LoginForm.vue";
import RegForm from "@/components/RegUserForm.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "RegUserPage",

  components: { NavBar, LoginForm, RegForm, BaseLayout },

  data() {
    return {
      isReg: true
    }
  },

  methods: {
    reg() {
      this.isReg = !this.isReg
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
  background-color: #E0E7E9;
  border-radius: 8px 8px 8px 8px;
  color: black;
}

#loginPage {
  height: 100vh;
}
</style>