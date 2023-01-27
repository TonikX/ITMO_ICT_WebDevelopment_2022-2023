class RoomAPI {
    constructor(instance) {
        this.API = instance
    }

    getRooms = async () => {
        return this.API({
            url: '/hotels/all_rooms'
        })
    }

    getFreeRooms = async () => {
        return this.API({
            url: '/hotels/rooms_with_time'
        })
    }
}

export default RoomAPI