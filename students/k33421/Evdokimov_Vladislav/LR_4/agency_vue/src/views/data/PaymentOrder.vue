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
          <payment-order-table-card/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import PaymentOrderTableCard from '@/components/data/PaymentOrderTableCard'

export default {
  name: 'PaymentOrder',
  components: {
    NavDrawer,
    PaymentOrderTableCard
  }
}
</script>

<style scoped>

</style>
