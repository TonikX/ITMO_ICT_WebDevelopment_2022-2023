import { defineStore } from "pinia";
// импортируем API
import { roomsApi } from "@/api";

const userRoomsStore = defineStore("rooms", {
  state: () => ({
    date: "",
    rooms: "",
  }),

  actions: {
    async loadFreeRooms(date) {
      const response = await roomsApi.freeRooms(date);
      this.date = date;
      this.rooms = JSON.stringify(response.data.count);
      return response;
    },
  },
});

export default userRoomsStore;
