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

    putAccUser = async (token, id, username, firstName, lastName, email, phoneGuest, passportGuest, phoneEmployee, positionEmployee) => {
        return this.API({
            method: 'PUT',
            url: `/account/user/${id}/`,
            headers: {'Authorization': 'Bearer ' + token},
            data: {
                username: username,
                first_name: firstName,
                last_name: lastName,
                email: email,
                user_guest: {
                    phone_guest: phoneGuest,
                    passport_guest: passportGuest
                },
                user_employee: {
                    phone_employee: phoneEmployee,
                    position_employee: positionEmployee
                }
            }
        })
    }

    deleteUser = async (token, id, currentPassword) => {
        return this.API({
            method: 'DELETE',
            url: `/auth/users/${id}/`,
            headers: {'Authorization': 'Bearer ' + token},
            data: {
                current_password: currentPassword
            }
        })
    }

    createUser = async (username, email, password) => {
        return this.API({
            method: 'POST',
            url: '/auth/users/',
            data: {
                username: username,
                email: email,
                password: password
            }
        })
    }
}

export default UserApi
