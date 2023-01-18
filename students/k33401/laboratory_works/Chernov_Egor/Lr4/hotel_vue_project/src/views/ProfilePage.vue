<template>
  <base-layout>
    <nav-bar />
    <h1>Profile info:</h1>
    <div class="container">
      <input v-model="username" type="text" class="row mb-2" placeholder="Username">
      <input v-model="first_name" type="text" class="row mb-2" placeholder="First name">
      <input v-model="last_name" type="text" class="row mb-2" placeholder="Last name">
      <input v-model="email" type="text" class="row mb-2" placeholder="E-mail">
      <div v-if="user_guest">
        <input v-model="user_guest.phone_guest" type="text" class="row mb-2" placeholder="Phone">
        <input v-model="user_guest.passport_guest" type="text" class="row mb-2" placeholder="Passport">
      </div>
      <div v-else>
        <input v-model="user_employee.phone_employee" type="text" class="row mb-2">
        <input v-model="user_employee.position_employee" type="text" class="row mb-2">
      </div>
      <button @click="updateData" class="row">Save</button>
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import NavBar from "@/components/NavBar.vue";
import {mapActions, mapState} from "pinia";
import useUserStore from "@/stores/user";

export default {
  name: "ProfilePage",

  components: { BaseLayout, NavBar },

  data() {
    return {
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      user_guest: "",
      user_employee: ""
    }
  },

  computed: {
    ...mapState(useUserStore, ['accUser'])
  },

  methods: {
    ...mapActions(useUserStore, ['loadAccUser']),

    updateData() {

    }
  },

  mounted() {
    this.loadAccUser(localStorage.getItem('accessToken'), localStorage.getItem('idUser'))
    this.username = this.accUser.username
    this.first_name = this.accUser.first_name
    this.last_name = this.accUser.last_name
    this.email = this.accUser.email
    this.user_guest = this.accUser.user_guest
    this.user_employee = this.accUser.user_employee
  }
}
</script>

<style scoped>

</style>