class UsersEventsAPI {
    constructor(instance) {
        this.API = instance
    }

    fetchUsersEvents = async (token) => {
        return this.API({
            url: '/api/v1/users_events',
            headers: {
                'Authorization': `Token ${token}`
            }
        })
    }

    addUsersEvents = async (data, token) => {
        return this.API({
            method: 'POST',
            url: '/api/v1/users_events/add',
            data,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            }
        })
    }

    removeUsersEvent = async (id, token) => {
        return this.API({
            method: 'DELETE',
            url: `/api/v1/users_events/${id}`,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            }
        })
    }

}

export default UsersEventsAPI