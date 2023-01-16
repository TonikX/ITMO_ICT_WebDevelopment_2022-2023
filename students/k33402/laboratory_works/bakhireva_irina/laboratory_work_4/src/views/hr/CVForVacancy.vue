<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Резюме для вакансии {{ vacancy_id }}</h1>
        <v-container class="border my-6" v-for="cv in cvs" v-bind:key="cv.id">
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
            <v-btn
                    :to="{name:'CV', params: { id: cv.id}}">
                Подробнее
            </v-btn>
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

onMounted(() => {
	axios
		.get(`/company/my/vacancy/${vacancy_id.value}/cvs`)
		.then(response => {
			cvs.value = response.data;
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
