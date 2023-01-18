import { defineStore } from 'pinia'
import { tagsAPI } from "@/api";

const useTagsStore = defineStore('tags', {
    state: () => ({
        tags: [],
    }),

    actions: {
        async loadTags() {
            const response = await tagsAPI.getAllTags()

            this.tags = response.data

            return response
        },
    }
})

export default useTagsStore
