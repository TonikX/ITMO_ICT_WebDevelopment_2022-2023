<template>
  <div v-if="user" class="container w-75">
    <h1 class="m-5">Profile</h1>
    <h3 class="mt-3">Username</h3>
    <p id="name">{{ user.username }}</p>
    <h3 class="mt-3">Email</h3>
    <p id="surname">{{ user.email }}</p>
    <h3 class="mt-3">Moderator</h3>
    <p id="email">{{ user.is_staff }}</p>
  </div>

</template>

<script>

import useBazzarStore from "@/stores/bazzar";
import {mapActions, mapState} from "pinia";

export default {
  name: "Profile",
  computed: {
    ...mapState(useBazzarStore, ['token', 'user'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['loadUser'])
  },
  mounted() {
    if (!this.token) {
      document.location = document.location.origin
    }
  }
}
</script>


<style scoped>

</style>