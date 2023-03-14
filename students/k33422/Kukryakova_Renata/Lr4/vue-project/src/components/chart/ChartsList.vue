<template>
  <div class="wrapper d-flex" v-for="chart in charts">
    <button :id="chart.id" class="btn btn-light d-flex justify-content-between align-items-center mb-1"
            style="width: 250px; border: 1px solid"
            @click="renderEvent(chart.id)">
      <div class="d-flex align-items-center ">
        <img :src="chart.image" alt="" style="width: 30px; height: 30px"
             class="rounded-circle"/>
        <div class="ms-2 d-flex flex-column">
          <p class="fw-bold mb-0 d-flex">{{ chart.name }}</p>
          <p class="text-muted d-flex mb-0">{{ chart.symbol.toUpperCase() }}</p>
        </div>
      </div>
      <div class="d-flex ">
        <svg class="draw-chart" style="width: 30px; height: 30px">
          <use xlink:href="#chart">
          </use>
        </svg>
      </div>
    </button>
  </div>
</template>

<script>
export default {
  props: {
    charts: {
      type: Array,
      required: true
    }
  },
  emits: ['renderEvent'],
  data() {
    return {
      chart: {
        id: Number,
        name: String,
        symbol: String,
      },
    }
  },
  methods: {
    renderEvent(id) {
      this.$emit('renderEvent', id)
    }
  }
}
</script>

