<template>
  <div class="container py-5">
    <div class="row row-cols-2">
      <div class="col-12 pb-3">
        <CurrencyChart :currency_coinlib_id="currency.coinlib_id"/>
      </div>
      <BuySellButtonsBlock :currency="currency" v-if="currency"/>
    </div>
  </div>
</template>

<script>
import $ from "jquery"

import CurrencyChart from "../components/CurrencyChart.vue";
import BuySellButtonsBlock from "../components/BuySellButtonsBlock.vue";

export default {
  name: "CurrencyView",
  data() {
    return {
      currency: {}
    }
  },
  created() {
    this.loadCurrency(this.$route.params.id)
  },
  methods: {
    loadCurrency(id) {
      $.ajax({
        url: `http://127.0.0.1:8000/currencies/${id}/`,
        type: "GET",
        success: (response) => {
          this.currency = response
        }
      })
    }
  },
  components: {
    CurrencyChart,
    BuySellButtonsBlock
  }
}
</script>
