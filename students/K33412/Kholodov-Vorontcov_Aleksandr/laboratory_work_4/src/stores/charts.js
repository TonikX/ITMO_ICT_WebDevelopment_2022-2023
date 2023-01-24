import {defineStore} from "pinia";
import {chartsAPI} from "@/api";

const useChartsStore = defineStore('charts', {
    state: () => ({
        charts: []
    }),
    actions: {
        async loadCharts() {
            const response = await chartsAPI.getCharts()
            this.charts = response.data

            return response.data
        }
    }
})

export default useChartsStore
