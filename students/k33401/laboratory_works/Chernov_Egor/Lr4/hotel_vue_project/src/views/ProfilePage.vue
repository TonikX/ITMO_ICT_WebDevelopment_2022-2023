<template>
  <base-layout>
    <nav-bar />
    <h1>Profile info:</h1>
    <div class="container">
      <input v-model="username" type="text" class="row mb-2" placeholder="Username">
      <input v-model="first_name" type="text" class="row mb-2" placeholder="First name">
      <input v-model="last_name" type="text" class="row mb-2" placeholder="Last name">
      <input v-model="email" type="text" class="row mb-2" placeholder="E-mail">
      <div v-if="!isStaff">
        <input v-model="user_guest.phone_guest" type="text" class="row mb-2" placeholder="Phone">
        <input v-model="user_guest.passport_guest" type="text" class="row mb-2" placeholder="Passport">
      </div>
      <div v-else>
        <input v-model="user_employee.phone_employee" type="text" class="row mb-2" placeholder="Phone">
        <input v-model="user_employee.position_employee" type="text" class="row mb-2" placeholder="Position">
      </div>
      <input v-model="password" type="password" class="row" placeholder="Password">
      <button @click="updateData" class="col mt-2">Save</button>
      <button @click="delUser" class="col ms-2 mt-2">Delete</button>
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
      user_guest: {
        phone_guest: "",
        passport_guest: ""
      },
      user_employee: {
        phone_employee: "",
        position_employee: ""
      },
      isStaff: localStorage.getItem('isStaff') === "true",
      password: ""
    }
  },

  computed: {
    ...mapState(useUserStore, ['accUser', 'del'])
  },

  methods: {
    ...mapActions(useUserStore, ['loadAccUser', 'updateAccUser', 'deleteUser']),

    async delUser() {
      await this.deleteUser(localStorage.getItem('accessToken'), localStorage.getItem('idUser'), this.password)

      this.$router.push({name: "hotels"})

      localStorage.removeItem('accessToken')
      localStorage.removeItem('idBookRoom')
      localStorage.removeItem('idUser')
      localStorage.removeItem('username')
      localStorage.removeItem('pinia_hotels')
      localStorage.removeItem('pinia_regCom')
      localStorage.removeItem('pinia_user')
      localStorage.removeItem('isStaff')
    },

    async updateData() {
      const accessToken = localStorage.getItem('accessToken')
      const idUser = localStorage.getItem('idUser')
      await this.updateAccUser(accessToken, idUser, this.username, this.first_name, this.last_name, this.email, this.user_guest.phone_guest, this.user_guest.passport_guest, this.user_employee.phone_employee, this.user_employee.position_employee)
    }
  },

  async mounted() {
    await this.loadAccUser(localStorage.getItem('accessToken'), localStorage.getItem('idUser'))
    this.username = this.accUser.username
    this.first_name = this.accUser.first_name
    this.last_name = this.accUser.last_name
    this.email = this.accUser.email
    this.user_guest.phone_guest = (this.accUser.user_guest?.phone_guest === undefined) ? "" : this.accUser.user_guest.phone_guest
    this.user_guest.passport_guest = (this.accUser.user_guest?.passport_guest === undefined) ? "" : this.accUser.user_guest.passport_guest
    this.user_employee.phone_employee = (this.accUser.user_employee?.phone_employee === undefined) ? "" : this.accUser.user_employee.phone_employee
    this.user_employee.position_employee = (this.accUser.user_employee?.position_employee === undefined) ? "" : this.accUser.user_employee.position_employee
  }
}
</script>

<style scoped>

</style>