<template>
  <div class="row row-cols-1 g-4">
    <div class="col">
      <div v-for="currency in currencies" v-bind:key="currency" class="card shadow-sm my-3">
        <router-link :to="'/currency/' + currency.id" class="btn btn-light card-bg-color text-left">
          <div class="row d-flex align-items-center px-4">

            <div class="col-5 col-sm-3 col-xl-1 col-lg-2 d-flex justify-content-center">
              <img :src="currency.image" style="max-height:100px; max-width:100px;" class="img rounded-start"
                   alt="{{currency.name}}">
            </div>

            <div class="col-7 col-sm-9 col-xl-11 col-lg-10">
              <div class="card-body">
                <h5 class="card-title card-main-color">{{ currency.name }}</h5>

                <div class="row row-cols-1 row-cols-lg-2 row-cols-xl-4 pb-3">
                  <div class="col">
                    <p class="card-main-color"><small class="card-muted-color">1 {{ currency.abbreviation }}:</small>
                      ${{ parseFloat(currency.price) }}</p>
                  </div>
                  <div class="col">
                    <p class="card-main-color"><small class="card-muted-color">Всего в обращении:</small>
                      {{ formatNumber(currency.count, 2) }}</p>
                  </div>
                  <div class="col">
                    <p :class="defineChangesColor(currency.daily_changes)"><small
                        class="card-muted-color">24 часа:</small> {{ currency.daily_changes }}%</p>
                  </div>
                  <div class="col">
                    <p :class="defineChangesColor(currency.weekly_changes)"><small
                        class="card-muted-color">7 дней:</small> {{ currency.weekly_changes }}%</p>
                  </div>
                </div>

                <p class="card-main-color"><small class="card-muted-color">Date added:
                  {{ formatDate(currency.date_added) }}</small></p>
              </div>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CurrenciesList",
  props: {
    currencies: Array
  },
  methods: {
    defineChangesColor(changes) {
      return changes >= 0 ? "card-success" : "card-danger"
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return date.getDate() + "." + (date.getMonth() + 1) + "." + date.getFullYear();
    },
    formatNumber(num, digits) {
      const lookup = [
        {value: 1, symbol: ""},
        {value: 1e3, symbol: "k"},
        {value: 1e6, symbol: "M"},
        {value: 1e9, symbol: "B"},
        {value: 1e12, symbol: "T"},
        {value: 1e15, symbol: "P"},
        {value: 1e18, symbol: "E"}
      ];
      const rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
      const item = lookup.slice().reverse().find(function (item) {
        return num >= item.value;
      });
      return item ? (num / item.value).toFixed(digits).replace(rx, "$1") + item.symbol : "0";
    }
  }
}
</script>

<style scoped>

</style>