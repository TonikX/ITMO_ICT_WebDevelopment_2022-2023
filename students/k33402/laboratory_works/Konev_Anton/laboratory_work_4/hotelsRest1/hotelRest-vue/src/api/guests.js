class GuestsAPI {
    constructor(instance) {
        this.API = instance
    }

    getAllGuests = async () => {
        return this.API({
            url: '/hotels/guests'
        })
    }

    getGuestById = async (id) => {
        return this.API({
            url: `/hotels/guests/${id}`
        })
    }

    addBooking = async (data, token) => {
        return this.API({
            method: 'POST',
            url: '/hotels/booking',
            data,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            }
        })
    }

    closeBooking = async (id) => {
        return this.API({
            method: 'POST',
            url: `/hotels/check_out_booking/${id}`
        })
    }


}

export default GuestsAPI