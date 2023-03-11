<template>
  <div class="container w-75">
    <div class="row d-flex justify-content-between align-items-center mb-4">
      <h1 class="col col-8 m-5">Sales</h1>
    </div>
    <chart :plot_rows="sellsInfo"></chart>

    <div class="mt-4">
      <table class="table bg-secondary-own text-main-own">
        <thead>
        <tr>
          <th scope="col">Date</th>
          <th scope="col">Product</th>
          <th scope="col">Platform</th>
          <th scope="col">Username</th>
          <th scope="col">Price</th>
        </tr>
        </thead>
        <tbody id="salesTable">
        <tr v-for="sell in row">
          <th scope="row">{{ sell.date }}</th>
          <td>{{ sell.name }}</td>
          <td>{{ sell.platform }}</td>
          <td>{{ sell.username }}</td>
          <td>{{ sell.price }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBazzarStore from "@/stores/bazzar";
import Chart from "@/components/Chart.vue";

export default {
  name: "Sells",
  components: {Chart},
  computed: {
    ...mapState(useBazzarStore, ['sells', 'sellsInfo'])
  },
  data() {
    return {
      row: []
    }
  },
  methods: {
    ...mapActions(useBazzarStore, ['loadSells', 'loadSellsInfo'])
  },
  mounted() {
    const response = this.loadSells()
    for (const s of this.sells) {
      this.row.push({
        date: s.date,
        name: s['product'].game.name,
        username: s['username'],
        platform: s['product']['platform'].name,
        price: s['product'].price
      })
    }
    const response2 = this.loadSellsInfo()
  }
}
</script>