<template>
    <header class="fixed-top">
        <navbar-pages></navbar-pages>
        <navbar-genres></navbar-genres>
    </header>
    <div class="empty-div"></div>
    <login-modal></login-modal>
    <signup></signup>
</template>

<script>

import NavbarGenres from "@/components/NavbarGenres.vue";
import NavbarPages from "@/components/NavbarPages.vue";
import LoginModal from "@/components/LoginModal.vue";
import Signup from "@/components/Signup.vue";

export default {
    name: "Navbar",
    components: {LoginModal, NavbarPages, NavbarGenres, Signup}
}
</script>

<style scoped>

</style>
