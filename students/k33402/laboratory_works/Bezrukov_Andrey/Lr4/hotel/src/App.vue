<template>
  <v-app>
    <v-app-bar app color="teal" dark>
      <div class="d-flex align-center">
        <h1 class="headline">My hotel</h1>
      </div>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn color="white" plain @click="logout">
          Logout
        </v-btn>
        <v-btn color="white" plain @click="rooms">
          Rooms
        </v-btn>
        <v-btn color="white" plain @click="guests">
          Guests
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <router-view />
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  }),

  methods: {
    logout () {
      localStorage.removeItem('auth_token')
      this.$router.push({ name: 'Login' })
    },
    guests () {
      this.$router.push({ name: 'Guests' })
    },
    rooms () {
      this.$router.push({ name: 'Rooms' })
    }
  }
}
</script>
