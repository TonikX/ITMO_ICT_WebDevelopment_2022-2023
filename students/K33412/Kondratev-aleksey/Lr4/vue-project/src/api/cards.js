export default class CardApi {
  constructor(instance) {
    this.API = instance
  }

  getAll = async () => {
    return this.API({
      url: '/events'
    })
  }

  getById = async (id) => {
    return this.API({
      url: `/events/${id}`
    })
  }
}

