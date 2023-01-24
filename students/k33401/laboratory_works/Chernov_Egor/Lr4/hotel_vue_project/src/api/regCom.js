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

    postCom = async (token, idUser, idRoom, checkIn, checkOut, rating, review) => {
        return this.API({
            method: 'POST',
            url: "/act/com/",
            headers: {'Authorization': 'Bearer ' + token},
            data: {
                user_com: idUser,
                room_com: idRoom,
                rating_com: rating,
                check_in_com: checkIn,
                check_out_com: checkOut,
                review_com: review
            }
        })
    }

    putReg = async (token, idReg, idUser, idHotel, idRoomType, idRoom, idEmployee, statusReg, statusPay, checkIn, checkOut, booking) => {
        return this.API({
            method: 'PUT',
            url: `/act/reg/${idReg}/`,
            headers: {'Authorization': 'Bearer ' + token},
            data: {
                user_reg: idUser,
                hotel_reg: idHotel,
                rt_reg: idRoomType,
                room_reg: idRoom,
                employee_reg: idEmployee,
                status_reg_reg: statusReg,
                status_pay_reg: statusPay,
                check_in_reg: checkIn,
                check_out_reg: checkOut,
                booking_reg: booking
            }
        })
    }

    deleteReg = async (token, idReg) => {
        return this.API({
            method: 'DELETE',
            url: `/act/reg/${idReg}/`,
            headers: {'Authorization': 'Bearer ' + token}
        })
    }
}

export default RegComApi
