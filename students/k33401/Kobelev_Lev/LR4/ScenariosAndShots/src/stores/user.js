import {defineStore} from "pinia";
import {authAPI} from "@/api";

export const useUserStore = defineStore("user", {
    state: () => ({
        authToken: null,
        username: null
    }),

    actions: {
        async fetchUser(authToken) {
            const response = await authAPI.fetchUser(authToken)
            const user = await response
            this.authToken = authToken
            this.username = user.data.username
        },
        async signUp(username, password, email) {
            await authAPI.signUp(username, password, email)

            return this.logIn(username, password)
        },
        async logIn(username, password) {
            const user = await authAPI.getAuthToken(username, password)
            return user
        },
        logOut() {
            this.authToken = null
            this.username = null
        }
    }
})

export default useUserStore
