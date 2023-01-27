<template>
    <div class="modal" id="signupModal" tabindex="-1" aria-labelledby="signupModalLabel" aria-hidden="true">

        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="signupModalLabel">Sign Up</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container">
                        <div class="text-danger h6 text-center">
                            <p>{{ mistake }}</p>
                        </div>
                        <div class="mb-3">
                            <label for="username1" class="form-label">Username</label>
                            <input type="text" class="form-control" id="username1" v-model="username"
                                   placeholder="name@example.com">
                        </div>
                        <div class="mb-3">
                            <label for="password1" class="form-label">Password
                            </label>
                            <input type="password" id="password1" class="form-control" v-model="password1">
                        </div>
                        <div class="mb-3">
                            <label for="password2" class="form-label">Retype Password
                            </label>
                            <input type="password" id="password2" class="form-control" v-model="password2">
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="submit" data-bs-toggle="modal"
                            data-bs-target="#loginModal" class="btn btn-outline-success mb-3">
                        Log in
                    </button>
                    <button type="submit" class="btn btn-success mb-3" v-on:click="signupform()">Sign up</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBooksStore from "@/stores/books";

export default {
    name: "Signup",

    computed: {
        ...mapState(useBooksStore, ['user', 'token'])
    },

    data() {
        return {
            username: "",
            password1: "",
            password2: "",
            mistake: ""
        }
    },

    methods: {
        ...mapActions(useBooksStore, ['signup']),
        signupform: async function () {
            const response = this.signup(this.username, this.password1, this.password2)
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
