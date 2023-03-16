<template>
    <v-form @submit.prevent="onSubmit">
        <v-alert :text="error" v-if="error" type="error"/>
        <v-text-field v-for="field in fields"
                      v-bind:key="field.key"
                      v-model="profile[field.key]"
                      :name="field.key"
                      :label="field.title"/>
        <v-btn color="primary" type="submit">Зарегистрироваться</v-btn>
    </v-form>
</template>

<script setup>
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError} from "@/utils";

const router = useRouter()
const user = useUserStore();

onMounted(() =>
{
	if (user.isAuth)
		router.push({name: "Home"});
})

const error = ref("");

const fields = [
	{title: "Логин", key: "username"},
	{title: "Пароль", key: "password"},
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
];
const profile = ref({});

function onSubmit() {
	error.value = "";
	let profile_values = Object.fromEntries(fields.map(field => [field.key, profile.value[field.key]]));
	axios
		.post("/auth/users/", profile_values)
		.then(() => {
			router.push({name: "Login"});
		})
		.catch(axiosError => {
			error.value = getError(axiosError)
		});
}
</script>
