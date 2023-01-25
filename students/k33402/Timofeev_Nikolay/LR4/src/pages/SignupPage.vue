<template>
    <div class="container">
        <nav-bar></nav-bar>
        <hr class="opacity-100 m-0" />
        <h1 class="text-center mt-3">Sign Up</h1>

        <form class="container d-flex justify-content-center" onsubmit="return false;">
            <div class="col-4">
                <div class="form-group">
                    <label for="usernameInput">Username</label>
                    <input
                        class="form-control"
                        id="usernameInput"
                        aria-describedby="emailHelp"
                        :value="username"
                        @input="(e) => (username = e.target.value)"
                    />
                </div>
                <div class="form-group">
                    <label for="emailInput">Email address</label>
                    <input
                        type="email"
                        class="form-control"
                        id="emailInput"
                        aria-describedby="emailHelp"
                        :value="email"
                        @input="(e) => (email = e.target.value)"
                    />
                </div>
                <div class="form-group">
                    <label for="passwordInput">Password</label>
                    <input
                        type="password"
                        class="form-control"
                        id="passwordInput"
                        :value="password"
                        @input="(e) => (password = e.target.value)"
                    />
                </div>
                <div class="d-flex justify-content-between mt-3">
                    <button type="submit" class="btn btn-primary" @click="signUp">Sign Up</button>
                    <div class="border-right pr-3 mr-3"></div>
                    <button type="button" class="btn btn-secondary">
                        <router-link class="text-white" to="/">Cancel</router-link>
                    </button>
                </div>
            </div>
        </form>

        <hr class="opacity-100" />
        <page-footer />
    </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import PageFooter from "@/components/PageFooter.vue";

import { useToast } from "vue-toastification";

export default {
    setup() {
        const toast = useToast();
        return { toast };
    },
    components: { NavBar, PageFooter },
    data() {
        return {
            username: "",
            email: "",
            password: "",
        };
    },
    methods: {
        async signUp() {
            if (!this.username || !this.email || !this.password) {
                this.toast.error('Enter credentials!')
                return
            }
            try {   
                await this.axios.post('http://localhost:8088/auth/users/', {
                    username: this.username,
                    password: this.password,
                    email: this.email,
                }, {})
            } catch (e) {
                this.toast.warning('An error occured, try later');
                return
            }
            this.$router.push('/');
            this.toast.success(`Welcome, ${this.username}! You may login with entered creadentials`)
        },
    },
};
</script>
