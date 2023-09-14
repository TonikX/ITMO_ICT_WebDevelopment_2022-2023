import {defineStore} from 'pinia'
import {userEventsApi, usersApi} from "@/api";


const useUsersStore = defineStore('users', {
    state: () => ({
        user: {},
        token: null,
        userEvents: []
    }),

    actions: {
        async CurrentUser() {
            let response = null

            if (this.token) {
                response = await usersApi.fetchCurrentUser(this.token)
                this.user = response.data?.username ? response.data : {}
                console.log(this.user)
            }
            return this.user
        },
        async login(credentials) {
            const response = await usersApi.login(credentials)

            this.token = response?.data?.auth_token || null
            if (this.token) {
                window.localStorage.setItem('user_token', this.token)
            }

            return this.token
        },
        async signUp(user) {
            return await usersApi.signUp(user)
        },
        async logout() {
            let response = null

            if (this.token) {
                response = await usersApi.logout(this.token)
                if (response.status === 204) {
                    window.localStorage.removeItem('user_token')
                    this.token = ''
                    this.user = {}
                    this.userEvents = []
                }
            }

            return response
        },

        async getUserEvents() {
            const response = await userEventsApi.getByUserId(this.user.id)

            this.userEvents = response.data
            console.log(this.userEvents)

            return response
        },

        async addUserEvent(data) {

            return await userEventsApi.enrollUser(data)
        }
    }
})

export default useUsersStore