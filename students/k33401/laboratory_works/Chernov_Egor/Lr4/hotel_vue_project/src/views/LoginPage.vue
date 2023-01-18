<template>
  <base-layout>
    <div class="container">
      <login-form v-if="isReg" />
      <reg-form v-else />
      <p v-if="isReg">Do you have an account?</p>
      <button @click="reg" v-if="isReg">Register</button>
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import LoginForm from "@/components/LoginForm.vue";
import RegForm from "@/components/RegUserForm.vue";

export default {
  name: "RegUserPage",

  components: { LoginForm, RegForm, BaseLayout },

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

</style>