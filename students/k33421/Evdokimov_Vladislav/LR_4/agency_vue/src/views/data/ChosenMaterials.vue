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
          <chosen-materials-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import ChosenMaterialsTableCard from '@/components/data/ChosenMaterialsTableCard'

export default {
  name: 'ChosenMaterials',
  components: {
    NavDrawer,
    ChosenMaterialsTableCard
  }
}
</script>

<style scoped>

</style>
