import { defineStore } from 'pinia'
import { regComApi } from "@/api";

const useRegComStore = defineStore('regCom',  {
    state: () => ({
        comments: [],
        regs: []
    }),

    actions: {
        async loadRegs(token) {
            const response = await regComApi.getRegs(token)

            this.regs = response.data

            return response
        },

        async loadComments() {
            const response = await regComApi.getComments()

            this.comments = response.data

            return response
        },

        async createReg(token, idUser, idHotel, idRoomType, idRoom, statusReg, statusPay, checkIn, checkOut, booking) {
            const response = await regComApi.postReg(token, idUser, idHotel, idRoomType, idRoom, statusReg, statusPay, checkIn, checkOut, booking)

            this.regs = response.data

            return response
        }
    }
})

export default useRegComStore
