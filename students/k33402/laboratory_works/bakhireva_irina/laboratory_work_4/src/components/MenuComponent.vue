<template>
    <div class="d-flex flex-column justify-center align-center">
        <h1>Hello {{ role }}</h1>
        <v-tabs align-with-title>
            <v-tab
                    v-for="item in getMenu(role)"
                    :key="item.key"
                    :to="{name: item.key}"
                    slider-color="primary"
            >
                {{ item.title }}
            </v-tab>
        </v-tabs>
    </div>
</template>

<script setup>
import {useUserStore} from "@/stores/user";
import {computed} from "vue";

const user = useUserStore();
const role = computed(() => user.role || "guest");

function getMenu(role) {
	switch (role) {
		case "HR":
			// edit vacancy, create vacancy
			return [
				{title: "Моя компания", key: "MyCompany"},
				{title: "Создать вакансию", key: "CreateVacancy"},
				{title: "Все резюме", key: "AllCV"},
				{title: "Профиль", key: "Profile"},
				{title: "Редактировать профиль", key: "EditProfile"},
				{title: "Выйти", key: "Logout"}
			]
		case "Applicant":
			return [
				// get company, get vacancy
				{title: "Резюме", key: "MyCV"},
				{title: "Доступные курсы", key: "AvailableCourses"},
				{title: "Мои вакансии", key: "VacanciesForMe"},
				{title: "Компании", key: "Companies"},
				{title: "Профиль", key: "Profile"},
				{title: "Редактировать профиль", key: "EditProfile"},
				{title: "Выйти", key: "Logout"}
			]
		default:
			return [
				{title: "Авторизация", key: "Login"},
				{title: "Регистрация", key: "Register"},
			]
	}
}

</script>
