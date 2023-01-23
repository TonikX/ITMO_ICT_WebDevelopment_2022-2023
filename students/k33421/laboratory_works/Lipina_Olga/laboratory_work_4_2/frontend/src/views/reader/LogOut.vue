<script>
export default {
  name: 'LogOut',
  methods: {
    LogOut () {
      try {
        const token = localStorage.getItem('auth_token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        localStorage.setItem('auth_token', '-1')
        // console.log('h ' + token)
        this.axios.post('http://127.0.0.1:8000/auth/token/logout/').then(response => {
          console.log('SIGN OUT RESPONSE', response)
          // localStorage.removeItem('token')
          // this.$bus.$emit('logged', 'User logged out')
          this.$router.push({ name: 'home' })
        })
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
