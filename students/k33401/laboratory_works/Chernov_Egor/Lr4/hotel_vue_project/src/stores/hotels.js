import {defineStore} from 'pinia'
import {hotelsApi} from "@/api";

const useHotelsStore = defineStore('hotels', {
    state: () => ({
        hotels: [],
        hotel_room_types: [],
        rooms: [],
        room: []
    }),

    actions: {
        async loadHotels() {
            const response = await hotelsApi.getAll()

            this.hotels = response.data

            return response
        },
        async loadHotelRoomTypes(id) {
            const response = await hotelsApi.getHotelRoomTypes(id)

            this.hotel_room_types = response.data

            return response
        },
        async loadRooms(id) {
            const response = await hotelsApi.getRooms(id)

            this.rooms = response.data

            return response
        },
        async loadRoom(id) {
            const response = await hotelsApi.getRoom(id)

            this.room = response.data

            return response
        }
    }
})

export default useHotelsStore
