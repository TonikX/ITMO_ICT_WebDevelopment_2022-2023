import {defineStore} from 'pinia'
// импортируем API
import {roomsApi} from '@/api'

// создаём хранилище
const useRoomsStore = defineStore('rooms', {
    state: () => ({
        rooms: [],
    }),

    actions: {
        async loadRooms() {
            const response = await roomsApi.getAllRooms()
            this.rooms = response.data
            return response
        },

        async sortRooms(data) {
            const response = await roomsApi.sortRooms(data)
            this.rooms = response.data
            return response
        },
    }
})

export default useRoomsStore
