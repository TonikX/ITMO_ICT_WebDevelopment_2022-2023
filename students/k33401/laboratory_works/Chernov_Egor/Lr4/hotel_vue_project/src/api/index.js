import instance from "@/api/instance";
import HotelsApi from "@/api/hotels";
import RegComApi from "@/api/regCom";
import UserApi from "@/api/user";


const hotelsApi = new HotelsApi(instance)

const regComApi = new RegComApi(instance)

const userApi = new UserApi(instance)

export {
    hotelsApi,
    regComApi,
    userApi
}