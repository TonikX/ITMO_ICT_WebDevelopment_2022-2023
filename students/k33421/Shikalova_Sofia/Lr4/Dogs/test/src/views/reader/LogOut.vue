<script>
import axios from 'axios'
/* eslint-disable */
//Vue.prototype.$axios = axios
//import Vue from 'vue'

export default {
  name: 'LogOut',
  methods: {
    LogOut () {
      try {
        const token = sessionStorage.getItem('auth_token')
        if (token) {     
          const data = {}    
          console.log(token)
          //this.axios.defaults.headers.common.Authorization = `token ${token}`
          //console.log(this.axios)

          sessionStorage.setItem('auth_token', '-1')
          //console.log('h ' + token)
          axios.post('http://127.0.0.1:8000/auth/token/logout/', data, {
            headers: {
            'Authorization': `token ${token}` 
            }
          }).then(response => {
            console.log('SIGN OUT RESPONSE', response)
          // localStorage.removeItem('token')
          // this.$bus.$emit('logged', 'User logged out')
            this.$router.push({ name: 'home' })
        })
        }

      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    this.LogOut()
  }
}
</script>

<style scoped>
</style>
