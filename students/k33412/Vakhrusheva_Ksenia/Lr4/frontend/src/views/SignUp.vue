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

            <v-text-field
                    v-model="first_name"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Имя"
                    name="first_name"
                    required
            ></v-text-field>

            <v-text-field
                    v-model="last_name"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Фамилия"
                    name="last_name"
                    required
            ></v-text-field>

            <v-text-field
                    v-model="position"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Должность"
                    name="position"
                    required
            ></v-text-field>

            <v-text-field
                    v-model="working_days"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Рабочие дни"
                    name="working_days"
                    required
            ></v-text-field>

            <v-text-field
                    v-model="working_hours"
                    :rules="nonEmptyRules"
                    class="mt-3"
                    label="Рабочие часы"
                    name="working_hours"
                    required
            ></v-text-field>

            <div class="d-flex mt-3 align-center flex-column flex-sm-row">
                <v-btn
                        :disabled="!valid"
                        color="primary"
                        type="submit"
                >
                    Зарегистрироваться
                </v-btn>

                <span class="mx-3 py-1">
                    или
                </span>

                <v-btn
                        :to="{name:'SignIn'}"
                        variant="text"
                >
                    Войти
                </v-btn>
            </div>
        </v-form>
    </UnauthenticatedWrapComponent>
</template>

<script>

import UnauthenticatedWrapComponent from "@/components/UnauthenticatedWrapComponent.vue";
import axios from "axios";

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
		first_name: "",
		last_name: "",
		position: "",
		working_days: "",
		working_hours: "",
		error: "",
	}),
	methods: {
		submitForm(e) {
			const formData = {
				username: this.username,
				password: this.password,
				first_name: this.first_name,
				last_name: this.last_name,
				position: this.position,
				working_days: this.working_days,
				working_hours: this.working_hours,
			}

			axios
				.post("/auth/users/", formData)
				.then(response => {
					this.$router.push({name: "SignIn"})
				})
				.catch(error => {
					this.error = error.response?.data || error.message || "Что-то пошло не так";
					console.log(error)
				})
		}
	}
}
</script>

<style scoped>
form {
    width: 550px;
    max-width: 100%;
}
</style>
