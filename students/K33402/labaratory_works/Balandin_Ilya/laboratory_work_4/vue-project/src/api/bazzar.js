class BazzarAPI {
    constructor(instance) {
        this.API = instance
    }

    getGenres = async () => {
        return this.API({
            url: `/gamebazzar/genre/`
        })
    }

    getGames = async () => {
        return this.API({
            url: `/gamebazzar/game/`
        })
    }

    getPlatforms = async () => {
        return this.API({
            url: `/gamebazzar/platform/`
        })
    }

    getProducts = async (params) => {
        return this.API({
            url: `/gamebazzar/product/${params}`
        })
    }

    getProduct = async (id) => {
        return this.API({
            url: `/gamebazzar/product/${id}/`
        })
    }

    getSells = async () => {
        return this.API({
            url: `/gamebazzar/sell/`
        })
    }

    getSellsInfo = async () => {
        return this.API({
            url: `/gamebazzar/sell/info/`
        })
    }

    deleteStaff = async (username, token) => {
        return this.API({
            method: 'DELETE',
            url: `/gamebazzar/staff/${username}/`,
            headers: {
                'Authorization': `Token ${token}`
            }
        })
    }

    updateStaff = async (username, token, position) => {
        return this.API({
            method: 'PATCH',
            url: `/gamebazzar/staff/${username}/`,
            headers: {
                'Authorization': `Token ${token}`
            },
            data: {
                is_staff: position
            }
        })
    }

    updateProduct = async (id, token, count) => {
        return this.API({
            method: 'PATCH',
            url: `/gamebazzar/product/${id}/update/`,
            headers: {
                'Authorization': `Token ${token}`
            },
            data: {
                count: count
            }
        })
    }

    createProduct = async (token, game, platform, price, count) => {
        return this.API({
            method: 'POST',
            url: `/gamebazzar/product/create/`,
            headers: {
                'Authorization': `Token ${token}`
            },
            data: {
                count: count,
                game: game,
                platform: platform,
                price: price
            }
        })
    }

    register = async (username, email, password1, password2) => {
        return this.API({
            method: 'POST',
            url: `/auth/users/`,
            data: {
                email: email,
                username: username,
                password: password1,
                re_password: password2,
            }
        })
    }

    login = async (username, password) => {
        return this.API({
            method: 'POST',
            url: `/auth/token/login/`,
            data: {
                username: username,
                password: password
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

    getUser = async (token) => {
        return this.API({
            method: 'GET',
            url: '/gamebazzar/me/',
            headers: {
                'Authorization': `Token ${token}`
            }
        })
    }

    getStaff = async () => {
        return this.API({
            method: 'GET',
            url: '/gamebazzar/staff/'
        })
    }
}

export default BazzarAPI
