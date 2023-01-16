<template>
    <AuthenticatedWrapComponent>
        <v-alert v-if="error" :text="error" type="error"></v-alert>
        <v-progress-circular
                v-if="!loaded"
                color="primary"
                indeterminate/>
        <div v-if="loaded">
            <h1>График продаж</h1>
            <div style="max-height:500px">
                <Bar
                        id="my-chart-id"
                        :data="chartData"
                        :options="chartOptions"
                />
            </div>
        </div>
    </AuthenticatedWrapComponent>
</template>

<script>
import AuthenticatedWrapComponent from "@/components/AuthenticatedWrapComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

import {Bar} from 'vue-chartjs'
import {BarElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, Title, Tooltip} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
	name: "Sales",
	components: {AuthenticatedWrapComponent, Bar},
	computed: {
		...mapStores(useAuthStore),
		chartData() {
			return {
				labels: this.sales.map(sale => sale.name),
				datasets: [{
					label: "Продано единиц товара",
					data: this.sales.map(sale => sale.sales__quantity__sum)
				}]
			}
		}
	},
	created() {
		this.authStore.init();
	},
	data: () => ({
		error: "",
		loaded: false,
		sales: null,
		chartOptions: {
			responsive: true
		}
	}),
	mounted() {
		axios
			.get("/sales")
			.then(response => {
				this.sales = response.data;
				console.log("response", this.sales);
			})
			.catch(error => {
				if (error.response.status === 401) { // unauthorized
					this.authStore.resetToken();
					this.$router.push({name: "SignIn"});
				} else {
					this.error = error.response?.data || error.message || "Что-то пошло не так";
					console.log(error)
				}
			})
			.finally(() => {
				this.loaded = true;
			})
	},
}
</script>
