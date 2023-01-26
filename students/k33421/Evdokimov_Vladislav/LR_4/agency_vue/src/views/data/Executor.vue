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
          <executor-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import ExecutorTableCard from '@/components/data/ExecutorTableCard'

export default {
  name: 'Executor',
  components: {
    NavDrawer,
    ExecutorTableCard
  }
}
</script>

<style scoped>

</style>
