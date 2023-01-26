<template>
  <section class="dataTable-wrapper">
    <div class="dataTable-wrapper d-flex justify-content-center">
      <table class="table align-middle border-light mt-5 w-75">
        <tr class="head-row border-light ">
          <th class="align-middle fw-bold">Название
<!--            <sort-button/>-->
          </th>
          <th class="align-middle fw-bold">Цена
<!--            <sort-button/>-->
          </th>
          <th class="fw-bold">Количество
<!--            <sort-button/>-->
          </th>
          <th class="fw-bold">Итого</th>
          <th class="fw-normal">
            <div class="">
              <select-sort
                  v-model="sortName"
                  :options="sortOptions"
              />
            </div>
          </th>
          <th class="d-flex justify-content-center">
            <div>
              <p class="balance m-0">Баланс:</p>
              <p class="balance fw-light m-0">{{ balance() }}
              </p>
            </div>
          </th>
        </tr>
        <wallet :coins="coins" @buyEvent="buyCoin" @sellEvent="sellCoin"/>
      </table>
    </div>
  </section>
</template>

<script>
import Wallet from "@/components/lists/Wallet.vue";
import {mapActions, mapState} from "pinia";
import useCoinsStore from "@/stores/coins";
import useUsersStore from "@/stores/users";

export default {
  name: 'Personal',
  components: {
    Wallet
  },
  data() {
    return {
      coins: [],
      sortName: '',
      sortOptions: [
        {value: 'name ASC', name: 'По названию (ASC)'},
        {value: 'name DESC', name: 'По названию (DESC)'},
        {value: 'current_price ASC', name: 'По цене (ASC)'},
        {value: 'current_price DESC', name: 'По цене (DESC)'},
        {value: 'amount ASC', name: 'По количеству (ASC)'},
        {value: 'amount DESC', name: 'По количеству (DESC)'},
      ]
    }
  },
  methods: {
    ...mapActions(useCoinsStore, ['getWallet', "loadCoins", "loadCustomCoins"]),
    ...mapActions(useUsersStore, ['commitActions']),

    async getCoins() {
      let current = await this.getWallet(this.user.id);
      const data = await this.loadCustomCoins()
      for (let i = 0; i < current.coins.length; i++) {
        for (let j = 0; j < data.length; j++) {
          if (current.coins[i].id === data[j].id) {
            this.coins[i] = data[j]
            this.coins[i].amount = current.coins[i].amount
          }
        }
      }
    },

    balance() {
      let res = 0;
      for (let i = 0; i < this.coins.length; i++) {
        res += this.coins[i].amount * this.coins[i].current_price;
      }
      return res.toFixed(2)
    },

    async buyCoin(id, amount) {
      let newCoin = true
      for (let i = 0; i < this.user.coins.length; i++) {
        if (id === this.user.coins[i].id) {
          this.user.coins[i].amount += amount
          newCoin = false
        }
      }

      if (newCoin) {
        this.user.coins.push({id: id, amount: amount})
      }

      await this.commitActions(this.user);
      await this.getCoins()
    },

    async sellCoin(id, amount) {
      let index;
      for (let i = 0; i < this.user.coins.length; i++) {
        if (id === this.user.coins[i].id) {
          this.user.coins[i].amount -= amount;
          index = i;
        }
      }

      if (this.user.coins[index].amount === 0) {
        this.user.coins = this.user.coins.filter(coin => coin.id !== id)
      }

      await this.commitActions(this.user);
      await this.getCoins()
      location.reload()
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user'])
  },
  mounted() {
    this.getCoins()
  },
  watch: {
    async sortName(sortName) {
      const sortSplit = sortName.split(' ')
      const type = sortSplit[0]
      const order = sortSplit[1]
      if (type === 'name') {
        this.coins.sort((a, b) => a[type].localeCompare(b[type]))
      } else {
        this.coins.sort((a, b) => a[type] - b[type])
      }
      if (order === 'DESC') {
        this.coins.reverse()
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Tahoma', sans-serif
}

.table {
  border: 2px solid;
}

.head-row {
  border-bottom: 2px solid;
  font-weight: normal;
}

.head-row {
  font-weight: normal;
}

.table thead th {
  padding: 30px;
  font-weight: normal;
}

.dataTable-wrapper {
  margin: 20px auto;
  overflow-x: auto
}


::placeholder {
  color: black;
  font-weight: 600;
}


.table tbody td {
  padding: 30px;
  margin: 0;
}

.btn-pagination {
  border: none;
  background-color: white;
  margin-left: 15px;
}


body {
  background-color: var(--bg-color) !important;
  color: var(--text-color) !important;
  border-color: var(--card-color) !important;
}

.page-number {
  border-color: var(--text-color);
}

tr {
  border-color: var(--card-color) !important;
}
</style>
