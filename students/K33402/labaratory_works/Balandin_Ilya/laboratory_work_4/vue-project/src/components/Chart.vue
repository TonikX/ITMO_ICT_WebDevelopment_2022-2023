<template>
  <div id="linechart_material" class="bg-secondary-own" style="height: 500px"></div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBazzarStore from "@/stores/bazzar";

export default {
  name: "Chart",
  props: {
    plot_rows: {
      required: true
    }
  },
  computed: {
    ...mapState(useBazzarStore, ['sellsInfo'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['loadSellsInfo']),
    drawChart: function () {
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Day');
      data.addColumn('number', 'Sales');

      data.addRows(this.plot_rows);

      var options = {
        height: 500,
        legend: {position: 'none'},
        lineWidth: 4,
      };
      var chart = new google.charts.Line(document.getElementById('linechart_material'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    }
  },
  mounted() {
    google.charts.load('current', {'packages': ['line']});
    google.charts.setOnLoadCallback(this.drawChart);
  }
}
</script>

<style scoped>

</style>