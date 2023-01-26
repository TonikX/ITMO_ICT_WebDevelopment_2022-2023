<template>
    <div class="card border-success mb-3" style="max-width: 18rem">
        <div class="card-header bg-transparent border-success">
            <router-link :to="'market/' + id">{{ title }}</router-link>
        </div>
        <div class="card-body text-success">
            <h5 class="card-title">{{ price }}$</h5>
            <img class="card-img" src="@/assets/chart.png" width="200" />
        </div>
        <div v-if="description" class="card-footer bg-transparent border-success">{{ description }}</div>
    </div>
</template>

<script>
export default {
    props: ["id", "title", "description"],
    name: "CryptoCard",
    data() {
        return {
            price: null,
        };
    },
    methods: {
        async fetchData() {
            this.axios
                .get(`http://127.0.0.1:8088/market/${this.id}/`)
                .then((res) => {
                    this.price = res.data.last_price;
                })
                .catch(() => null);
        },
    },
    async mounted() {
        await this.fetchData();
    },
};
</script>

<style>
.card-img {
    filter: blur(2px);
    -webkit-filter: blur(2px);
}
</style>
