import {defineStore} from 'pinia'

export const useStateStore = defineStore ({
    id: 'UserStatus',
    state: () => ({
        userState: false
    }),
    actions:{
        StateChecker(payload){
            this.userState = payload;
        }
    }
})


