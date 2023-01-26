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
          <work-group-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import WorkGroupTableCard from '@/components/data/WorkGroupTableCard'

export default {
  name: 'WorkGroup',
  components: {
    NavDrawer,
    WorkGroupTableCard
  }
}
</script>

<style scoped>

</style>
