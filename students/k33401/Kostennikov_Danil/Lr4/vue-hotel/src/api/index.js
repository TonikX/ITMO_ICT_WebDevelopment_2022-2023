import instance from "@/api/instance";
import RoomsApi from "@/api/rooms";
import UserApi from "@/api/user";

const roomsApi = new RoomsApi(instance);
const userApi = new UserApi(instance);

export { roomsApi, userApi };
