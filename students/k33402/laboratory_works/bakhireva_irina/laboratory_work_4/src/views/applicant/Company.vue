<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1 class="my-6">Компания {{ company_id }}</h1>
        <CompanyInfoComponent :company="company"/>
        <h1 class="my-6">HR</h1>
        <HRInfoComponent :hr="company.hr.user"/>
        <h1 class="my-6">Вакансии</h1>
        <v-container class="border my-6" v-for="vacancy in company.vacancies" v-bind:key="vacancy.id">
            <VacancyInfoComponent :vacancy="vacancy"/>
            <div class="header my-6">Специализация</div>
            <v-list>
                <v-list-item v-for="spec in vacancy.specs" v-bind:key="spec.id">
                    {{ getSpecializationName(spec) }}
                </v-list-item>
            </v-list>
        </v-container>
    </div>
</template>

<style scoped>
.header {
    font-size: 18pt;
    font-weight: bold;
}
</style>

<script setup>

import {useRoute, useRouter} from "vue-router";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError, getSpecializationName} from "@/utils";
import {useUserStore} from "@/stores/user";
import HRInfoComponent from "@/components/HRInfoComponent.vue";
import CompanyInfoComponent from "@/components/CompanyInfoComponent.vue";
import VacancyInfoComponent from "@/components/VacancyInfoComponent.vue";

const loaded = ref(false);
const error = ref("");
const router = useRouter();
const route = useRoute();
const user = useUserStore();
const company_id = ref(route.params.id);
const company = ref({});

onMounted(() => {
	axios
		.get(`/company/${company_id.value}`)
		.then(response => {
			company.value = response.data;
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

</script>
