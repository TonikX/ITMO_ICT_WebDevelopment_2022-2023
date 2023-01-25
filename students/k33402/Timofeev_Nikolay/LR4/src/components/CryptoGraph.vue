<template>
    <Line :data="data" :options="options" />
</template>

<script>
import { Line } from "vue-chartjs";

export default {
    components: { Line },
    name: "CryptoGraph",
    props: ["data"],
    data() {
        return {
            options: {
                responsive: true,
                maintainAspectRatio: false,
            },
        };
    },
};
</script>
