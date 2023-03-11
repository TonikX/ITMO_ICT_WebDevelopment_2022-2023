import {defineStore} from 'pinia'
import {bazzarAPI} from '@/api'


const useBazzarStore = defineStore('bazzar', {
    state: () => ({
        user: null,
        token: null,
        genres: [],
        platforms: [],
        products: [],
        staff: [],
        sells: [],
        sellsInfo: [],
        games: []
    }),

    actions: {
        async register(username, email, password1, password2) {
            const response = await bazzarAPI.register(username, email, password1, password2)
            return response
        },

        async login(username, password) {
            const response = await bazzarAPI.login(username, password)
            this.token = await response.data.auth_token
            await this.loadUser()
            return response
        },

        async logout() {
            this.token = null
            this.user = null
        },

        async loadUser() {
            const response = await bazzarAPI.getUser(this.token)
            this.user = response.data
            return response
        },

        async loadGenres() {
            const response = await bazzarAPI.getGenres()
            this.genres = response.data
            return response
        },

        async loadSells() {
            const response = await bazzarAPI.getSells()
            this.sells = response.data
            return response
        },

        async loadGames() {
            const response = await bazzarAPI.getGames()
            this.games = response.data
            return response
        },

        async loadSellsInfo() {
            const response = await bazzarAPI.getSellsInfo()
            this.sellsInfo = []
            for (const si of response.data) {
                this.sellsInfo.push([si['date'], si['amount']])
            }
            return this.sellsInfo
        },


        async loadPlatforms() {
            const response = await bazzarAPI.getPlatforms()
            this.platforms = response.data
            return response
        },

        async loadProducts(params) {
            const response = await bazzarAPI.getProducts(params)
            this.products = response.data
            return response
        },

        async loadProduct(id) {
            const response = await bazzarAPI.getProduct(id)
            return response
        },

        async loadStaff() {
            const response = await bazzarAPI.getStaff()
            this.staff = response.data
            return response
        },

        async deleteStaff(username, token) {
            const response = await bazzarAPI.deleteStaff(username, token)
            this.staff = await this.loadStaff()
            return response
        },

        async updateStaff(username, token, position) {
            const response = await bazzarAPI.updateStaff(username, token, position)
            this.staff = await this.loadStaff()
            return response
        },

        async updateProduct(id, token, count) {
            const response = await bazzarAPI.updateProduct(id, token, count)
            return response
        },

        async createProduct(token, game, platform, price, count) {
            const response = await bazzarAPI.createProduct(token, game, platform, price, count)
            console.log(response)
            return response
        }
    }
})

export default useBazzarStore
