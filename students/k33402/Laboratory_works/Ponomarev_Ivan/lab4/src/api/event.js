class eventApi{
    constructor(instance){
        this.API = instance
    }

    getEventsList = async () => {
        return this.API({
            url: `/api/events/all`,
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
    }

    getCertainEvent = async (id) => {
        return this.API({
            url: `/api/events/${id}`,
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
    }

    getFilteredEventsByCategoryAndCity = async (category, city) => {
        return this.API({
            url: `/api/events/all?category=${category}&city=${city}`,
            method: 'GET',
        })
    }

    getFilteredEventsByCategory = async (category) => {
        return this.API({
            url: `/api/events/all?category=${category}`,
            method: 'GET'
        })
    }

    getFilteredEventsByCity = async (city) => {
        return this.API({
            url: `/api/events/all?city=${city}`,
            method: 'GET'
        })
    }
}
export default eventApi
