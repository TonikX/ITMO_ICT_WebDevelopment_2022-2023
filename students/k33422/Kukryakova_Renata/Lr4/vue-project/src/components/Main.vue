<template>
  <section class="dataTable-wrapper d-flex justify-content-center">
    <table class="table align-middle mt-5 w-75 bg-white border-light">
      <tr class="search-row p-2 bg-light">
        <td colspan="2" class="align-middle search-header  justify-content-between">
          <div class="form d-flex">
            <search-input v-model="search" @send-search="findCoins" style="width: 350px !important;"/>
          </div>
        </td>
        <td colspan="3" class="">
          <div class="d-flex justify-content-end">
            <select-sort
                v-model="sortName"
                :options="sortOptions"
            />
          </div>
        </td>
      </tr>
      <tr class="head-row p-2 border-light">
        <th class="fw-normal ps-4 align-middle">Название
          <sort-button v-model="sortName"/>
        </th>
        <th class="fw-normal align-middle">Цена
          <sort-button/>
        </th>
        <th class="fw-normal align-middle">Изменение
          <sort-button/>
        </th>
        <th class="fw-normal align-middle">Дата добавления
          <sort-button/>
        </th>
        <th class="fw-normal">
          <div class="pagination d-flex justify-content-center align-content-center p-0">
            <button class="btn-pagination m-0 btn-prev" @click="getPrevPage" :style="[this.page > 1 ? {'display' : 'block'} : {'display':'none'}]">
              <svg style="width: 30px; height: 30px;">
                <use xlink:href="#arrow">
                </use>
              </svg>
            </button>
            <div class="page-number m-0 mx-1"
                 style="display: flex; justify-content: center">
              <input v-model="page">
            </div>
            <button class="btn-pagination btn-next m-0" @click="getNextPage" :style="[this.page < 3 ? {'display' : 'block'} : {'display':'none'}]">
              <svg style="width: 30px; height: 30px; transform: rotate(180deg)">
                <use xlink:href="#arrow">
                </use>
              </svg>
            </button>
          </div>
        </th>
      </tr>
      <coins-list :coins="coins" @buyEvent="buyCoin"/>
    </table>
  </section>
</template>

<script>
import useCoinsStore from "@/stores/coins";
import {mapActions, mapState} from "pinia";
import CoinsList from "@/components/lists/CoinsList.vue";
import useUsersStore from "@/stores/users";


export default {
  name: 'Main',
  components: {
    CoinsList
  },
  data() {
    return {
      coins: [],
      page: 1,
      limit: 10,
      total: 3,
      search: '',
      sortName: '',
      sortOptions: [
        {value: 'name ASC', name: 'По названию (ASC)'},
        {value: 'name DESC', name: 'По названию (DESC)'},
        {value: 'current_price ASC', name: 'По цене (ASC)'},
        {value: 'current_price DESC', name: 'По цене (DESC)'},
        {value: 'price_change_percentage_24h ASC', name: 'По изменению (ASC)'},
        {value: 'price_change_percentage_24h DESC', name: 'По изменению (DESC)'},
        {value: 'atl_date ASC', name: 'По дате (ASC)'},
        {value: 'atl_date DESC', name: 'По дате (DESC)'},
      ]
    }
  },
  methods: {
    ...mapActions(useCoinsStore, ['loadCoins']),
    ...mapActions(useUsersStore, ['commitActions']),
    async getCoins() {
      this.coins = await this.loadCoins(this.search, this.sortName);
    },
    buyCoin(id, amount) {
      let newCoin = true
      for (let i = 0; i < this.user.coins.length; i++) {
        if (id === this.user.coins[i].id) {
          this.user.coins[i].amount += amount;
          newCoin = false;
        }
      }
      if (newCoin) {
        this.user.coins.push({id: id, amount: amount});
      }

      this.commitActions(this.user);
    },
    async findCoins() {
      this.coins = await this.loadCoins(this.search, this.sortName);
    },
    async getPrevPage() {
      if (this.page > 1) {
        this.page--;
        this.coins = await this.loadCoins(this.search, this.sortName, this.page);
      }

    },
    async getNextPage() {
      if (this.page < this.total) {
        this.page++;
        this.coins = await this.loadCoins(this.search, this.sortName, this.page);
      }
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user'])
  },
  mounted() {
    this.getCoins();
  },
  watch: {
    async sortName(sortName) {
      this.coins = await this.loadCoins(this.search, sortName);
    }
  }
}
</script>

<style scoped>
.table {
  border: 2px solid var(--card-color) !important;
}

.head-row {
  border-bottom: 2px solid;
  font-weight: normal;
}


.btn-pagination {
  border: none;
  background-color: white;
  margin-left: 15px;
}


.page-number {
  border-color: var(--text-color);
  border: 2px solid;
  border-radius: 20px;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
}

tr {
  border-color: var(--card-color);
}

input {
  width: 9px;
  height: 20px;
  border: none;
}

</style>