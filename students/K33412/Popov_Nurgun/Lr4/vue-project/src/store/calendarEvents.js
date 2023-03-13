import { defineStore } from 'pinia'
import { calendarEventsApi } from '@/api'

const useCalendarEventsStore = defineStore('calendarEvents', {
  state: () => ({
    calendarEvents: [],
    selectedEvent: { title: '', date: '', description: '' }
  }),

  actions: {
    async loadCalendarEvents() {
      const response = await calendarEventsApi.getAll()

      this.calendarEvents = response.data

      return response
    },

    async loadEventById(id) {
      this.selectedEvent = { title: '', date: '', description: '' }

      const response = await calendarEventsApi.getById(id)

      this.selectedEvent = response.data

      return response
    },

    async createEvent(data) {
      const response = await calendarEventsApi.create(data)

      return response
    }
  }
})

export default useCalendarEventsStore