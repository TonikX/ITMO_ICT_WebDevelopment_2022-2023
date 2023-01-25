<template>
    <AuthenticatedWrapComponent>
        <v-alert v-if="error" :text="error" type="error"></v-alert>
        <v-progress-circular
                v-if="!loaded"
                color="primary"
                indeterminate/>
        <div v-if="loaded">
            <h1>Профиль</h1>
            <div class="ms-3 my-6" style="max-width:500px">
                <v-row v-for="[key,title] of Object.entries(keys)" class="border">
                    <v-col class="font-weight-bold">{{ title }}</v-col>
                    <v-col>{{ profile[key] }}</v-col>
                </v-row>
            </div>
            <v-btn :to="{name: 'EditProfile'}">
                Редактировать профиль
            </v-btn>
        </div>
    </AuthenticatedWrapComponent>
</template>

<script>
import AuthenticatedWrapComponent from "@/components/AuthenticatedWrapComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "Profile",
	components: {AuthenticatedWrapComponent},
	computed: {
		...mapStores(useAuthStore),
	},
	created() {
		this.authStore.init();
	},
	data: () => ({
		error: "",
		loaded: false,
		keys: {
			"id": "ID",
			"username": "Имя пользователя",
			"first_name": "Имя",
			"last_name": "Фамилия",
			"position": "Должность",
			"working_days": "Рабочие дни",
			"working_hours": "Рабочие часы"
		},
		profile: undefined
	}),
	mounted() {
		axios
			.get("/auth/users/me")
			.then(response => {
				this.profile = response.data;
				console.log("response", this.profile);
			})
			.catch(error => {
				if (error.response.status === 401) { // unauthorized
					this.authStore.resetToken();
					this.$router.push({name: "SignIn"});
				} else {
					this.error = error.response?.data || error.message || "Что-то пошло не так";
					console.log(error)
				}
			})
			.finally(() => {
				this.loaded = true;
			})
	},
}
</script>
