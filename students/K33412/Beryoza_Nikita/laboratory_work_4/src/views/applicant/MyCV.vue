<template>
    <div>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Мое резюме</h1>
        <h2>Информация о пользователе</h2>
        <v-container class="my-6">
            <UserInfoComponent :user="cv_user"/>
        </v-container>
        <h2>История работы</h2>
        <div class="my-6">
            <WorkHistoryComponent :work_history="cv_work_history"/>
        </div>
        <h2>История Образования</h2>
        <div class="my-6">
            <EducationListComponent :education="cv_education"/>
        </div>
        <h2>Доступные курсы</h2>
        <div class="my-6">
            <AvailableCoursesListComponent :courses="cv_courses"/>
        </div>
    </div>
    </div>
</template>

<script setup>
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import {computed, onMounted, ref} from "vue";
import axios from "axios";
import {getError} from "@/utils";
import WorkHistoryComponent from "@/components/WorkHistoryComponent.vue";
import UserInfoComponent from "@/components/UserInfoComponent.vue";
import EducationListComponent from "@/components/EducationListComponent.vue";
import AvailableCoursesListComponent from "@/components/AvailableCoursesListComponent.vue";

const loaded = ref(false);
const error = ref("");
const cv = ref({});
const cv_user = computed(() => cv.value.user);
const cv_work_history = computed(() => cv.value.work_history);
const cv_education = computed(() => cv.value.education);
const cv_courses = computed(() => cv.value.courses);

const router = useRouter()
const user = useUserStore();

onMounted(() => {
	axios
		.get("/cv/my/")
		.then(response => {
            cv.value = response.data;
            console.log(cv.value.user);
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
