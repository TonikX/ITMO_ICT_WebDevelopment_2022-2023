import {defineStore} from 'pinia'
import { user_api} from '@/api'

const userStore = defineStore('users', {
    state: () => ({
        user: {},
        authToken: null,
        userEnrollments: []
    }),

    actions: {
        async login(data) {
            const response = await user_api.login(data)
            this.authToken = response?.data?.auth_token || null
            if (this.token) {
                localStorage.setItem('authToken', this.authToken)
            }   
            return response
        },

        async addNewUser(data) {
            const response = await user_api.sign_up(data)
            console.log(response.data)
            this.user = response.data
            localStorage.setItem('user', response.data.id)
            return response
        },

        async logout() {
            try{
            const response = await user_api.logout(this.authToken)
            }catch(e){
                console.log(e.response)
            }
            this.user = {}
            this.authToken = null
            this.userEnrollments = []
            localStorage.removeItem("authToken")
            localStorage.removeItem("user")
        },

        async get_user(authToken) {
            const response = await user_api.get_user_info(this.authToken)
            localStorage.setItem('user', response.data['id'])
            this.get_user_info(response.data.id)
            return response
        },
        async get_user_info(id){
            const response = await user_api.get_user_profile(id)
            this.user = response.data
            console.log(this.user)
        }
    }
})

export default userStore