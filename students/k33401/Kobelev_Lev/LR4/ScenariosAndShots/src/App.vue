<script setup>
import { RouterView } from 'vue-router'
import FooterMenu from "./components/FooterMenu.vue";
import HeaderMenu from "./components/HeaderMenu.vue";
import SignUpPopUp from "./components/SignUpPopUp.vue";
import LogInPopUp from "./components/LogInPopUp.vue";
</script>

<template>
    <body class="d-flex flex-column min-vh-100">
        <HeaderMenu />
        <main>
            <SignUpPopUp />
            <LogInPopUp />
            <RouterView />
        </main>
        <FooterMenu />
    </body>
</template>

<style>
    @import './assets/main.css';
</style>
