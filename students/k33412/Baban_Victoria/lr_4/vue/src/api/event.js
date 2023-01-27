class EventsAPI {
    constructor(instance) {
        this.API = instance
    }

    fetchEvent = async (id) => {
        return this.API({
            url: `/api/v1/events/${id}`
        })
    }

    fetchEvents = async (id) => {
        return this.API({
            url: `/api/v1/events`
        })
    }

    fetchEventsByCategory = async (category) => {
        if (category === '') {
            return this.fetchEvents();
        }
        return this.API({
            url: `/api/v1/events?category=${category}`
        })
    }


    fetchEventsByCategoryDistrictType = async (category, district, type_event) => {
        if ((category === '') && (district === '') && (type_event === '')) {
            return this.fetchEvents();
        }
        return this.API({
            url: `/api/v1/events?category=${category}&district=${district}&type_event=${type_event}`
        })
    }
}

export default EventsAPI