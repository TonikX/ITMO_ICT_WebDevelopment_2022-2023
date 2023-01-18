<template>
    <div class="modal fade" id="signUp" tabindex="-1" aria-labelledby="signUpLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title text-center container-fluid" id="signUpLabel">Sign Up</h5>
                </div>
                <div class="modal-body">
                    <form onsubmit="signup(event)">
                        <!-- Email input -->
                        <div class="form-floating mb-3">
                            <input type="email" class="form-control" id="emailSignUp" placeholder="email@mail.ru"
                                   v-model="email">
                            <label for="emailSignUp">
                                Email address
                            </label>
                        </div>
                        <!-- Username input -->
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="usernameSignUp" placeholder="username"
                                   v-model="username">
                            <label for="usernameSignUp">
                                Username
                            </label>
                        </div>
                        <!-- Password input -->
                        <div class="form-floating mb-3">
                            <input type="password" class="form-control" id="passwordSignUp"
                                   placeholder="password" v-model="password">
                            <label for="passwordSignUp">
                                Password
                            </label>
                        </div>
                        <!-- Submit button -->
                        <div class="text-center mb-4">
                            <button type="button" class="btn btn-primary btn-block mb-4" @click="Signup"
                                    data-bs-toggle="modal" data-bs-target="#signUp">Sign Up
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
    name: "SignUpPopUp",
    data() {
        return {
            username: '',
            password: '',
            email: '',
        }
    },
    methods: {
        ...mapActions(useUserStore, ['signUp', 'fetchUser']),

        Signup: async function () {
            const response = this.signUp(this.username, this.password, this.email)

            response
                .then((result) => {
                    this.fetchUser(result.data.auth_token)
                })
                .catch((err) => {
                    alert("Такой пользователь уже существует");
                })
        }
    }
}
</script>
