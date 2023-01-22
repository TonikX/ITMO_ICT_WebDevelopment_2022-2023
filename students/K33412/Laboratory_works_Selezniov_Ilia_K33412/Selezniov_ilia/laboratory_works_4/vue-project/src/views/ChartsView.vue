<template>
  <Header/>
  <Chart />
</template>
<script>
import Header from "@/components/headers/Header.vue";
import {Chart} from 'vue-tradingview-widgets';
export default {
  components: {
    Header,
    Chart
  }
}
</script>