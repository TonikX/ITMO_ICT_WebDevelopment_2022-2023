import { defineStore } from 'pinia'
// импортируем API
import {loginApi} from "@/api";

// создаём хранилище
const useUserStore = defineStore('user', {

    actions: {
        async login(data) {
            const response = await loginApi.login(data)
            localStorage.setItem("token", response.data.auth_token)
            return response
        }
    },

})

export default useUserStore
