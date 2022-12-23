class UsersAPI {
  constructor(instance) {
      this.API = instance
  }

  createNewUser = async (data) => {
    return this.API({
      method: 'POST',
      url: '/auth/users/',
      data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
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

  logout = async (token) => {
    return this.API({
      method: 'POST',
      url: '/auth/token/logout/',
      headers: {
        'Authorization': `Token ${token}`
      }
    })
  }

  fetchCurrentUserInfo = async (token) => {
    return this.API({
      url: '/auth/users/me/',
      headers: {
        'Authorization': `Token ${token}`
      }
    })
  }
}

export default UsersAPI