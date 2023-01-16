<template>
    <v-form @submit.prevent="onSubmit">
        <v-alert :text="error" v-if="error" type="error"/>
        <v-text-field v-model="username" name="username" label="Логин"/>
        <v-text-field v-model="password" name="password" type="password" label="Пароль"/>
        <v-btn color="primary" type="submit">Войти</v-btn>
    </v-form>
</template>

<script setup>
import {useUserStore} from "@/stores/user";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError} from "@/utils"
import {useRouter} from "vue-router";

const router = useRouter();
const user = useUserStore();

onMounted(() =>
{
	if (user.isAuth)
		router.push({name: "Home"});
});

const username = ref("");
const password = ref("");
const error = ref("");

function onSubmit() {
	error.value = "";
	let token = "";
	axios
		.post("/auth/token/login/", {username: username.value, password: password.value})
		.then(response => {
			token = response.data.auth_token;
			return axios.get("user/", {headers: {"authorization": `Token ${token}`}})
		})
		.then(response => {
			const role = response.data.role;
			user.updateToken(token, role);
			router.push({name: "Home"});
		})
		.catch(axiosError => {
			error.value = getError(axiosError)
		});
}
</script>
