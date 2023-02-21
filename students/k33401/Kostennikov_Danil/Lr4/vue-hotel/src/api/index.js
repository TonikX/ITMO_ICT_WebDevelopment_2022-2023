import instance from "@/api/instance";
import RoomsApi from "@/api/rooms";
import UserApi from "@/api/user";
import ClientApi from "@/api/client";

const roomsApi = new RoomsApi(instance);
const userApi = new UserApi(instance);
const clientApi = new ClientApi(instance);

export { roomsApi, userApi, clientApi };
