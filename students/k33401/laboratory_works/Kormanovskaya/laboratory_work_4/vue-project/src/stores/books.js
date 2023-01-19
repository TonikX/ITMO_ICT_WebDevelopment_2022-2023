import {defineStore} from 'pinia'
// импортируем API
import {libraryAPI} from '@/api'


const useLibraryStore = defineStore('library', {
    state: () => ({
        books: [],
        genres: [],
        user: {},
        book: {},
        token: {}
    }),

    actions: {
        async loadBooks(params) {
            const response = await libraryAPI.getBooks(params)
            this.books = response.data
            return response
        },

        async loadBook(slug) {
            const response = await libraryAPI.getBook(slug)
            this.book = response.data
            return response
        },

        async loadGenres() {
            const response = await libraryAPI.getGenres()
            this.genres = response.data
            return response
        },

        async loadUserinfo(token) {
            const response = await libraryAPI.getUserinfo(token)
            const user = await response
            this.user = response.data
            this.token = token
            return response
        },

        async login(username, password){
            const response = await libraryAPI.login(username, password)
            this.token = response.data
            return response
        },

        async signup(username, password1, password2){
            const response = await libraryAPI.signup(username, password1, password2)
            this.token = response.data
            return response
        },

        async logout(token) {
            try {
                const response = await libraryAPI.logout(token)
                const smth = await response
            }
            catch {

            }
            this.token = null
            this.user = null
        },

        async addBook(token, id, read) {
            const response = await libraryAPI.addBook(token, id, read)
        },

        async updateBook(token, id, is_read, rate, review) {
            const response = await libraryAPI.updateBook(token, id, is_read, rate, review)
        }
    }
})


export default useLibraryStore
