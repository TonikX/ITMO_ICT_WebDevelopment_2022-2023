class LibraryAPI {
    constructor(instance) {
        this.API = instance
    }

    getBooks = async (params) => {
        return this.API({
            url: `/library/books/?${params}`
        })
    }

    getBook = async (slug) => {
        return this.API({
            url: `/library/books/${slug}/`
        })
    }

    getGenres = async () => {
        return this.API({
            url: '/library/genres/'
        })
    }

    signup = async (username, password1, password2) => {
        return this.API({
            method: 'POST',
            url: `/auth/users/`,
            data: {
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

    getUserinfo = async (token) => {
        return this.API({
            method: 'GET',
            url: '/library/me/',
            headers: {
                'Authorization': `Token ${token}`
            }
        })
    }

    addBook = async (id, token, read) => {
        return this.API({
            method: 'POST',
            url: `/library/reading/${id}/add/`,
            headers: {
                'Authorization': `Token ${token}`
            },
            data: {
                is_read: read
            }
        })
    }

    updateBook = async (token, id, is_read, rate, review) => {
        return this.API({
            method: 'PUT',
            url: `/library/reading/${id}/update/`,
            headers: {
                'Authorization': `Token ${token}`
            },
            data: {
                is_read: is_read,
                rate: rate,
                review_text: review
            }
        })
    }
}

export default LibraryAPI
