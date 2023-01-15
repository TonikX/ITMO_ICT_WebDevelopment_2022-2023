import { defineStore } from 'pinia'
import { hotelsApi } from "@/api";

const useHotelsStore = defineStore('hotels',  {
  state: () => ({
    hotels: []
  }),

  actions: {
    async loadHotels() {
      const response = await hotelsApi.getAll()

      this.hotels = response.data

      return response
    }
  }
})

export default useHotelsStore
