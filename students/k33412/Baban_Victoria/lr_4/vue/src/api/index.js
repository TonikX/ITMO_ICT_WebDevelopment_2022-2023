import instance from "../api/instance"
import UserAPI from "../api/user"
import EventsAPI from "../api/event"
import UsersEventsAPI from "../api/users_events"


const userAPI = new UserAPI(instance)
const eventsAPI = new EventsAPI(instance)
const userEventsAPI = new UsersEventsAPI(instance)

export {
    userAPI,
    eventsAPI,
    userEventsAPI
}