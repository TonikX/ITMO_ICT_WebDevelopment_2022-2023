<script>
import $ from "jquery";

export default {
  created() {
    let authToken = localStorage.getItem("auth_token")
    if (authToken) {
      $.ajaxSetup({
        headers: {'Authorization': "Token" + authToken}
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
