class UserApi {
    constructor(instance) {
        this.API = instance
    }

    login = async (username, password) => {
        return this.API({
            method: 'POST',
            url: `/auth/token/`,
            data: {
                username: username,
                password: password
            }
        })
    }

    getUsers = async (token) => {
        return this.API({
            method: 'GET',
            url: '/auth/users/',
            headers: {'Authorization': 'Bearer ' + token}
        })
    }

    getAccUser = async (token, id) => {
        return this.API({
            method: 'GET',
            url: `/account/user/${id}/`,
            headers: {'Authorization': 'Bearer ' + token}
        })
    }

    putAccUser = async (token, id) => {
        return this.API({
            method: 'GET',
            url: `/account/user/${id}/`,
            headers: {'Authorization': 'Bearer ' + token},
            data: {

            }
        })
    }
}

export default UserApi
