import { defineStore } from 'pinia'
import { scenariosAPI } from "@/api";

const useScenariosStore = defineStore('scenarios', {
    state: () => ({
        scenarios: [],
        selectedScenario: null,
    }),

    actions: {
        async loadScenarios(authToken) {
            const response = await scenariosAPI.getAllScenarios(authToken)

            this.scenarios = response.data

            return response
        },
        async filterScenarios(params) {
            const response = await scenariosAPI.getFilteredScenarios(params)

            this.scenarios = response.data

            return response
        },
        sortScenarios(key, asc) {
            if (asc) {
                this.scenarios.sort((a, b) => (a[key] > b[key]) ? 1 : ((b[key] > a[key]) ? -1 : 0))
            }
            else {
                this.scenarios.sort((b, a) => (a[key] > b[key]) ? 1 : ((b[key] > a[key]) ? -1 : 0))
            }
        },
        async likeScenario(id, authToken) {
            const response = await scenariosAPI.likeScenario(id, authToken)

            return response
        },
        async loadScenarioById(id) {
            const response = await scenariosAPI.getScenarioById(id)

            this.selectedScenario = response.data

            return response
        },
        async createScenarioReview(text, id, authToken) {
            const response = await scenariosAPI.createScenarioReview(text, id, authToken)

            return response
        }
    }
})

export default useScenariosStore
