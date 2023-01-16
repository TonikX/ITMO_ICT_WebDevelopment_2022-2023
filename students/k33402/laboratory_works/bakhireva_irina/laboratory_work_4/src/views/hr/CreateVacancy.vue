<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Создание вакансии</h1>
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

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError, getSpecializationName} from "@/utils";
import {useUserStore} from "@/stores/user";

const loaded = ref(false);
const error = ref("");
const router = useRouter();
const user = useUserStore();
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
const vacancy_education_level = ref(education_choices[0].value);
const vacancy_specs = ref([]);

function onSubmit() {
	loaded.value = false;
	let create = vacancy.value;
	create.education_level = vacancy_education_level.value;
	create.specs = vacancy_specs.value.map(spec_id => ({"id": spec_id}));
	console.log(create);
	axios
		.post(`/company/my/vacancys/`, create)
		.then(() => {
			router.push({name: "MyCompany"})
		})
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
		.get(`/specializations/`)
		.then(response => {
			specializations.value = response.data.map(specialization => ({
				...specialization,
				full: getSpecializationName(specialization)
			}))
		})
		.finally(() => {
			loaded.value = true;
		})
})
</script>
