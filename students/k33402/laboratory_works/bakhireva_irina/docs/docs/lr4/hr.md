# Представления для HR агента

## HR.vue

Представление, которое отвечает за отрисовку вложенного роутинга. Так же проверяются права доступа пользователя к
дальнейшим представлениям.

```js
const router = useRouter()
const user = useUserStore();

onMounted(() => {
	if (!user.isHR) {
		user.updateToken();
		router.push({name: "Login"});
	}
})

```

## hr/AllCV.vue

Представление отображает список всех резюме в системе с информацией о пользователе, его специализации, обучении и
воможностью посмотреть более полную информацию.

```Vue

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
```

## hr/CreateVacancy.vue

Представление отображает форму для создания вакансии от лица текущей компании HR агента. Специализация заполняется
через `v-select` со множественным выбором, образование так же выбирается через `v-select`. Даты создания и закрытия
вакансии заполняются через внешний `Datepicker` из-за отсутствия такового в библиотеке `Vuetify 3`.

```Vue

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
```

## hr/CV.vue

Представление отображает подробную информацию о любом резюме по его идентификатору

## hr/CVForVacancy.vue

Представление отображает список резюме, доступных по требованиям, указанным в вакансии.

## hr/EditVacancy.vue

Представление отображает форму для редактирования существующей вакансии. Форма аналогична форме в представлении для создания вакансии (`hr/CreateVacancy.vue`).

## hr/MyCompany.vue

Представление отображает информацию о текущей компании HR агента. К каждому резюме компании добавляются два действия - просмотр списка резюме для данной вакансии и возможность отредактировать вакансию.

```Vue
<h1 class="my-6">Компания</h1>
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
<v-btn
	:to="{name:'CVForVacancy', params: {id: vacancy.id }}" class="me-3 mb-3">
	Найти резюме
</v-btn>

<v-btn
	:to="{name:'EditVacancy', params: {id: vacancy.id}}" class="me-3 mb-3">
	Редактировать вакансию
</v-btn>
</v-container>
```
