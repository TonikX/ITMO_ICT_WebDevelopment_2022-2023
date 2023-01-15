import instance from "@/api/instance";
import HotelsApi from "@/api/hotels";


const hotelsApi = new HotelsApi(instance)

export {
    hotelsApi
}