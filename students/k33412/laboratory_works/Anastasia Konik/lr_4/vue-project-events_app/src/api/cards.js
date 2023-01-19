class CardApi {
    constructor(instance) {
        this.API = instance
    }

    getAll = async () => {
        return this.API({
            url: '/api/events/list/'
        })
    }

    getOne = async (eventId) => {
        return this.API({
            url: `/api/event/${eventId}/`
        })
    }
}

export default CardApi

