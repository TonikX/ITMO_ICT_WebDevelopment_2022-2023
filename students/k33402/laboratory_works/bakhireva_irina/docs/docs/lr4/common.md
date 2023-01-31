# Общие представления и компоненты

## HomeView.vue

"Домашная" страница. Если пользователь не авторизован, отправляет его обратно на страницу авторизации, иначе отправляет
пользователя на страницу просмотра профиля.

## LoginView.vue

Страница авторизации. Использует компонент `LoginFormComponent.vue`. На странице присутствует форма из 2 полей и
компонент для отображения ошибок.

```Vue

<v-form @submit.prevent="onSubmit">
<v-alert :text="error" v-if="error" type="error"/>
<v-text-field v-model="username" name="username" label="Логин"/>
<v-text-field v-model="password" name="password" type="password" label="Пароль"/>
<v-btn color="primary" type="submit">Войти</v-btn>
</v-form>
```

## RegisterView.vue

Страница регистрации. Использует компонент `RegisterFormComponent.vue`. На странице присутствует форма, которая
генерируется для заранее заготовленного набора полей, и компонент для отображения ошибок.

```js
const fields = [
	{title: "Логин", key: "username"},
	{title: "Пароль", key: "password"},
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
];
```

```Vue

<v-form @submit.prevent="onSubmit">
<v-alert :text="error" v-if="error" type="error"/>
<v-text-field v-for="field in fields"
              v-bind:key="field.key"
              v-model="profile[field.key]"
              :name="field.key"
              :label="field.title"/>
<v-btn color="primary" type="submit">Зарегистрироваться</v-btn>
</v-form>
```

## common/EditProfile.vue

Представление для редактирование профиля пользователя. Отредактировать можно ограниченный набор полей, по которому
строится форма.

```js
const fields = [
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
]
```

```Vue

<v-form @submit.prevent="onSubmit">
<v-alert :text="error" v-if="error" type="error"/>
<v-text-field v-for="field in fields"
              v-bind:key="field.key"
              v-model="profile[field.key]"
              :name="field.key"
              :label="field.title"/>
<v-btn color="primary" type="submit">Сохранить</v-btn>
</v-form>
```

## common/Logout.vue

Представление, которое очищает данные об авторизации и возвращает пользователя на форму авторизации.

```js
onMounted(() => {
	if (user.isAuth) {
		axios
			.post("/auth/token/logout/")
			.finally(() => {
				user.updateToken();
				router.push({name: "Login"});
			});
	}
});
```

## common/Profile.vue

Представление отображает всю общедоступную информацию о текущем пользовательском аккаунте, которая представлена в объекте.

```js
const headers = [
	{title: "ID", key: "id"},
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
	{title: "Роль", key: "role"}
].filter(header => user.value[header.key] !== undefined);
```

```Vue

<v-row v-for="header in headers" v-bind:key="header.key" class="border-b">
<v-col class="font-weight-bold">{{ header.title }}</v-col>
<v-col>{{ user[header.key] }}</v-col>
</v-row>
```

## stores/user.js

Хранилище, в котором сохраняются объекты токена для авторизации пользователя и пользовательская роль. Токен записывается
в число заголовков, отправляемых при каждом запросе на сервер библиотекой `axios`. При изменении данные сохраняются в
локальное хранилище (`localStorage`).

```js
const token = ref(localStorage.getItem("token"));
const role = ref(localStorage.getItem("role"));

if (token.value) axios.defaults.headers.common["Authorization"] = `Token ${token.value}`;
else axios.defaults.headers.common["Authorization"] = "";
```

```js
function updateToken(newToken = "", newRole = "") {
	token.value = newToken;
	role.value = newRole;

	if (newToken) axios.defaults.headers.common["Authorization"] = `Token ${newToken}`;
	else axios.defaults.headers.common["Authorization"] = "";

	localStorage.setItem("token", newToken);
	localStorage.setItem("role", newRole);
}
```

## router/index.js

Роутер для навигации между представлениями. Каждому представлению определяется адрес, имя и указывается компонент,
который необходимо рендерить. Индивидуальные представления реализованы через вложенные пути (аттрибут `children`).

