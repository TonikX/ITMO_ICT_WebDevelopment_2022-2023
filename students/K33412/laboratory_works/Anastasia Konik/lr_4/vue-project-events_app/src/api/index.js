import instance from "@/api/instance"
import CardApi from "@/api/cards"
import UsersApi from "@/api/users"
import UserEventsApi from "@/api/userEvents"

const cardApi = new CardApi(instance)
const usersApi = new UsersApi(instance)

const userEventsApi = new UserEventsApi(instance)

export {
    cardApi,
    usersApi,
    userEventsApi
}

