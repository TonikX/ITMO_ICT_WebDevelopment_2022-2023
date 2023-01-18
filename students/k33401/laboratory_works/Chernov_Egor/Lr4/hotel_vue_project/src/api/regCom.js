class RegComApi {
    constructor(instance) {
        this.API = instance
    }

    getRegs = async (token) => {
        return this.API({
            method: 'GET',
            url: "/act/reg/",
            headers: {'Authorization': 'Bearer ' + token}
        })
    }

    getComments = async () => {
        return this.API({
            method: 'GET',
            url: "/act/com/"
        })
    }

    postReg = async (token, idUser, idHotel, idRoomType, idRoom, statusReg, statusPay, checkIn, checkOut, booking) => {
        return this.API({
            method: 'POST',
            url: "/act/reg/",
            headers: {'Authorization': 'Bearer ' + token},
            data: {
                user_reg: idUser,
                hotel_reg: idHotel,
                rt_reg: idRoomType,
                room_reg: idRoom,
                status_reg_reg: statusReg,
                status_pay_reg: statusPay,
                check_in_reg: checkIn,
                check_out_reg: checkOut,
                booking_reg: booking
            }
        })
    }
}

export default RegComApi
