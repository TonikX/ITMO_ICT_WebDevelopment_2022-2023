import {defineStore} from 'pinia'
import {userApi} from "@/api";

const useUserStore = defineStore('user', {
    state: () => ({
        users: [],
        tokens: [],
        accUser: []
    }),

    actions: {
        async loadUsers(token) {
            const response = await userApi.getUsers(token)

            this.users = response.data

            return response
        },
        async loadUserToken(username, password) {
            const response = await userApi.login(username, password)

            this.tokens = response.data

            return response
        },
        async loadAccUser(token, id) {
            const response = await userApi.getAccUser(token, id)

            this.accUser = response.data

            return response
        },
        async updateAccUser(token, id) {
            const response = await userApi.putAccUser(token, id)

            this.accUser = response.data

            return response
        }
    }
})

export default useUserStore
