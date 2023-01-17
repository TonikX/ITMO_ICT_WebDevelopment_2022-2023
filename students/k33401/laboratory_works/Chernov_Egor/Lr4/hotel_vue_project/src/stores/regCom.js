import { defineStore } from 'pinia'
import { regComApi } from "@/api";

const useRegComStore = defineStore('regCom',  {
    state: () => ({
        comments: []
    }),

    actions: {
        async loadComments() {
            const response = await regComApi.getComments()

            this.comments = response.data

            return response
        }
    }
})

export default useRegComStore
