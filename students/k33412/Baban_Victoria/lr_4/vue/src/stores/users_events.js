import {defineStore} from 'pinia'
import {userEventsAPI} from '../api'

const useUserEventsStore = defineStore('user_events', {
  state: () => ({
    userEvents: [],
  }),

  actions: {
    async fetchUsersEvents(token) {
      const response = await userEventsAPI.fetchUsersEvents(token)

      this.userEvents = response.data.user_events
      return response
    },
    async addUsersEvents(event, token) {
      const response = await userEventsAPI.addUsersEvents( {event}, token)
      return response
    },
    async removeUsersEvent(id, token) {
      const response = await userEventsAPI.removeUsersEvent(id, token)
      return response
    },
  }
})

export default useUserEventsStore