import instance from "@/api/instance";
import HotelsApi from "@/api/hotels";
import RegComApi from "@/api/regCom";


const hotelsApi = new HotelsApi(instance)

const regComApi = new RegComApi(instance)

export {
    hotelsApi,
    regComApi
}