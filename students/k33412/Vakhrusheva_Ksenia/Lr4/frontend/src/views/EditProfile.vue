<template>
    <AuthenticatedWrapComponent>
        <v-alert v-if="error" :text="error" type="error"></v-alert>
        <v-progress-circular
                v-if="!loaded"
                color="primary"
                indeterminate/>
        <div v-if="loaded">
            <h1>Редактирование профиля</h1>
            <div class="my-6" style="max-width:500px">
                <v-form @submit.prevent="submitForm">

                    <v-text-field
                            v-for="[key,title] of Object.entries(keys)"
                            v-model="profile[key]"
                            :label="title"
                            :name="key"
                            class="mt-3"
                    ></v-text-field>


                    <v-btn
                            color="primary"
                            type="submit">
                        Сохранить
                    </v-btn>
                </v-form>
            </div>
        </div>
    </AuthenticatedWrapComponent>
</template>

<script>
import AuthenticatedWrapComponent from "@/components/AuthenticatedWrapComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "EditProfile",
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
		valid: true,
		nonEmptyRules: [
			v => !!v || "Обязательное поле"
		],
		keys: {
			"first_name": "Имя",
			"last_name": "Фамилия",
			"position": "Должность",
			"working_days": "Рабочие дни",
			"working_hours": "Рабочие часы"
		},
		profile: {},
	}),
	methods: {
		submitForm() {
			const formData = this.profile;
			this.error = false;
			this.loaded = false;
			axios
				.patch("/auth/users/me/", formData)
				.then(response => {
					this.profile = response.data;
					console.log("response", this.profile);
				})
				.catch(error => {
					if (error.response.status === 401) { // unauthorized
						this.authStore.resetToken();
						this.$router.push({name: "SignIn"});
					} else {
						this.error = JSON.stringify(error.response?.data) || error.message || "Что-то пошло не так";
						console.log(error)
					}
				})
				.finally(() => {
					this.loaded = true;
				})
		}
	},
	mounted() {
		axios
			.get("/auth/users/me/")
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
