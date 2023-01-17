<template>
  <div>
    {{currency.name}}
  </div>
</template>

<script>
import $ from "jquery"

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
  }
}
</script>

<style scoped>

</style>