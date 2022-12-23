import { defineStore } from 'pinia'
import { usersAPI } from '@/api'

const useUsersStore = defineStore('users', {
  state: () => ({
    user: {},
    token: null,
  }),

  actions: {
    setToken(token) {
      this.token = token || null
    },
    async fetchCurrentUser() {
      let response = null

      if (this.token) {
        response = await usersAPI.fetchCurrentUserInfo(this.token)
        this.user = response.data?.username ? response.data : {}
      }

      return this.user
    },
    async login(credentials) {
      const response = await usersAPI.login(credentials)

      this.token = response?.data?.auth_token || null
      if (this.token) {
        window.localStorage.setItem('fabiana-user', this.token)
      }

      return this.token
    },
    async signUp(user) {
      const response = await usersAPI.createNewUser(user)

      return response
    },
    async logout() {
      let response = null

      if (this.token) {
        response = await usersAPI.logout(this.token)
        if (response.status === 204) {
          window.localStorage.removeItem('fabiana-user')
          this.token = '';
          this.user = {};
        }
      }

      return response
    },
  }
})

export default useUsersStore
