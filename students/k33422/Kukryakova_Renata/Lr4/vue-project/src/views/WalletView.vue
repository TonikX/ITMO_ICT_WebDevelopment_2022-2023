<template>
    <Header/>
    <Personal/>
    <br>
    <chart/>
</template>

<script>
import Header from "@/components/headers/Header.vue";
import Personal from "@/components/Personal.vue";
import {Chart} from "vue-tradingview-widgets";

export default {
  components: {
    Header,
    Personal,
    Chart
  }
}
</script>
