import { defineStore } from 'pinia'
import { loginApi } from '@/api'

const useLoginStore = defineStore('users', {
  state: () => ({
    users: []
  }),

  actions: {
    async userLogin(data) {
      const response = await loginApi.userLogin(data)

      this.users = response.data

      return response
    }
  }
})

export default useLoginStore