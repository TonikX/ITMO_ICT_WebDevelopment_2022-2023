<template>
  <AppLayout>
    <RouterView/>
  </AppLayout>
</template>

<script>
import $ from "jquery";
import AppLayout from "./layouts/AppLayout.vue";

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
  },
  components: {
    AppLayout
  }
}
</script>

<script setup>
import {RouterView} from 'vue-router'
</script>
