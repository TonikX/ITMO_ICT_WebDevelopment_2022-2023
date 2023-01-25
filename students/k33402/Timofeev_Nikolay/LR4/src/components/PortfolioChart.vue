<template>
    <Pie :options="options" :data="data"></Pie>
</template>

<script>
import { Pie } from "vue-chartjs";

export default {
    name: "PieChart",
    components: { Pie },
    props: {
        data: {
            type: Array,
            required: true,
        },
    },
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
