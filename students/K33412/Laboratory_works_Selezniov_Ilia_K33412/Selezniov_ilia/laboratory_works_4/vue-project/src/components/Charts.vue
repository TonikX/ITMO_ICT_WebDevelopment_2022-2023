<template>
  <section class="container w-100 pt-4">
    <div class="d-flex w-25 mb-5 justify-content-between search-section">
      <div class="form d-flex">
        <search-input v-model="search" @send-search="getCharts" style="width: 100px;"/>
      </div>
    </div>
    <div class="d-flex">
      <div class="chart-section" style="height: 500px; width: fit-content; overflow-y: scroll; padding-top: 20px">
        <charts :charts="charts" @render-event="setTarget"/>
      </div>
      <div class="d-flex flex-column align-items-center w-75">
        {{ name }}
        <ChartField class="w-100" :target="target"/>
      </div>

    </div>

  </section>
</template>

<script>
import Charts from "@/components/chart/ChartsList.vue";
import {mapActions} from "pinia";
import useChartsStore from "@/stores/charts";
import useCoinsStore from "@/stores/coins";
import ChartField from "@/components/chart/ChartField.vue";

export default {
  name: 'Chart',
  components: {
    ChartField,
    Charts,
  },
  data() {
    return {
      charts: [],
      search: '',
      target: {},
      name: '',
    }
  },
  methods: {
    ...mapActions(useChartsStore, ['loadCharts']),
    ...mapActions(useCoinsStore, ["loadCoinsList"]),
    async getCharts() {
      const current = await this.loadCharts();
      const data = await this.loadCoinsList(this.search);
      this.charts = this.mergeChartWithCoin(current, data)
    },
    mergeChartWithCoin(current, data) {
      let res = [];
      let prices = [];
      for (let i = 0; i < current.length; i++) {
        for (let j = 0; j < data.length; j++) {
          if (current[i].id === data[j].id) {
            res.push(data[j])
            prices.push(current[i].prices)
          }
        }
      }

      for (let k = 0; k < res.length; k++) {
        res[k].prices = prices[k];
      }

      return res
    },
    setTarget(id) {
      const res = JSON.parse(JSON.stringify(this.charts.filter(x => x.id === id)));
      this.name = res[0].name
      this.target = res[0].prices;
    }
  },
  mounted() {
    this.getCharts()
  }
}
</script>

<style>

</style>