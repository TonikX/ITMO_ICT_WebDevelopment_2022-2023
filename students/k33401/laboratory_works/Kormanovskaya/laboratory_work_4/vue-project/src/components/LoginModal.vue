<template>
    <div class="modal" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">

        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="loginModalLabel">Log In</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container">
                        <div class="text-danger h6 text-center">
                            <p>{{ mistakeLogin }}</p>
                        </div>
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" class="form-control" id="username" v-model="username"
                                   placeholder="name@example.com">
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password |
                                <a href="#" class="text-decoration-none align-self-end">
                                    <small>Forgot password?</small>
                                </a>
                            </label>
                            <input type="password" id="password" class="form-control" v-model="password">
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="submit" v-on:click="loginform(username, password)" class="btn btn-success mb-3">
                        Log in
                    </button>
                    <button type="submit" class="btn btn-outline-success mb-3"
                       data-bs-toggle="modal"
                       data-bs-target="#signupModal" >Sign up</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBooksStore from "@/stores/books";

export default {
    name: "LoginModal",

    computed: {
        ...mapState(useBooksStore, ['user', 'token'])
    },

    data() {
        return {
            username: "",
            password: "",
            mistakeLogin: ""
        }
    },

    methods: {
        ...mapActions(useBooksStore, ['login', 'loadUserinfo']),
        loginform: async function () {
            const response = this.login(this.username, this.password)
            response
                .then(async (result) => {
                    await this.loadUserinfo(result.data.auth_token)
                    location.reload()
                })
                .catch((error) => {
                    this.mistakeLogin = "Invalid username and password combination"
                })
        }
    }
}
</script>

<style scoped>

</style>
