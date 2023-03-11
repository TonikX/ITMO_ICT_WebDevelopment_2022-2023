<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand fw-bold text-main-own" href="#">GameBa<span class="text-primary">z</span><span
          class="text-danger">z</span>ar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
              aria-expanded="false" aria-label="Toggle navigation">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
             class="bi bi-list text-secondary-own" viewBox="0 0 16 16">
          <path fill-rule="evenodd"
                d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
        </svg>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ">
          <li class="nav-item">
            <router-link class="nav-link text-secondary-own" to="/">Products</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-secondary-own" to="/sells">Sells</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-secondary-own" to="/staff">Staff</router-link>
          </li>
        </ul>
        <ul class="navbar-nav mb-2 mb-lg-0" id="isUser">
          <div v-if="token">
            <li class="nav-item dropdown" id="isUser">
              <a class="nav-link dropdown-toggle text-secondary-own" href="#" id="navbarDropdown" role="button"
                 data-bs-toggle="dropdown" aria-expanded="false">
                {{ user.username }}
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <router-link class="dropdown-item" to="/profile">Profile</router-link>
                </li>
                <li><a class="dropdown-item text-danger" href="#" v-on:click="logoutUser()">Logout</a></li>
              </ul>
            </li>
          </div>
          <div v-else>
            <li class="nav-item" id="isNotUser">
              <button type="button" class="btn btn-link text-decoration-none" data-bs-toggle="modal"
                      data-bs-target="#loginModal">
                Login
              </button>
            </li>
          </div>
        </ul>
      </div>
    </div>
  </nav>
  <login></login>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBazzarStore from "@/stores/bazzar";
import BaseLayout from "@/layouts/BaseLayout.vue";
import Login from "../components/Login.vue";

export default {
  name: "Navbar",
  components: {Login},
  computed: {
    ...mapState(useBazzarStore, ['user', 'token'])
  },
  methods: {
    ...mapActions(useBazzarStore, ['logout']),

    logoutUser: async function () {
      this.logout()
      document.location.reload()
    }
  }

}
</script>