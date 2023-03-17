class userApi {
    constructor(instance){
        this.API = instance
    }

    login = async (data) => {
        return this.API({
            url: `/api/auth/token/login/`,
            method: 'POST',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    logout = async (authToken) => {
        return this.API({
            url: `api/auth/token/logout`,
            method: 'GET',
            headers: {
                'Authorization': `Token ${authToken}`
            }
        })
    }

    sign_up = async (data) => {
        return this.API({
            url: `api/auth/users/`,
            method: 'POST',
            data,
            headers: {
                'Content-Type': 'application/json',
            }
        })
    }

    get_user_info = async (authToken) => {
        return this.API({
            url: `api/auth/users/me/`,
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authToken}`
            }
        })
    }
    get_user_profile = async (id) => {
        return this.API({
            url: `/api/users/${id}`,
            method: 'GET'
        })
    }

}
export default userApi