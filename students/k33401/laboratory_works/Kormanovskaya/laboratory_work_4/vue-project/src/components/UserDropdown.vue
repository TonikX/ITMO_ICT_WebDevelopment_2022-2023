<template>
    <li class="nav-item dropdown" id="navProfile">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
           data-bs-toggle="dropdown" aria-expanded="false">{{ user.username }}</a>
        <ul class="dropdown-menu dropdown-menu-light dropdown-menu-end" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="http://localhost:8080/profile">Profile</a></li>
            <li><a class="dropdown-item disabled" href="#">Bookshelf</a></li>
            <li><a class="dropdown-item disabled" href="#">Clubs</a></li>
            <li>
                <hr class="dropdown-divider bg-focus">
            </li>
            <li>
                <button class="dropdown-item black" v-on:click="logoutbutton(token)">Logout</button>
            </li>
        </ul>
    </li>
</template>

<script>

import {mapActions, mapState} from 'pinia'
import useLibraryStore from "@/stores/books";
import BaseLayout from "@/layouts/BaseLayout.vue";

export default {
    name: "UserDropdown",

    computed: {
        ...mapState(useLibraryStore, ['token', 'user'])
    },

    methods: {
        ...mapActions(useLibraryStore, ['logout']),

        logoutbutton: async function (token) {
            const response = await this.logout(token)
            location.reload()
        }
    }
}

</script>

<style scoped>

</style>
