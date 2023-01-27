import {defineStore} from "pinia";
import {roomAPI} from "@/api";

const useRoomsStore = defineStore('rooms', {
    state: () => ({
        rooms: []
    }),
    actions: {
        async loadAllRooms() {
            const response = await roomAPI.getRooms();
            this.rooms = response.data;
            return response.data
        },

        async loadFreeRooms() {
            const response = await roomAPI.getFreeRooms();
            return response.data
        },
    }

})

export default useRoomsStore