class CalendarEventsApi {
    constructor(instance) {
      this.API = instance
    }
  
    getAll = async () => {
      return this.API({
        url: '/calendarEvents'
      })
    }
  
    getById = async (id) => {
      return this.API({
        url: `/calendarEvents/${id}`
      })
    }
  
    create = async (data) => {
      return this.API({
        url: '/calendarEvents',
        method: 'POST',
        data,
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }
  
  }
  
  export default CalendarEventsApi