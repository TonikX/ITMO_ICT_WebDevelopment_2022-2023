export default class UserEventsApi {
  constructor(instance) {
    this.API = instance
  }

  getAll = async () => {
    return this.API({
      url: '/userEvents'
    })
  }

  getById = async (id) => {
    return this.API({
      url: `/userEvents?userId=${id}`
    })
  }

  deleteById = async (id) => {
    return this.API({
      url: `/userEvents/${id}`,
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }

  createUserEvent = async (data) => {
    return this.API({
      url: '/userEvents',
      method: 'POST',
      data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }
}
