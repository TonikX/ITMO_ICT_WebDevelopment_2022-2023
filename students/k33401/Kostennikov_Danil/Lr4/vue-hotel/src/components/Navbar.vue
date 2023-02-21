<template>
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
      <a class="navbar-brand">Hotel app</a>
      <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
          <li v-if="user" class="nav-item">
            <router-link class="nav-link active" to="/freeRooms"
              ><a>Free rooms</a></router-link
            >
          </li>
          <li v-if="user" class="nav-item">
            <router-link class="nav-link active" to="/clientCity"
              ><a>Client city count</a></router-link
            >
          </li>
        </ul>
      </div>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li v-if="!user" class="nav-item auth_link">
            <router-link class="nav-link active" to="/login">
              <a class="nav-link">Login</a></router-link
            >
          </li>
          <li v-if="!user" class="nav-item auth_link">
            <router-link class="nav-link active" to="/register">
              <a class="nav-link">Register</a></router-link
            >
          </li>
          <li v-if="user" class="nav-item profile_link">
            <router-link class="nav-link active" to="/navbar">
              <a class="nav-link" @click="logout" href="#">LogOut</a>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";

export default {
  name: "Navbar",
  computed: {
    ...mapState(usersStore, ["user", "token"]),
  },

  methods: {
    ...mapActions(usersStore, ["logout", "login"]),
  },
};
</script>
