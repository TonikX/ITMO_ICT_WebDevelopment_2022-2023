import instance from "@/api/instance"
import CalendarEventsApi from "@/api/calendarEvents"

const calendarEventsApi = new CalendarEventsApi(instance)

export {
  
  calendarEventsApi
}