<template>
    <AuthenticatedWrapComponent>
        <v-alert v-if="error" :text="error" type="error"></v-alert>
        <v-progress-circular
                v-if="!loaded"
                color="primary"
                indeterminate/>
        <div v-if="loaded">
            <h1>Персонал</h1>
            <v-text-field
                    v-model="staff_search"
                    class="mt-3"
                    label="Поиск сотрудника"
                    name="search"
            ></v-text-field>
            <v-data-table
                    :headers="headers"
                    :items="staff"
                    :items-per-page="5"
                    class="elevation-1">
            </v-data-table>
        </div>
    </AuthenticatedWrapComponent>
</template>

<script>

import AuthenticatedWrapComponent from "@/components/AuthenticatedWrapComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "Staff",
	components: {AuthenticatedWrapComponent},
	computed: {
		...mapStores(useAuthStore),
		staff() {
			if (this.staff_search)
				return this.staff_raw.filter(staff => staff.full_name.toLowerCase().includes(this.staff_search.toLowerCase()))
			return this.staff_raw;
		}
	},
	created() {
		this.authStore.init();
	},
	data: () => ({
		error: "",
		loaded: false,
		staff_search: "",
		staff_raw: undefined,
		headers: [
			{title: "ID", key: "id"},
			{title: "Имя", key: "full_name"},
			{title: "Должность", key: "position"},
			{title: "Рабочие дни", key: "working_days"},
			{title: "Рабочие часы", key: "working_hours"},
		]
	}),
	mounted() {
		axios
			.get("/staff")
			.then(response => {
				this.staff_raw = response.data;
				console.log("response", this.staff_raw);
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
