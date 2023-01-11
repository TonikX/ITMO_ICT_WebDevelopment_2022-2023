import { defineStore } from 'pinia' 
import { calendarEventsApi, cardApi } from '@/api' 
 
const useCalendarEventsStore = defineStore('calendarEvents', { 
  state: () => ({ 
    calendarEvents: [], 
    selectedEvent: { title: '', date: '', description: '', id: "" } 
  }), 
 
  actions: { 
    async loadCalendarEvents() { 
      const response = await calendarEventsApi.getAll(); 
      const response2 = await cardApi.getAll(); 
 
      const jsonResponse = Array.from(response2.data); 
 
      this.calendarEvents = response.data 
 
      response2.data.forEach((item) => { 
        this.calendarEvents.push(item) 
      }) 
       
      console.log(this.calendarEvents) 
 
      return response 
    }, 
 
    async loadEventById(id) { 
      this.selectedEvent = { title: '', date: '', description: '', id: '' } 
 
      // const response = await calendarEventsApi.getById(id) 
      const response = await cardApi.getById(id) 
 
      this.selectedEvent = response.data 
 
      return response 
    }, 
 
    async createEvent(data) { 
      const response = await calendarEventsApi.create(data) 
 
      return response 
    }, 
 
    async deleteEvent(id) { 
      const response = await calendarEventsApi.deleteEv(id) 
 
      return response 
    } 
  } 
}) 
 
export default useCalendarEventsStore