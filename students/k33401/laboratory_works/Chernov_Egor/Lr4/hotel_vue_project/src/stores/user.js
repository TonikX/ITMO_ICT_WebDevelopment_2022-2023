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
        async updateAccUser(token, id, username, firstName, lastName, email, phoneGuest, passportGuest, phoneEmployee, positionEmployee) {
            const response = await userApi.putAccUser(token, id, username, firstName, lastName, email, phoneGuest, passportGuest, phoneEmployee, positionEmployee)

            this.accUser = response.data

            return response
        },
        async deleteUser(token, id, currentPassword) {
            await userApi.deleteUser(token, id, currentPassword)
        },
        async createUser(username, email, password) {
            const response = await userApi.createUser(username, email, password)

            this.accUser = response.data

            return response
        },
    }
})

export default useUserStore
