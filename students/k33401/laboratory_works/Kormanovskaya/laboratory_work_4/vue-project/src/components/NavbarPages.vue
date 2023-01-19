<template>
    <nav class="navbar navbar-dark bg-dark navbar-expand-md justify-content-end">
        <div class="container-fluid">
            <a class="navbar-brand title-font text-white ms-2"
               href="http://localhost:8080/">
                <h2>Читае<span class="text-danger">м</span>ы</h2>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
                <ul class="navbar-nav mb-1 mb-lg-0 mx-0 mx-lg-0 mx-sm-3" id="navbarTop">
                    <div v-if="token">
                        <user-dropdown></user-dropdown>
                    </div>
                    <div v-else >
                        <li class="nav-item" id="navLogin">
                            <button class="btn btn-success" type="submit" data-bs-toggle="modal"
                                    data-bs-target="#loginModal">Log in
                            </button>
                        </li>
                    </div>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import UserDropdown from "@/components/UserDropdown.vue";
import useBooksStore from "@/stores/books";
import BaseLayout from "@/layouts/BaseLayout.vue";

export default {
    components: {UserDropdown},
    name: "NavbarPages",

    computed: {
        ...mapState(useBooksStore, ['user', 'token'])
    },

    methods: {

    },
}
</script>

<style scoped>

</style>
