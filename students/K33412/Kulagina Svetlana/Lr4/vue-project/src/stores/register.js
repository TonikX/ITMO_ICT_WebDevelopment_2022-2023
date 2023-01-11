import { defineStore } from 'pinia' 
import { registerApi } from '@/api' 
 
const useRegisterStore = defineStore('users', { 
  state: () => ({ 
    users: [] 
  }), 
 
  actions: { 
    async userRegister(data) { 
      const response = await registerApi.userRegister(data) 
 
      this.users = response.data 
 
      return response 
    } 
  } 
}) 
 
export default useRegisterStore