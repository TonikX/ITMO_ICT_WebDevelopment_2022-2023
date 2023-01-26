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
          <request-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import RequestTableCard from '@/components/data/RequestTableCard'

export default {
  name: 'Request',
  components: {
    NavDrawer,
    RequestTableCard
  }
}
</script>

<style scoped>

</style>
