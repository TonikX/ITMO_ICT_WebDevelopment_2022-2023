import {singupApi} from "@/api";
import {defineStore} from 'pinia'

const useSingUpStore = defineStore('singup', {

    actions: {
        async singup(data) {
            return await singupApi.singup(data)
        }
    },

})

export default useSingUpStore
