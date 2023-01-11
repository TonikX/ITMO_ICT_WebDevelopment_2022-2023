import { defineStore } from 'pinia'
import { userEventsApi } from '@/api'

const useUserEventsStore = defineStore('userEvents', {
	state: () => ({
		userEvents: []
	}),

	actions: {
		async addUserEvents(data) {
			const response = await userEventsApi.createUserEvent(data);

			this.userEvents = response.data;
			
			return response
		},

		async getUserEventsById(id) {
			const response = await userEventsApi.getById(id)
			console.log(response)
			return response
		},

		async deleteCardById(id) {
			const response = await userEventsApi.deleteById(id);

			return response
		}
	}


})

export default useUserEventsStore