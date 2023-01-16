<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Компании</h1>
        <div class="my-6">
            <CompanyListComponent :companys="companys"/>
        </div>
    </div>
</template>

<script setup>
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError} from "@/utils";
import CompanyListComponent from "@/components/CompanyListComponent.vue";

const loaded = ref(false);
const companys = ref([]);
const error = ref("");

const router = useRouter()
const user = useUserStore();

onMounted(() => {
	axios
		.get("/companys/")
		.then(response => {
			companys.value = response.data;
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
