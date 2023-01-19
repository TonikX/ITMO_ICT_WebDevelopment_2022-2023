<template>
  <div class="container pt-5">
    <div class="input-group">
      <form class="form-floating" @submit.prevent="filterBySearchString">
        <input v-model="searchString" class="form-control" type="search" id="searchInput"
               placeholder="Поиск криптовалюты (название/символ)"
               aria-label="Search">
        <label for="searchInput">Поиск криптовалюты (название/символ)</label>
      </form>
      <button class="btn btn-main" type="submit">Search</button>
    </div>

    <button class="btn btn-main mx-3 mt-3" @click="sortByDateButtonPressed">Сортировать по дате
      {{ sortByDateButtonSign }}
    </button>
    <button class="btn btn-main mx-3 mt-3" @click="sortByPriceButtonPressed">Сортировать по цене
      {{ sortByPriceButtonSign }}
    </button>
  </div>
</template>

<script>
export default {
  name: "CurrencyFiltersBlock",
  data() {
    return {
      searchString: "",
      sortByDateDesc: false,
      sortByPriceDesc: false,
      sortByDateButtonSign: '',
      sortByPriceButtonSign: '',
      filterURL: ""
    }
  },
  props: {
    baseURL: String
  },
  created() {
    if (this.baseURL) {
      this.filterURL = this.baseURL
    } else {
      const unwatch = this.$watch('baseURL', () => {
        this.filterURL = this.baseURL
        unwatch()
      })
    }
  },
  watch: {
    filterURL(newUrl) {
      if (this.filterURL !== this.baseURL) {
        this.$emit('response', newUrl)
      }
    }
  },
  methods: {
    sortByDateButtonPressed() {
      this.sortByDateDesc = !this.sortByDateDesc
      this.sortByPriceButtonSign = ' '

      if (this.sortByDateDesc) {
        this.sortByDateButtonSign = '↑'
        this.addSearchParam("ordering", "date_added")
      } else {
        this.sortByDateButtonSign = '↓'
        this.addSearchParam("ordering", "-date_added")
      }
    },

    filterBySearchString() {
      this.addSearchParam("search", this.searchString)
    },

    sortByPriceButtonPressed() {
      this.sortByPriceDesc = !this.sortByPriceDesc
      this.sortByDateButtonSign = ' '

      if (this.sortByPriceDesc) {
        this.sortByPriceButtonSign = '↑'
        this.addSearchParam("ordering", "price")
      } else {
        this.sortByPriceButtonSign = '↓'
        this.addSearchParam("ordering", "-price")
      }
    },

    addSearchParam(param, value) {
      let newUrl = new URL(this.filterURL)
      newUrl.searchParams.set(param, value)
      this.filterURL = newUrl.toString()
    }
  }
}
</script>
