<script setup>
import {RouterLink, RouterView} from 'vue-router'
import Navbar from "@/components/Navbar.vue";

</script>

<template>
  <header>
    <navbar></navbar>
  </header>
  <main>
    <router-view/>
  </main>
  <footer>

  </footer>
</template>

<style>

</style>