class CheckTokenApi {
    constructor(instance) {
        this.API = instance
    }

    checkToken = async () => {
        return this.API({
            method: 'GET',
            url: '/api/auth/users/me/',
            headers: {
                'Content-Type': 'application/json'
            }
        })
    };
}

export default CheckTokenApi
