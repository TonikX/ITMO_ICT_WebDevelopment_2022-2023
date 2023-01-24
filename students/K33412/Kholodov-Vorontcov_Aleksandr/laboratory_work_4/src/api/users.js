export default class UsersAPI {
    constructor(instance) {
        this.API = instance
    }

    getAllUsers = async () => {
        return this.API({
            method: 'GET',
            url: '/users'
        })
    }

    getCurrentUser = async (id) => {
        return this.API({
            method: 'GET',
            url: `/users/${id}`
        })
    }

    push = async (user) => {
        return this.API({
            method: 'PUT',
            url: `/users/${user.id}`,
            data: user,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }


    createNewUser = async (data) => {
        return this.API({
            method: 'POST',
            url: '/users',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
}
