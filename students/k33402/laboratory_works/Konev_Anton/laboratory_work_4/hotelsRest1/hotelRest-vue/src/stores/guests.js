import {defineStore} from "pinia";
import {guestsAPI} from "@/api";

const useGuestsStore = defineStore('guests', {
    state: () => ({
        guests: []
    }),
    actions: {
        async getGuestsList() {
            const response = await guestsAPI.getAllGuests();
            this.guests = response.data;
            return response.data;
        },
        async sendBooking(data, token) {
            const response = await guestsAPI.addBooking(data, token);
            return response.data;
        },
        async getSelectedGuest(id) {
            const response = await guestsAPI.getGuestById(id);
            return response.data;
        },
        async sendClosed(id) {
            const response = await guestsAPI.closeBooking(id);
            return response.data;
        }
    }
})

export default useGuestsStore