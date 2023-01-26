<template>
    <div class="modal fade" id="logIn" tabindex="-1" aria-labelledby="logInLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title text-center container-fluid" id="logInpLabel">Log In</h5>
                </div>
                <div class="modal-body">
                    <form>
                        <!-- Username input -->
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="usernameLogIn" name="user"
                                   placeholder="username" v-model="username">
                            <label for="usernameLogIn">
                                Username
                            </label>
                        </div>
                        <!-- Password input -->
                        <div class="form-floating mb-3">
                            <input type="password" class="form-control" id="passwordLogIn" name="password"
                                   placeholder="password" v-model="password">
                            <label for="passwordLogIn">
                                Password
                            </label>
                        </div>
                        <div class="row mb-4">
                            <div class="col d-flex justify-content-center">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="rememberMe" checked>
                                    <label class="form-check-label" for="rememberMe"> Remember me </label>
                                </div>
                            </div>
                            <div class="col">
                                <a href="#">Forgot password?</a>
                            </div>
                        </div>
                        <!-- LogIn button -->
                        <div class="text-center mb-4">
                            <button type="button" class="btn btn-primary btn-block mb-4" @click="Login"
                                    data-bs-toggle="modal" data-bs-target="#logIn">Log In
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import {useUserStore} from "../stores/user.js";

import {mapActions} from 'pinia'

export default {
    name: "LogInPopUp",
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        ...mapActions(useUserStore, ['logIn', 'fetchUser']),

        Login: async function () {
            const response = this.logIn(this.username, this.password)

            response
                .then((result) => {
                    this.fetchUser(result.data.auth_token)
                })
                .catch((err) => {
                    alert("Неправильный логин или пароль");
                })
        }
    }
}
</script>
