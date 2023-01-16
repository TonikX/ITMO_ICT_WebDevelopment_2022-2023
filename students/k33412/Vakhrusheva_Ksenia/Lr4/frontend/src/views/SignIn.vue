<template>
    <UnauthenticatedWrapComponent>
        <v-form v-model="valid" class="mt-3" @submit.prevent="submitForm">
            <v-alert v-if="error" :text="error" type="error"></v-alert>
            <v-text-field
                    v-model="username"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Имя пользователя"
                    name="username"
                    required
            ></v-text-field>
            <v-text-field
                    v-model="password"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Пароль"
                    name="password"
                    required
                    type="password"
            ></v-text-field>

            <div class="d-flex mt-3 align-center flex-column flex-sm-row">
                <v-btn
                        :disabled="!valid"
                        color="primary"
                        type="submit"
                >
                    Войти
                </v-btn>

                <span class="mx-3 py-1">
                    или
                </span>

                <v-btn
                        :to="{name:'SignUp'}"
                        variant="text"
                >
                    Зарегистрироваться
                </v-btn>
            </div>
        </v-form>
    </UnauthenticatedWrapComponent>
</template>

<script>

import UnauthenticatedWrapComponent from "@/components/UnauthenticatedWrapComponent.vue";
import axios from "axios";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";

export default {
	name: "SignIn",
	components: {UnauthenticatedWrapComponent},
	data: () => ({
		valid: false,
		nonEmptyRules: [
			v => !!v || "Обязательное поле"
		],
		username: "",
		password: "",
		error: "",
		$store: null,
	}),
	computed: {
		...mapStores(useAuthStore),
	},
	methods: {
		submitForm(e) {
			const formData = {
				username: this.username,
				password: this.password,
			}

			axios
				.post("/auth/token/login", formData)
				.then(response => {
					const token = response.data.auth_token;
					this.authStore.setToken(token);
					axios.defaults.headers.common["Authorization"] = `Token ${token}`;
					this.$router.push({name: "Staff"});
				})
				.catch(error => {
					this.error = JSON.stringify(error.response?.data) || error.message || "Что-то пошло не так";
					console.log(error)
				})
		}
	}
}
</script>

<style scoped>
form {
    width: 500px;
    max-width: 100%;
}
</style>
