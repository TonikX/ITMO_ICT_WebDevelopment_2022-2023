<template>
  <apexchart type="line" :value="target" :options="chartOptions" :series="series"></apexchart>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
  name: 'Chart',
  components: {
    apexcharts: VueApexCharts,
  },
  props: {
    target: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chartOptions: {
        chart: {
          id: 'basic-bar'
        },
        xaxis: {
          categories: []
        }
      },
      series: [{
        name: '',
        data: []
      }]
    }
  },
  computed: {},
  watch: {
    target() {
      for (let i = 0; i < this.target.length; i++) {
        this.chartOptions.xaxis.categories[i] = this.target[i][0]
        this.series[0].data[i] = this.target[i][1].toFixed(5)
      }
    }
  }
}
</script>