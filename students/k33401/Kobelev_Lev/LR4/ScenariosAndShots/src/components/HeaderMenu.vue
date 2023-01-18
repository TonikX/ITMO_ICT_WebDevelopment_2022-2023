<template>
    <header class="header sticky-top">
        <!-- Sticky Navbar -->
        <nav class="navbar navbar-expand-md px-3 py-2 container-fluid">
            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContentMobile" aria-controls="navbarSupportedContentMobile"
                    aria-expanded="false" aria-label="Toggle navigation">
                List
            </button>
            <!-- Main Navigation -->
            <div class="col-6 collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto my-0">
                    <router-link :to="{name: 'scenarios'}">
                    <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="#">Scenarios</a>
                    </li>
                    </router-link>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Articles</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About</a>
                    </li>
                </ul>
            </div>
            <!-- Sign Up and Log In -->
            <div v-if="!username" class="col-6 d-flex justify-content-end">
                <div class="text-center">
                    <form>
                        <button type="button" class="btn btn-sm rounded-pill btn-outline-primary mx-1"
                                data-bs-toggle="modal" data-bs-target="#signUp">Sign Up
                        </button>
                    </form>
                </div>
                <div class="text-center">
                    <form>
                        <button type="button" class="btn btn-sm rounded-pill btn-primary mx-1"
                                data-bs-toggle="modal" data-bs-target="#logIn">Log In
                        </button>
                    </form>
                </div>
            </div>
            <!-- Profile -->
            <div v-else class="col-8 col-sm-4 d-flex justify-content-end">
                <div class="btn-group">
                    <div class="dropdown">
                        <button id='usernameText' class="btn btn-light dropdown-toggle" type="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false">
                            {{ username }}
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <li>
                                <button class="dropdown-item" href="profile.html">Profile</button>
                            </li>
                            <li>
                                <button class="dropdown-item" href="#">Settings</button>
                            </li>
                            <li>
                                <button class="dropdown-item" @click="logOut">Sign Out</button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <!-- Mobile Navigation -->
            <div class="col-6 collapse" id="navbarSupportedContentMobile">
                <ul class="navbar-nav me-auto my-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Scenarios</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Articles</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About</a>
                    </li>
                </ul>
            </div>
        </nav>
    </header>
</template>

<script>
import {useUserStore} from "../stores/user.js";

import {mapState, mapActions} from 'pinia'


export default {
    name: "HeaderMenu",

    computed: {
        ...mapState(useUserStore, ['username']),
    },

    methods: {
        ...mapActions(useUserStore, ['logOut'])
    }

}
</script>

<style scoped>
header {
    background-color: var(--bs-light);
}

a {
    text-decoration: none;
    color: inherit;
}
</style>
