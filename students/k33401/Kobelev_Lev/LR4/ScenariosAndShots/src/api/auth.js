class AuthAPI {
    constructor(instance) {
        this.API = instance
    }

    getAuthToken = async (username, password) => {
        return this.API({
            method: 'POST',
            url: 'auth/token/login/',
            data: {
                username: username,
                password: password
            },
        })
    }

    fetchUser = async (authToken) => {
        return this.API({
            method: 'GET',
            url: 'auth/users/me/',
            headers: {
                'Authorization': `token ${authToken}`,
            },
        })
    }

    signUp = async (username, password, email) => {
        return this.API({
            method: 'POST',
            url: 'auth/users/',
            data: {
                username: username,
                password: password,
                email: email
            },
        })
    }
}

export default AuthAPI
