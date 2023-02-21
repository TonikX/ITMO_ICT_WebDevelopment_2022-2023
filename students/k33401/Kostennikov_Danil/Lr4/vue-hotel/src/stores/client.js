import { defineStore } from "pinia";
// импортируем API
import { clientApi } from "@/api";

const clientStore = defineStore("rooms", {
  state: () => ({
    city: "",
    count: "",
  }),

  actions: {
    async loadClientCityCount(data) {
      const response = await clientApi.clientCityCount(data);
      this.city = data;
      this.count = JSON.stringify(response.data.count);
      return response;
    },
  },
});

export default clientStore;
