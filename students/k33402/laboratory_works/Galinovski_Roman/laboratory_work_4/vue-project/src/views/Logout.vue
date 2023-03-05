<script>
export default {
  name: 'Logout',
  methods: {
    LogOut () {
      try {
        const token = localStorage.getItem('auth_token')
        if (token) {
          this.axios.defaults.headers.common.Authorization = `token ${token}`
        }
        localStorage.setItem('auth_token', '-1')
        this.axios.post('http://127.0.0.1:8000/auth/token/logout/').then(response => {
          console.log('SIGN OUT RESPONSE', response)
          this.$router.push({ name: 'home' })
        })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    this.Logout()
  }
}
</script>

<style scoped>
</style>