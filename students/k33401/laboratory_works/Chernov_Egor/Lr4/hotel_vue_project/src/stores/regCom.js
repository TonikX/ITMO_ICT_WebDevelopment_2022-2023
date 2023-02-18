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
        },

        async createCom(token, idUser, idRoom, checkIn, checkOut, rating, review) {
            const response = await regComApi.postCom(token, idUser, idRoom, checkIn, checkOut, rating, review)

            this.comments.push(response.data)

            return this.comments
        },

        async updateReg(token, idReg, idUser, idHotel, idRoomType, idRoom, idEmployee, statusReg, statusPay, checkIn, checkOut, booking) {
            await regComApi.putReg(token, idReg, idUser, idHotel, idRoomType, idRoom, idEmployee, statusReg, statusPay, checkIn, checkOut, booking)
            const response = await regComApi.getRegs(token)

            this.regs = response.data

            return response
        },

        async delReg(token, idReg) {
            await regComApi.deleteReg(token, idReg)
            const response = await regComApi.getRegs(token)

            this.regs = response.data

            return response
        },
    }
})

export default useRegComStore
