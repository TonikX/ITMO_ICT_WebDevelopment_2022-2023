import {defineStore} from "pinia";
import {coinsAPI, usersAPI} from "@/api";

const useCoinsStore = defineStore('coins', {
    state: () => ({
        coins: []
    }),
    actions: {
        async loadCoins(search = '', sortName = '', page = 1, limit = 10) {
            const sortSplit = sortName.split(' ');
            const sort = sortSplit[0];
            const order = sortSplit[1];
            const response = await coinsAPI.getCoins(search, sort, order, page, limit);
            this.coins = response.data;
            return response.data;
        },
        async getWallet(idx) {
            const actual = await usersAPI.getCurrentUser(idx);
            const {id, coins} = actual.data;
            return {id, coins};
        },
        async loadCustomCoins() {
            const response = await coinsAPI.getCustomList();
            this.coins = response.data;
            return response.data;
        },
        async loadCoinsList(search = '') {
            const response = await coinsAPI.getCoins(search, '', '', '', '');
            this.coins = response.data;
            return response.data;
        }
    }
})

export default useCoinsStore
