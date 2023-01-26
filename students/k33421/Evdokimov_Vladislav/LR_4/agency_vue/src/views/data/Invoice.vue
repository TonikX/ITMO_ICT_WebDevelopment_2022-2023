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
          <invoice-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import InvoiceTableCard from '@/components/data/InvoiceTableCard'

export default {
  name: 'Invoice',
  components: {
    NavDrawer,
    InvoiceTableCard
  }
}
</script>

<style scoped>

</style>
