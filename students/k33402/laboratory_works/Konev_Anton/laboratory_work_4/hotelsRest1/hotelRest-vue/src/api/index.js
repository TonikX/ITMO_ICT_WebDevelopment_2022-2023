import instance from "@/api/instance.js";
import RoomAPI from "@/api/rooms";
import UsersAPI from "@/api/users";
import GuestsAPI from "@/api/guests";

const roomAPI = new RoomAPI(instance);
const userAPI = new UsersAPI(instance);
const guestsAPI = new GuestsAPI(instance);

export {
    roomAPI,
    userAPI,
    guestsAPI
}