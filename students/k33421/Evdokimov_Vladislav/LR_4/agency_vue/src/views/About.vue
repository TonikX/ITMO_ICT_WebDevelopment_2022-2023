<template>
  <v-container>
    <v-row>
      <v-col cols="2">
        <v-card>
          <nav-drawer v-if='auth'/>
        </v-card>
      </v-col>

      <v-col cols="10">
        <v-card>
          <h3>Программная система учёта "Луч-агенство"</h3>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
export default {
  name: 'About',
  components: {
    NavDrawer
  },
  computed: {
    auth () {
      return !!localStorage.getItem('token');
    }
  }
}

</script>

<style scoped>

</style>
