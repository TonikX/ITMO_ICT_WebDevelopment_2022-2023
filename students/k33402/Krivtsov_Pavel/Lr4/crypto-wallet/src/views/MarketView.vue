<template>
  <section>
    <div class="container pt-5 pb-3">
      <h1>
        Рынок криптовалюты
      </h1>
    </div>

    <hr class="featurette-divider">

    <CurrencyFiltersBlock :baseURL="baseURL" @response="(loadURL) => loadCurrencies(loadURL)" />

    <div class="container py-5">
      <CurrenciesList :currencies="currencies"/>
    </div>
  </section>
</template>

<script>
import $ from "jquery"

import CurrenciesList from "../components/CurrenciesList.vue";
import CurrencyFiltersBlock from "../components/CurrencyFiltersBlock.vue";

export default {
  name: "MarketView",
  data() {
    return {
      currencies: [],
      baseURL: 'http://127.0.0.1:8000/currencies/'
    }
  },
  created() {
    this.loadCurrencies(this.baseURL)
  },
  methods: {
    loadCurrencies(url) {
      $.ajax({
        url: url,
        type: "GET",
        success: (response) => {
          this.currencies = response
        }
      })
    }
  },
  components: {
    CurrenciesList,
    CurrencyFiltersBlock
  }
}
</script>
