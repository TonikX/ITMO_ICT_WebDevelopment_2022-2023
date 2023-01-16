import {defineStore} from "pinia";

export const useAuthStore = defineStore("auth", {
	state: () => ({
		token: "",
		isAuthenticated: false,
	}),
	actions: {
		init() {
			if (localStorage.getItem("token")) {
				this.setToken(localStorage.getItem("token"));
			} else {
				this.resetToken();
			}
		},
		setToken(token) {
			localStorage.setItem("token", token);
			this.token = token;
			this.isAuthenticated = true;
		},
		resetToken() {
			localStorage.setItem("token", "");
			this.token = '';
			this.isAuthenticated = false;
		}
	}
})
