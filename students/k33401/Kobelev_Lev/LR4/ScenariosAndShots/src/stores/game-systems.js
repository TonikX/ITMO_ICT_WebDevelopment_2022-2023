import { defineStore } from 'pinia'
import { gameSystemsAPI } from "@/api";

const useGameSystemsStore = defineStore('gameSystems', {
    state: () => ({
        gameSystems: [],
        selectedGameSystems: []
    }),
    actions: {
        async loadGameSystems() {
            const response = await gameSystemsAPI.getAllGameSystems()

            this.gameSystems = response.data

            return response
        },
    }
})

export default useGameSystemsStore
