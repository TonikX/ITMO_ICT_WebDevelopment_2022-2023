class HotelsApi {
    constructor(instance) {
        this.API = instance
    }

    getAll = async () => {
        return this.API({
            method: 'GET',
            url: '/hotel/'
        })
    }

    getHotelRoomTypes = async (id) => {
        return this.API({
            method: 'GET',
            url: `/hotel/${id}/`
        })
    }

    getRooms = async (id) => {
        return this.API({
            method: 'GET',
            url: `/hotel/room_type/${id}/`
        })
    }

    getRoom = async (id) => {
        return this.API({
            method: 'GET',
            url: `/hotel/room_type/room/${id}/`
        })
    }
}

export default HotelsApi
