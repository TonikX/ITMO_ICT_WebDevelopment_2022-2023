<template>
    <div>
        <v-alert :text="error" v-if="error" type="error"/>
        <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
        <div v-if="loaded">
            <h1>Резюме для вакансии {{ vacancy_id }}</h1>
            <v-container class="border my-6" v-for="cv in cvs" v-bind:key="cv.id">
                <v-form class="mt-6" @submit.prevent="onSubmit(cv.id)">
                    <UserInfoComponent :user="cv.user"/>
                    <v-row class="border-b">
                        <v-col class="font-weight-bold">Образование</v-col>
                        <v-col>{{ cv.education }}</v-col>
                    </v-row>
                    <div class="header my-6">Специализация</div>
                    <v-list>
                        <v-list-item v-for="spec in cv.specializations" v-bind:key="spec.id">
                            {{ getSpecializationName(spec) }}
                        </v-list-item>
                    </v-list>
                    <div class="header my-6">Назначение на вакансию</div>
                    <div class="header my-6">ФИО: "{{ cv.user.first_name }} {{ cv.user.last_name }}"</div>
                    <div class="btns">
                        <v-btn
                                :to="{name:'CV', params: { id: cv.id}}">
                            Подробнее
                        </v-btn>
                        <v-btn type="submit" color="primary">
                            Направить кандидата
                        </v-btn>
                    </div>
                </v-form>
            </v-container>
        </div>
    </div>
</template>

<style scoped>
.header {
    font-size: 18pt;
    font-weight: bold;
}

.btns {
    display: flex;
    justify-content: space-between;
}
</style>


<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError, getSpecializationName} from "@/utils";
import {useRoute, useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import UserInfoComponent from "@/components/UserInfoComponent.vue";

const loaded = ref(false);
const error = ref("");
const cvs = ref([]);

const route = useRoute();
const router = useRouter();
const user = useUserStore();
const vacancy_id = ref(route.params.id);
const vacancy = ref({});
const vacancy_education_level = ref(0);
const vacancy_specs = ref([]);

const education_choices = [
	{key: "Middle", title: "Неоконченное среднее", value: 1},
	{key: "High", title: "Среднее", value: 2},
	{key: "Bachelor", title: "Бакалавр", value: 3},
	{key: "Master", title: "Магистр", value: 4},
];

function onSubmit(cv_id) {
    loaded.value = false;
	let patch = vacancy.value;
	patch.education_level = vacancy_education_level.value;
    patch.specs = vacancy_specs.value.map(spec_id => ({ "id": spec_id }));
    patch.choosen_candidate = cv_id;
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
        .get(`/company/my/vacancy/${vacancy_id.value}`)
        .then(response => {
            vacancy.value = response.data;
			vacancy_specs.value = vacancy.value.specs.map(spec => spec.id)
			vacancy_education_level.value = education_choices.find(education => education.key === vacancy.value.education_level).value;
            console.log(response.data);
            return axios.get(`/company/my/vacancy/${vacancy_id.value}/cvs`)
        })
		.then(response => {
            cvs.value = response.data;
            return response
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
