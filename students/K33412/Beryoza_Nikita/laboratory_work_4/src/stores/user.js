import {defineStore} from 'pinia'
import {computed, ref} from "vue";
import axios from "axios";

export const useUserStore = defineStore('user', () => {
	const token = ref(localStorage.getItem("token"));
	const role = ref(localStorage.getItem("role"));

	if (token.value) axios.defaults.headers.common["Authorization"] = `Token ${token.value}`;
	else axios.defaults.headers.common["Authorization"] = "";

	const isAuth = computed(() => {
		return token.value && (role.value === "HR" || role.value === "Applicant")
	})

	const isHR = computed(() => {
		return isAuth.value && role.value === "HR"
	});

	const isApplicant = computed(() => {
		return isAuth.value && role.value === "Applicant"
	});

	function updateToken(newToken = "", newRole = "") {
		token.value = newToken;
		role.value = newRole;

		if (newToken) axios.defaults.headers.common["Authorization"] = `Token ${newToken}`;
		else axios.defaults.headers.common["Authorization"] = "";

		localStorage.setItem("token", newToken);
		localStorage.setItem("role", newRole);
	}

	return {token, role, isAuth, isHR, isApplicant, updateToken}
})
