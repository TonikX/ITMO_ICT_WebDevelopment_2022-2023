import instance from "@/api/instance"
import BazzarAPI from "@/api/bazzar"

const bazzarAPI = new BazzarAPI(instance)

export {
    bazzarAPI
}