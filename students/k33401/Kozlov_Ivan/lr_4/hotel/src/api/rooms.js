class RoomsApi {
    constructor(instance) {
        this.API = instance
    }

    getAllRooms = async () => {
        return this.API({
            url: '/api/all_rooms/'
        })
    }

    sortRooms = async (data) => {
        return this.API({
            url: '/api/all_rooms/?type__count_places_in_room=' + data
        })
    }
}

export default RoomsApi
