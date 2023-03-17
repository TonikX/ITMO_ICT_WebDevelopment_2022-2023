import { defineStore } from 'pinia'
import { event_api } from '@/api'

const eventsStore = defineStore('events',{
    state: () => ({
        events: [],
        category: '',
        city: '',
        event: {}
    }),

    actions: {
        async getEvents() {
            const response = await event_api.getEventsList();
            this.events = response.data;
            return response;
        },

        async getCertainEvent(id) {
            const response = await event_api.getCertainEvent(id)
            this.event = response.data;
            return response;
        },

        async getFilteredEventsByCategory(category) {
            const response = await event_api.getFilteredEventsByCategory(category);
            this.category = category;
            this.events = response.data;
            return response;
        },

        async getFilteredEventsByCity(city) {
            this.city = city;
            const response = await event_api.getFilteredEventsByCity(city);
            this.events = response.data;
            return response;
        },

        async getFilteredEventsByCategoryAndCity(category, city) {
            this.category = category;
            this.city = city;
            const response = await event_api.getFilteredEventsByCategoryAndCity(category, city);
            this.events = response.data;
            return response;
        }

    }
})

export default eventsStore