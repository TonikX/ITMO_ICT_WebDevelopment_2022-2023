<template>
    <body class="container">
        <nav-bar />
        <hr class="opacity-100 m-0" />

        <h1 class="text-center m-2">Find any listed currency:</h1>

        <div class="container d-flex justify-content-center col-8">
            <div class="mb-2 input-group">
                <input type="text" class="form-control" placeholder="USDT" @input="(e) => (query = e.target.value)" />
                <button class="btn btn-outline-primary" @click="searchCrypto" type="button" id="button-addon2">
                    Lookup
                </button>
                <button
                    v-if="retrieveLast"
                    class="btn btn-outline-info"
                    @click="getLastSearchRes"
                    type="button"
                    id="button-addon2"
                >
                    Last
                </button>
            </div>
        </div>

        <section v-if="results" class="container d-flex justify-content-center py-2">
            <div class="list-group col-8">
                <router-link
                    v-for="result in results"
                    :key="result"
                    :to="'/market/' + result.id"
                    href="#"
                    class="list-group-item list-group-item-action"
                >
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{ result.name }}</h5>
                        <small class="text-muted">{{ result.last_price }}$</small>
                    </div>
                    <p class="mb-1">{{ result.description }}</p>
                    <small class="text-muted">{{ result.group }}. {{ result.label }}</small>
                </router-link>
            </div>
        </section>

        <hr class="opacity-100 m-0" />
        <page-footer />
    </body>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    components: { NavBar, PageFooter },
    name: "SearchPage",
    data() {
        return {
            query: "",
            results: [],
        };
    },
    methods: {
        async searchCrypto() {
            this.axios.get(`http://127.0.0.1:8088/market/?search=${this.query}`).then((res) => {
                this.results = res.data;
            });
            await this.saveSearch(this.query);
        },
        async retrieveLast() {
            return localStorage.getItem("lastSearch") || null;
        },
        async saveSearch() {
            localStorage.setItem("lastSearch", this.query);
        },
        async getLastSearchRes() {
            this.query = await this.retrieveLast();
            await this.searchCrypto();
        },
    },
};
</script>
