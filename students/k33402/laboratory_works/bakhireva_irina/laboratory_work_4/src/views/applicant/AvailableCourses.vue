<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Доступные курсы</h1>
        <div class="my-6">
            <CoursesListComponent :courses="courses"/>
        </div>
    </div>
</template>

<script setup>
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import {onMounted, ref} from "vue";
import axios from "axios";
import {getError} from "@/utils";
import CoursesListComponent from "@/components/CoursesListComponent.vue";

const loaded = ref(false);
const courses = ref([]);
const error = ref("");

const router = useRouter()
const user = useUserStore();

onMounted(() => {
	axios
		.get("/cv/my/courses_for_me/")
		.then(response => {
			courses.value = response.data;
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
