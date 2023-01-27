<script setup>
import {RouterLink, RouterView} from 'vue-router'
import Navbar from "@/components/Navbar.vue";
import FooterOwn from "@/components/FooterOwn.vue";

</script>

<template>
    <body class="d-flex flex-column min-vh-100">
    <navbar></navbar>
    <main class="mt-5">
        <RouterView/>
    </main>
    <footer-own></footer-own>
    </body>


</template>

<style>

</style>
