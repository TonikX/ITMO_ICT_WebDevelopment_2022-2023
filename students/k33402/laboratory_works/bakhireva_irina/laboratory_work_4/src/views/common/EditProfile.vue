<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <v-form @submit.prevent="onSubmit">
            <v-alert :text="error" v-if="error" type="error"/>
            <v-text-field v-for="field in fields"
                          v-bind:key="field.key"
                          v-model="profile[field.key]"
                          :name="field.key"
                          :label="field.title"/>
            <v-btn color="primary" type="submit">Сохранить</v-btn>
        </v-form>
    </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import axios from "axios";
import {getError} from "@/utils";

const loaded = ref(false);
const error = ref("");
const router = useRouter()
const user = useUserStore();
const profile = ref({});

const fields = [
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
]

onMounted(() => {
	if (!user.isAuth) {
		user.updateToken();
		router.push({name: "Login"});
	}

	axios
		.get("/auth/users/me/")
		.then(response => {
			profile.value = response.data;
		})
		.catch(axiosError => {
			if (axiosError.response.status === 401) {
				user.updateToken();
				router.push({name: "Login"});
			} else {
				error.value = getError(axiosError)
			}
		}).finally(() => loaded.value = true)
})

function onSubmit() {
	loaded.value = false;
	let patch = Object.fromEntries(fields.map(field => [field.key, profile.value[field.key]]));
	axios
		.patch("/auth/users/me/", patch)
		.then(response => {
			profile.value = response.data;
		})
		.catch(axiosError => {
			if (axiosError.response.status === 401) {
				user.updateToken();
				router.push({name: "Login"});
			} else {
				error.value = getError(axiosError)
			}
		}).finally(() => loaded.value = true)
}

</script>
