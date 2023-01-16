import { defineStore } from 'pinia'
import { eventsAPI } from '../api'

const useEventsStore = defineStore('events', {
    state: () => ({
        events: [],
        categoryFilter: '',
        districtFilter: '',
        typeFilter: '',

        event: {}
    }),

    actions: {
        async fetchEvents() {
            const response = await eventsAPI.fetchEvents()
            this.events = response.data
            return response
        },

        async fetchEvent(id) {
            const response = await eventsAPI.fetchEvent(id)
            this.event = response.data
            return response
        },

        async fetchEventsByCategory(category) {
            this.categoryFilter = category === this.categoryFilter ? '' : category;
            const response = await eventsAPI.fetchEventsByCategory(this.categoryFilter)
            this.events = response.data
            return response
        },

        async fetchEventsByCategoryDistrictType(category, district, type_event) {
            this.categoryFilter = category === this.categoryFilter ? '' : category;
            this.districtFilter = district === this.districtFilter ? '' : district;
            this.typeFilter = type_event === this.typeFilter ? '' : type_event;
            const response = await eventsAPI.fetchEventsByCategoryDistrictType(this.categoryFilter, this.districtFilter, this.typeFilter)

            this.events = response.data
            return response
        }
    }
})

export default useEventsStore