<template>
    <header
        class="container d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-4"
    >
        <a href="/" class="d-flex align-items-center col-md-auto mb-2 mb-md-0 text-dark text-decoration-none">
            <img src="img/logo.svg" width="288" height="33" alt="TimofeevInvest" class="logo" />
        </a>
        <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
            <li>
                <a href="/" class="nav-link active px-2 link-dark text-decoration-underline"
                    ><router-link to="/">Home</router-link></a
                >
            </li>
            <li>
                <router-link
                    to="/search"
                    class="nav-link px-2 link-dark"
                    data-bs-toggle="modal"
                    data-bs-target="#searchModal"
                >
                    <i class="bi bi-search-heart"></i>
                </router-link>
            </li>
            <li>
                <router-link to="/profile" class="nav-link px-2 link-dark"> <i class="bi bi-wallet2"></i> </router-link>
            </li>
            <li v-if="!user">
                <router-link to="/login" class="nav-link px-2 link-dark"
                    ><i class="bi bi-person-circle"></i>
                </router-link>
            </li>
            <span v-else>
                <li>
                    <p class="nav-link px-2 link-dark">
                        Welcome, {{ user.username }}! {{ user.balance }}$
                        <a class="btn btn-sm btn-primary" @click="logout">Exit</a>
                    </p>
                </li>
            </span>
        </ul>
    </header>
</template>

<script>
export default {
    name: "NavBar",
    data() {
        return {
            user: null,
        };
    },
    methods: {
        async getMeData(token) {
            await this.axios
                .get("http://127.0.0.1:8088/auth/users/me/", {
                    headers: {
                        Authorization: `Token ` + token,
                    },
                })
                .then((res) => {
                    this.user = res.data;
                })
                .catch(() => null);
        },
        async logout() {
            localStorage.clear();
            this.$router.go();
        },
    },
    async mounted() {
        const token = localStorage.getItem("token");
        if (token) {
            await this.getMeData(token);
        }
    },
};
</script>
