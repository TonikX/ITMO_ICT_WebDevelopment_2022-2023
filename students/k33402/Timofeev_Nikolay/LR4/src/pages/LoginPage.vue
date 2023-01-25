<template>
    <div class="container">
        <nav-bar></nav-bar>
        <hr class="opacity-100 m-0" />
        <h1 class="text-center mt-3">Login</h1>

        <form class="container d-flex justify-content-center" onsubmit="return false;">
            <div class="col-4">
                <div class="form-group">
                    <label for="emailInput">Username</label>
                    <input
                        class="form-control"
                        id="emailInput"
                        :value="username"
                        @input="(e) => (username = e.target.value)"
                    />
                    <p class="lead" v-if="err">{{ err }}</p>
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
                    <button @click="loginUser" type="button" class="btn btn-primary">Login</button>
                    <div class="border-right pr-3 mr-3"></div>
                    <button type="button" class="btn btn-secondary">
                        <router-link class="text-white" to="/signup">Sign Up</router-link>
                    </button>
                </div>
            </div>
        </form>

        <hr class="opacity-100" />
        <page-footer />
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    components: { NavBar, PageFooter },
    data() {
        return {
            username: "",
            password: "",
            err: "",
        };
    },
    methods: {
        loginUser() {
            this.err = "";
            this.axios
                .post("http://127.0.0.1:8088/auth/token/login/", {
                    username: this.username,
                    password: this.password,
                })
                .then((resp) => {
                    localStorage.setItem("token", resp.data.auth_token);
                    this.$router.push("/");
                })
                .catch((e) => {
                    this.err = "Oops... Try again!";
                    console.log(e);
                    this.username = "";
                    this.password = "";
                });
        },
    },
};
</script>
