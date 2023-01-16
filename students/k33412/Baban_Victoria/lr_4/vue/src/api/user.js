import EventsAPI from "./event";

class UserAPI {
    constructor(instance) {
        this.API = instance
    }

    login = async (data) => {
        return this.API({
            method: 'POST',
            url: '/auth/token/login/',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    register = async (data) => {
        return this.API({
            method: 'POST',
            url: '/auth/users/',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    logout = async (token) => {
        return this.API({
            method: 'POST',
            url: '/auth/token/logout/',
            headers: {
                'Authorization': `Token ${token}`
            }
        })
    }

    currentUserInfo = async (token) => {
        return this.API({
            url: '/auth/users/me/',
            headers: {
                'Authorization': `Token ${token}`
            }
        })
    }

}

export default UserAPI