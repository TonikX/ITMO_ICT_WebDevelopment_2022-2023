<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Подходящие вакансии</h1>
        <VacancyListComponent :vacancys="vacancys"/>
    </div>
</template>

<script setup>
import VacancyListComponent from "@/components/VacancyListComponent.vue";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError} from "@/utils";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";

const loaded = ref(false);
const error = ref("");
const vacancys = ref([]);

const router = useRouter();
const user = useUserStore();

onMounted(() => {
	axios
		.get("/cv/my/vacancys")
		.then(response => {
			vacancys.value = response.data;
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
