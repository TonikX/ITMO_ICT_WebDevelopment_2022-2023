<template>
  <v-app>
    <div>
      <v-toolbar dense
                 dark
                 color="blue"
      >

        <v-toolbar-title @click="goToHome" style="cursor: pointer">Hotel by Paul Alekseev</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn color="white" plain @click="goToRooms">
            Rooms
          </v-btn>
          <v-btn color="white" plain @click="goToGuests">
            Guests
          </v-btn>
          <v-btn color="white" plain @click="goToRegistration">
            Register
          </v-btn>
        </v-toolbar-items>
        <v-btn color="white" plain @click="logout">
          Exit
        </v-btn>
      </v-toolbar>
    </div>
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>

</template>

<script>
export default {
  name: 'App',
  data: () => ({}),
  methods: {
    logout () {
      localStorage.removeItem('auth_token')
      this.$router.push({ name: 'Login' })
    },
    goToGuests () {
      this.$router.push({ name: 'Guests' })
    },
    goToRooms () {
      this.$router.push({ name: 'Rooms' })
    },
    goToRegistration () {
      this.$router.push({ name: 'Registration' })
    },
    goToHome () {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>
