# Представления для соискателя

## Applicant.vue

Представление, которое отвечает за отрисовку вложенного роутинга. Так же проверяются права доступа пользователя к
дальнейшим представлениям.

```js
const router = useRouter()
const user = useUserStore();

onMounted(() => {
	if (!user.isApplicant) {
		user.updateToken();
		router.push({name: "Login"});
	}
})

```

## applicant/AvailableCourses.vue

Представление отображает список доступных для прохождения соискателем курсов. Список доступных курсов получается при
отрисовке страницы и рендерится через `v-data-table` с заменой шаблона для полей со специализацией, чтобы оставить
только название.

```Vue

<v-data-table
	:items="courses"
	:headers="headers"
	class="elevation-1">
<template v-slot:item.spec="{ item }">
	{{ getSpecializationName(item.raw.spec) }}
</template>
<template v-slot:item.required_spec="{ item }">
	{{ item.raw.required_spec ? getSpecializationName(item.raw.required_spec) : "-" }}
</template>
</v-data-table>
```

## applicant/Companies.vue

Представление отображает список всех компаний в информационной системе. Список компаний отображается
через `v-data-table` с одним кастомным шаблоном со ссылкой на более подробную информацию о компании.

```Vue

<v-data-table
	:items="companys"
	:headers="headers"
	class="elevation-1">
<template v-slot:item.info="{ item }">
	<v-btn
		:to="{name: 'Company', params: { id: item.raw.id}}">
		Подробнее
	</v-btn>
</template>
</v-data-table>
```

## applicant/Company.vue

Представление отображает всю информацию о конкретной компании по ее идентификатору из адресной строки. Информация отрисовывается с использованием нескольких компонентов, каждый из которых отвечает за отрисовку своей части информации.

```Vue
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
```

## applicant/MyCV.vue

Представление отображает всю информацию о текущем резюме соискателя. Информация отрисовывается с использованием нескольких компонентов, каждый из которых отвечает за отрисовку своей части информации.

```Vue
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
```

```js
const cv = ref({});
const cv_user = computed(() => cv.value.user);
const cv_work_history = computed(() => cv.value.work_history);
const cv_education = computed(() => cv.value.education);
const cv_courses = computed(() => cv.value.courses);
```

## applicant/VacanciesForMe.vue

Представление отображает список вакансий, доступных с текущим резюме пользователя. 

```Vue
<v-container class="border my-6" v-for="vacancy in vacancys">
<div class="header my-6">Вакансия</div>
<VacancyInfoComponent :vacancy="vacancy"/>

<div class="header my-6">Специализация</div>
<v-list>
	<v-list-item v-for="spec in vacancy.specs" v-bind:key="spec.id">
		{{ getSpecializationName(spec) }}
	</v-list-item>
</v-list>

<div class="header my-6">Компания</div>
<CompanyInfoComponent :company="vacancy.company"/>

<div class="header my-6">HR</div>
<HRInfoComponent :hr="vacancy.company.hr.user"/>
</v-container>
```
