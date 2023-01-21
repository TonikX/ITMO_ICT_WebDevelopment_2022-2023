import {defineStore} from "pinia";
import {userAPI} from "@/api";

const useUsersStore = defineStore('users', {
    state: () => ({
        user: {},
        token: null,
    }),
    actions: {
        async signUp(user) {
            const response = await userAPI.createNewUser(user);
            return response.data;
        },

        async onLogin(credentials) {
            const response = await userAPI.login(credentials)
            this.user = {username: credentials.username, password: credentials.password}
            this.token = response.data.auth_token
            return response
        },

        async fetchUser() {
            if (this.token) {
                const response = await userAPI.fetchCurrentUserInfo(this.token)
                return response.data
            }
        },

        async onLogout() {
            if (this.token) {
                const response = await userAPI.logout(this.token)
                this.token = null;
                this.user = {}
                return response.data
            }
        },

        async getAdmin(id) {
            if (this.token) {
                const response = await userAPI.getAdminById(id, this.token)
                return response.data
            }
        }
    }

})

export default useUsersStore