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
          <services-p-l-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import ServicesPLTableCard from '@/components/data/ServicesPLTableCard'

export default {
  name: 'ServicePL',
  components: {
    NavDrawer,
    ServicesPLTableCard
  }
}
</script>

<style scoped>

</style>
