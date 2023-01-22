<template>
    <div>
        <headerBlock />
        <bodyBlock />
      <Chart />
      <CryptoMarket style="height: 340px;"/>
    </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import headerBlock from '../components/header.vue';
import bodyBlock from '../components/body.vue';
import style from '../assets/main.css';

import {Chart,CryptoMarket, Snaps, Screener} from 'vue-tradingview-widgets';
export default {
    name: "Mainpage",
    components: {headerBlock, bodyBlock,Chart,
      CryptoMarket,
      Screener,
      Snaps}
};

</script>
