<template>
    <body class="container">
        <nav-bar />
        <hr class="opacity-100 m-0" />

        <p class="lead text-center py-1 my-1">My Portfolio</p>
        <section class="px-4 py-5 my-5">
            <span class="row align-content-center">
                <span class="col">
                    <portfolio-chart v-if="graphData.length != 0" :data="graphData"/>
                </span>

                <span class="d-flex col justify-content-center">
                    <div class="card" style="width: 30rem">
                        <div class="card-header">Your assets</div>
                        <ul class="list-group">
                            <li
                                v-for="asset in assets"
                                :key="asset"
                                class="list-group-item d-flex justify-content-between align-items-center"
                            >
                                {{ asset.meta }}
                                <span class="badge bg-primary rounded-pill">{{ asset.amount }}</span>
                            </li>
                        </ul>
                    </div>
                </span>
            </span>
        </section>

        <hr class="opacity-100 m-0" />
        <page-footer />
    </body>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";
import PortfolioChart from "@/components/PortfolioChart.vue";

export default {
    components: { NavBar, PageFooter, PortfolioChart },
    name: "PortfolioPage",
    data() {
        return {
            assets: [],
            graphData: [],
        };
    },
    async mounted() {
        await this.getPortfolio();
    },
    methods: {
        async getPortfolio() {
            const assets = await this.axios.get(`http://localhost:8088/assets/`, {
                headers: {
                    Authorization: `Token ` + localStorage.getItem("token"),
                },
            });
            this.assets = assets.data.assets;
            this.prepareData(assets.data.assets)
            return assets.data.assets
        },
        prepareData(assets) {
            const labels = [];
            const datasets = [];

            for (const obj of Object.entries(assets)) {
                labels.push(obj[1].meta);
                datasets.push(obj[1].amount);
            }

            this.graphData = {
                labels,
                datasets: [
                    {
                        label: "Amount",
                        backgroundColor: "#f87979",
                        data: datasets,
                    },
                ],
            };
        }
    },
};
</script>
