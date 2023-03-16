<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Редактирование вакансии {{ vacancy_id }}</h1>
        <v-form class="mt-6" @submit.prevent="onSubmit">
            <v-select
                    v-model="vacancy_specs"
                    :items="specializations"
                    item-title="full"
                    item-value="id"
                    label="Специализации"
                    multiple>
            </v-select>
            <v-select
                    v-model="vacancy_education_level"
                    :items="education_choices"
                    item-title="title"
                    item-value="value"
                    label="Уровень образования">
            </v-select>
            <v-text-field v-for="field in fields"
                          v-bind:key="field.key"
                          v-model="vacancy[field.key]"
                          :name="field.key"
                          :label="field.title"/>
            <div class="mb-6">
                <label>
                    Дата добавления
                    <DatepickerComponent class="mt-3" v-model="vacancy.created_date"
                                         showNowButton></DatepickerComponent>
                </label>
            </div>
            <div class="mb-6">
                <label>
                    Дата закрытия
                    <DatepickerComponent class="mt-3" v-model="vacancy.closed_date" showNowButton></DatepickerComponent>
                </label>
            </div>
            <v-btn type="submit" color="primary">
                Сохранить
            </v-btn>
        </v-form>
    </div>
</template>

<script setup>

import {useRoute, useRouter} from "vue-router";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError, getSpecializationName} from "@/utils";
import {useUserStore} from "@/stores/user";

const loaded = ref(false);
const error = ref("");
const route = useRoute();
const router = useRouter();
const user = useUserStore();
const vacancy_id = ref(route.params.id);
const vacancy = ref({});
const specializations = ref([]);

/* -- */

const fields = [
	{title: "Требуемый стаж", key: "seniority"},
	{title: "Зарплата", key: "salary"},
	{title: "Описание", key: "description"},
]

const education_choices = [
	{key: "Middle", title: "Неоконченное среднее", value: 1},
	{key: "High", title: "Среднее", value: 2},
	{key: "Bachelor", title: "Бакалавр", value: 3},
	{key: "Master", title: "Магистр", value: 4},
];
const vacancy_education_level = ref(0);
const vacancy_specs = ref([]);

function onSubmit() {
	loaded.value = false;
	let patch = vacancy.value;
	patch.education_level = vacancy_education_level.value;
	patch.specs = vacancy_specs.value.map(spec_id => ({"id": spec_id}));
	console.log(patch);
	axios
		.patch(`/company/my/vacancy/${vacancy_id.value}/`, patch)
		.catch(axiosError => {
			if (axiosError.response.status === 401) {
				user.updateToken();
				router.push({name: "Login"});
			} else {
				error.value = getError(axiosError)
			}
		})
		.finally(() => {
			loaded.value = true
		})
}

onMounted(() => {
	axios
		.get(`/company/my/vacancy/${vacancy_id.value}/`)
		.then(response => {
			vacancy.value = response.data;
			vacancy_specs.value = vacancy.value.specs.map(spec => spec.id)
			vacancy_education_level.value = education_choices.find(education => education.key === vacancy.value.education_level).value;
			console.log(response.data)
			return axios.get(`/specializations/`);			
		})
		.then(response => {
			specializations.value = response.data.map(specialization => ({
				...specialization,
				full: getSpecializationName(specialization)
			}))
		})
		.catch(axiosError => {
			if (axiosError.response?.status === 401) {
				user.updateToken();
				router.push({name: "Login"});
			} else {
				error.value = getError(axiosError)
			}
		}).finally(() => loaded.value = true)
})

</script>
