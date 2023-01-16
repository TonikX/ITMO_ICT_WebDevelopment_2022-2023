import {defineStore} from 'pinia'
import {userAPI} from '../api'

const useUserStore = defineStore('user', {
    state: () => ({
        user: {},
        token: null,
    }),

    actions: {
        setToken(token) {
            this.token = token || null
        },
        async login(data) {
            const response = await userAPI.login(data)
            this.token = response?.data?.auth_token || null
            if (this.token) {
                localStorage.setItem("token", this.token)
            }
            return response
        },
        async register(user) {
            const response = await userAPI.register(user)

            return response
        },
        async logout() {
            let response = null

            if (this.token) {
                response = await userAPI.logout(this.token)
                if (response.status === 204) {
                    window.localStorage.removeItem('token')
                    this.token = '';
                    this.user = {};
                }
            }

            return response
        },
        async currentUserInfo() {
            let response = null

            if (this.token) {
                response = await userAPI.currentUserInfo(this.token)
                this.user = response.data?.username ? response.data : {}
            }

            return this.user
        },
    },

})

export default useUserStore