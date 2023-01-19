<template>
  <WelcomeSection/>
  <section>
    <div class="container py-5">
      <div class="d-flex justify-content-center pb-5">
        <h2>Купить криптовалюту</h2>
      </div>

      <CurrenciesList :currencies="currencies"/>

      <div class="d-flex justify-content-center pt-4">
        <div tabindex="0">
          <router-link to="/market" class="link-side">
            Посмотреть больше
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import $ from "jquery"

import WelcomeSection from "../components/WelcomeSection.vue";
import CurrenciesList from "../components/CurrenciesList.vue";

export default {
  name: "WelcomeView",
  components: {
    WelcomeSection,
    CurrenciesList
  },
  data() {
    return {
      currencies: []
    }
  },
  created() {
    this.loadPopularCurrencies()
  },
  methods: {
    loadPopularCurrencies() {
      $.ajax({
        url: "http://127.0.0.1:8000/currencies/popular/",
        type: "GET",
        success: (response) => {
          this.currencies = response
        }
      })
    }
  }
}
</script>

<style scoped>

</style>