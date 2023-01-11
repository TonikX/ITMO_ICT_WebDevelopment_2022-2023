import {defineStore} from 'pinia'
// импортируем API
import {cLientApi} from '@/api'

// создаём хранилище
const useClientStore = defineStore('clients', {
    state: () => ({
        clients: [],
    }),

    actions: {
        async getClients() {
            const response = await cLientApi.getAllClients()
            this.clients = response.data
            return response
        },

    }
})

export default useClientStore
