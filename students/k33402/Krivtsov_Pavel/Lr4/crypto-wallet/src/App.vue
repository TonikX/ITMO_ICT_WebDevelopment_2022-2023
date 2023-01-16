<script>
import $ from "jquery";

export default {
  computed: {
    auth_token() {
      return localStorage.getItem("auth_token")
    }
  },
  created() {
    if (this.auth_token) {
      $.ajaxSetup({
        headers: {'Authorization': "Token" + " " + this.auth_token}
      })
    }
  }
}
</script>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<!--  <RouterLink to="/">Home</RouterLink>-->
  <RouterView />
</template>

<style>

</style>
