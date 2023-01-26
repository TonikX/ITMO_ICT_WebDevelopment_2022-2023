<template>
  <v-container>
    <v-row>
      <v-col cols="2">
        <v-card>
          <nav-drawer/>
        </v-card>
      </v-col>

      <v-col cols="10">
        <v-card>
          <client-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import ClientTableCard from '@/components/data/ClientTableCard'

export default {
  name: 'Client',
  components: {
    NavDrawer,
    ClientTableCard
  }
}
</script>

<style scoped>

</style>
