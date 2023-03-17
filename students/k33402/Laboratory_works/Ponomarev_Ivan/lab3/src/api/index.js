import eventApi from "@/api/event"
import userApi from "@/api/user"
import enrollmentsApi from "@/api/enrollment"
import categoriesApi from "@/api/category"
import instance from "@/api/instance"

const event_api = new eventApi(instance)
const user_api = new userApi(instance)
const enrollment_api = new enrollmentsApi(instance)
const category_api = new categoriesApi(instance)

export {
    event_api,
    user_api,
    enrollment_api,
    category_api
}

