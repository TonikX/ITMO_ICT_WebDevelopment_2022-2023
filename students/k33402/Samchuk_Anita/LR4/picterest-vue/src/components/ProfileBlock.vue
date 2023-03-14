<template>
  <div class="d-flex align-items-center">
    <router-link to="/profile" class="mx-2">
      <img src="@/assets/img/avatar.png" alt="profile" width="30" height="30"/>
    </router-link>
    <svg v-if="isLoggedIn" @click="logout" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="black" class="bi bi-box-arrow-right ml-3" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
      <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'ProfileBlock',

  data () {
    return {
      isLoggedIn: false
    }
  },

  mounted () {
    if (localStorage.getItem('accessToken')) {
      this.isLoggedIn = true
    }
  },

  methods: {
    logout () {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('user')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>

</style>
