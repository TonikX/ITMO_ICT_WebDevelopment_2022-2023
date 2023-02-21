import { defineStore } from "pinia";
import { userApi } from "@/api";

const usersStore = defineStore("users", {
  state: () => ({
    user: null,
    token: null,
  }),

  actions: {
    async register(user) {
      console.log("in store", user);
      const response = await userApi.register(user);
      console.log("in store response", response);
      return response.data;
    },

    async login(credentials) {
      const response = await userApi.login(credentials);
      this.user = {
        username: credentials.username,
        password: credentials.password,
      };
      this.token = response.data.auth_token;
      return response;
    },

    async logout() {
      if (this.token) {
        this.token = null;
        this.user = null;
        this.$router.push("Navbar");
        return true;
      }
    },
  },
});

export default usersStore;
