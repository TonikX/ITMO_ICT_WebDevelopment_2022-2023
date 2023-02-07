import instance from "@/api/instance";
import RoomsApi from "@/api/rooms";

const roomsApi = new RoomsApi(instance);

export { roomsApi };
