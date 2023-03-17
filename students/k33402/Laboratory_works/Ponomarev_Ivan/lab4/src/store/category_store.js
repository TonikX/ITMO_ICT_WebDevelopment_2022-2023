import { defineStore } from 'pinia'
import { category_api } from '@/api'

const categoriesStore = defineStore('categories', {
    state: () => ({
        categories: []
    }),

    actions: {
        async getCategories() {
            const response = await category_api.getCategories();
            this.categories = response.data;
            return response;
        }
    }
})

export default categoriesStore