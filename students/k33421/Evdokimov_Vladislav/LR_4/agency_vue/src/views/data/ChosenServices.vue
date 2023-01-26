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
          <chosen-services-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import ChosenServicesTableCard from '@/components/data/ChosenServicesTableCard'

export default {
  name: 'ChosenServices',
  components: {
    NavDrawer,
    ChosenServicesTableCard
  }
}
</script>

<style scoped>

</style>
