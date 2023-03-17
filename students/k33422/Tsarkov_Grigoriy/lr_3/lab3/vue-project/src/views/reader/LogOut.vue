<script>
export default {
  name: 'LogOut',
  methods: {
    LogOut () {
      try {
          const token = sessionStorage.getItem('auth_token')
          if (token) {
            this.axios.defaults.headers.common["Authorization"] = `token ${String(token)}`
            sessionStorage.setItem('auth_token', '-1')
            this.$router.push({ name: 'home' })
            this.axios.post('http://127.0.0.1:8000/auth/token/logout/').then(response =>
            {console.log('SIGN OUT RESPONSE', response)
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
