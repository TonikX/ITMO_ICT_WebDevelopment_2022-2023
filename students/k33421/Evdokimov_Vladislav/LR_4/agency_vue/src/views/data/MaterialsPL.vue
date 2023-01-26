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
          <materials-p-l-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import MaterialsPLTableCard from '@/components/data/MaterialsPLTableCard'

export default {
  name: 'MaterialsPL',
  components: {
    NavDrawer,
    MaterialsPLTableCard
  }
}
</script>

<style scoped>

</style>
