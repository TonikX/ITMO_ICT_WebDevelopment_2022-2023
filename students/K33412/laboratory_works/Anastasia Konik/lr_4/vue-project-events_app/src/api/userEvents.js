class UserEventsApi {
    constructor(instance) {
        this.API = instance
    }

    getByUserId = async (userId) => {
        return this.API({
            url: `/api/user/events/${userId}/`
        })
    }

    enrollUser = async (data) => {
        return this.API({
            url: '/api/enroll/create/',
            method: 'POST',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
}

export default UserEventsApi

