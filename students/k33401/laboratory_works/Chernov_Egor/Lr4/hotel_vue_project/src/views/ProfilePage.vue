<template>
  <base-layout>
    <nav-bar />
    <div class="container col-5 py-4" id="profilePage">
      <h1 class="text-center mb-4">Profile info:</h1>
      <div class="text-center p-4" id="profileForm">
        <div class="input-group mb-3">
          <span class="input-group-text" style="width: 156px" id="username">Username</span>
          <input v-model="username" type="text" class="form-control" aria-describedby="username">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" style="width: 156px">First and last name</span>
          <input v-model="first_name" type="text" aria-label="First name" class="form-control">
          <input v-model="last_name" type="text" aria-label="Last name" class="form-control">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" style="width: 156px" id="email">E-mail</span>
          <input v-model="email" type="text" class="form-control" aria-describedby="email">
        </div>
        <div v-if="!isStaff">
          <div class="input-group mb-3">
            <span class="input-group-text" style="width: 156px" id="phone">Phone</span>
            <input v-model="user_guest.phone_guest" type="text" class="form-control" aria-describedby="phone">
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" style="width: 156px" id="passport">Passport</span>
            <input v-model="user_guest.passport_guest" type="text" class="form-control" aria-describedby="passport">
          </div>
        </div>
        <div v-else>
          <div class="input-group mb-3">
            <span class="input-group-text" style="width: 156px" id="phone">Phone</span>
            <input v-model="user_employee.phone_employee" type="text" class="form-control" aria-describedby="phone">
          </div>
          <div class="input-group mb-3">
            <span class="input-group-text" style="width: 156px" id="position">Position</span>
            <input v-model="user_employee.position_employee" type="text" class="form-control" aria-describedby="position">
          </div>
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" style="width: 156px" id="password">Password</span>
          <input v-model="password" type="password" class="form-control" aria-describedby="password">
        </div>
        <a class="nav-link py-1 px-2 fs-5 mt-3" @click="updateData" id="saveButton">Save</a>
        <a class="nav-link py-1 px-2 fs-5 mt-3" @click="delUser" id="delButton">Delete</a>
      </div>
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
a {
  cursor: pointer;
}

#profileForm {
  background-color: rgba(253, 246, 236, 0.4);
  border-radius: 8px 8px 8px 8px;
  color: black;
}

#profilePage {
  min-height: 100vh;
}

#saveButton {
  background-color: #E0E7E9;
  border-radius: 8px 8px 8px 8px;
}

#delButton {
  background-color: #ffdfd4;
  border-radius: 8px 8px 8px 8px;
}
</style>