# Лабораторная работа 4. Реализация клиентской части средствами Vue.js.

## Работа с курса по Фронтенд разработки

Мигрировать ранее написанный сайт на фреймворк Vue.JS.

Минимальные требования:

1 Должен быть подключён роутер

2 Должна быть реализована работа с внешним API

3 Разумное деление на компоненты

* `router/index.js`

Роутер и все доступные нам urlы на которые можно зайти

```js
import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CalendarView from '@/views/CalendarView.vue'
import PersonalView from '@/views/PersonalView.vue'
import EntryView from '@/views/EntryView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import EventView from '@/views/EventView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: MainView
		},
		{
			path: '/calendar/',
			name: 'calendar',
			component: CalendarView
		},
		{
			path: '/personal/',
			name: 'personal',
			component: PersonalView
		},
		{
			path: '/entry/',
			name: 'entry',
			component: EntryView
		},
		{
			path: '/registration/',
			name: 'registration',
			component: RegistrationView
		},
		{
			path: '/event/',
			name: 'event',
			component: EventView
		},
	]
})

export default router
```

## Дальше представлены все компоненты нашего сайта

* `Card.vue`

Шаблон карточки для подгрузки в mainPage

```vue
<template>
  <img :src="src" class="card-img-top" width="262" :alt="description" style="height: 11rem;">
  <div class="card-body">
    <h3 class="card-title">{{ title }}</h3>
    <p class="card-text">{{ description }}</p>
    <p class="card-data">{{ date }}</p>
  <a href="./event.html" class="btn btn-primary">На сайт мероприятия</a>
  <form action="" @submit.prevent="subscribe(id)">
    <button type="submit" class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
      <svg class="icon-main"><use xlink:href="#register-icon"></use></svg>
      Записаться
    </button>
  </form>
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useUserEventsStore from "@/stores/userEvents.js"

export default {
  name: 'CardNote',

  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
  },

  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    },
    src: {
      type: String,
      required: true
    },
    id: {
      type: Number,
      required: true
    },
  },

  methods: {
    ...mapActions(useUserEventsStore, ['addUserEvents']),

    async subscribe(id) {
      const userEvents = {
        "userId": JSON.parse(localStorage.user).id,
        "eventId": id
      }

      console.log(userEvents)

      const response = await this.addUserEvents(userEvents);

      console.log(response)
    }
  }
}

</script>
```

* `PersonalCard.vue`

Шаблон карточки для личного кабинета

```vue
<template>
  <img :src="src" class="card-img-top" width="262" :alt="description" style="height: 11rem;">
  <div class="card-body">
    <h3 class="card-title">{{ title }}</h3>
    <p class="card-text">{{ description }}</p>
    <p class="card-data">{{ date }}</p>
  <form action="" @submit.prevent="deleteCard(primaryId)">
    <button type="submit" class="btn btn-danger mt-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Отписаться от мероприятия
    </button>
  </form>
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useUserEventsStore from "@/stores/userEvents.js"

export default {
  name: 'PersonalCard',
  
  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
  },

  methods: {
    ...mapActions(useUserEventsStore, ['addUserEvents', 'deleteCardById']),

    async deleteCard(id) {
      this.deleteCardById(id)

      location.reload()
    }
  },

  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    },
    src: {
      type: String,
      required: true
    },
    primaryId: {
      type: Number,
      required: true
    },
  },
}

</script>
```

* `Entry.vue`

Компонента входа

```vue
<template>
  <main class="container-xl p-5 mb-5">
    <form class="d-flex-column" @submit.prevent="login">
      <h1 class="row mb-5 justify-content-center">Вход</h1>
      <div class="row mb-3 justify-content-center">
        <label for="email" class="col-sm-1 col-form-label">Почта</label>
        <div class="col-sm-3 col-md-4">
          <input type="text" class="form-control" v-model="form.email" name="email" id="email">
        </div>
      </div>
      <div class="row mb-3 justify-content-center">
        <label for="password" class="col-sm-1 col-form-label">Пароль</label>
        <div class="col-sm-3 col-md-4">
          <input type="password" class="form-control" v-model="form.password" name="password" id="password">
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-sm-4 col-md-5">
          <button type="submit" class="btn btn-primary" :to="{ path: '/' }">Войти</button>
          <a class="btn btn-primary" href="./reqistration.html" role="button">Зарегистрироваться</a>
        </div>
      </div>
    </form>
  </main>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import router from '@/router'

import useLoginStore from '../stores/login'

export default {
  name: 'EntryBlock',

  data() {
    return {
      form: {
        email: "",
        password: ""
      }
    };
  },

  methods: {
    ...mapActions(useLoginStore, ['userLogin']),

    async login() {
      const response = await this.userLogin(this.form);

      const { accessToken, user } = response.data

      localStorage.accessToken = accessToken
      localStorage.user = JSON.stringify(user)

      localStorage.accessToken ? router.push('/') : router.push('')
    }
  }
}
</script>
```

* `Registration.vue`

Компонента регистрации

```vue
<template>
	<main class="container-xl p-5">
		<form class="d-flex-column" @submit.prevent="register">
			<h1 class="row mb-5 justify-content-center">Регистрация</h1>
			<div class="row mb-3 justify-content-center">
				<label for="inputName3" class="col-sm-1 col-form-label">Имя</label>
				<div class="col-sm-3">
					<input type="text" class="form-control" v-model="form.firstname" name="firstname" id="inputName3" placeholder="Алексей" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputSurname3" class="col-sm-1 col-form-label">Фамилия</label>
				<div class="col-sm-3">
					<input type="text" class="form-control" v-model="form.lastname" name="lastname" id="inputSurname3" placeholder="Кондратьев" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputEmail3" class="col-sm-1 col-form-label">Почта</label>
				<div class="col-sm-3">
					<input type="email" class="form-control" v-model="form.email" name="email" id="inputEmail3" placeholder="example@email.com" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputLogin3" class="col-sm-1 col-form-label">Логин</label>
				<div class="col-sm-3">
					<input type="text" class="form-control" v-model="form.login" name="login" id="inputLogin3" placeholder="9Anpanman" required>
				</div>
			</div>
			<div class="row mb-3 justify-content-center">
				<label for="inputPassword3" class="col-sm-1 col-form-label">Пароль</label>
				<div class="col-sm-3">
					<input type="password" class="form-control" v-model="form.password" name="password" id="inputPassword3" required>
				</div>
			</div>
			<div class="row justify-content-center">
				<div class="col-sm-4">
					<button type="submit" class="btn btn-primary">Зарегистрироваться</button>
				</div>
			</div>
		</form>
	</main>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import router from '@/router'

import useRegisterStore from '../stores/register'

export default {
	name: 'RegistrationBlock',

  data() {
    return {
      form: {
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        login: ""
      }
    };
  },

  methods: {
    ...mapActions(useRegisterStore, ['userRegister']),

    async register() {
      const response = await this.userRegister(this.form);

      const { accessToken, user } = response.data

      localStorage.accessToken = accessToken
      localStorage.user = JSON.stringify(user)

      localStorage.accessToken ? router.push('/') : router.push('')
    }
  }
}
</script>
```

* `Header.vue`

Хедер для каждой странички

```vue
<template>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" display="none">
    <symbol id="personal-area" width="16" height="16" viewBox="0 0 16 16">
      <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-5 6s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zM11 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5zm.5 2.5a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1h-4zm2 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2zm0 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2z"/>
    </symbol>

    <symbol id="calendar" viewBox="0 0 16 16">
        <path d="M11 6.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
        <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
    </symbol>

    <symbol id="exit-door" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
      <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
    </symbol>

    <symbol id="entry-door" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
      <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
    </symbol>

    <symbol id="main-icon" viewBox="0 0 16 16">
      <path d="M8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4.5a.5.5 0 0 0 .5-.5v-4h2v4a.5.5 0 0 0 .5.5H14a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146zM2.5 14V7.707l5.5-5.5 5.5 5.5V14H10v-4a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v4H2.5z"/>
    </symbol>

    <symbol id="register-icon" viewBox="0 0 16 16">
      <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
    </symbol>
  </svg>

  <header class="container-fluid colors">
    <nav class="navbar navbar-expand-md d-flex justify-content-between">
      <div>
        <a class="colors navbar-brand text-color fs-4 p-2" href="#" @click="$router.push('/')">Главная <svg class="icon-main"><use xlink:href="#main-icon"></use></svg></a>
        <a class="colors navbar-brand text-color fs-6 p-2" href="#" @click="$router.push('/calendar/')">Календарь <svg class="icon-main"><use xlink:href="#calendar"></use></svg></a>
      </div>
      <div>
        <button class="colors navbar-brand text-color fs-6" id="entry" @click="$router.push('/entry/')">Вход <svg class="icon-main"><use xlink:href="#entry-door"></use></svg></button>
        <button class="colors navbar-brand text-color fs-6 button-logout" id="exit" @click="logout">Выход <svg class="icon-main"><use xlink:href="#exit-door"></use></svg></button>
        <button class="colors navbar-brand text-color fs-6" id="register" @click="$router.push('/registration/')">Регистрация <svg class="icon-main"><use xlink:href="#register-icon"></use></svg></button>
        <button class="colors navbar-brand text-color fs-5 p-2" id="lc" @click="$router.push('/personal/')">
          Личный кабинет
          <svg class="icon-main">
            <use class="icon-main" xlink:href="#personal-area"></use>
          </svg>
        </button>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'HeaderBlock',

  methods: {
    check() {
      const entryButton = document.querySelector('#entry');
      const registerButton = document.querySelector('#register');
      const exitButton = document.querySelector('#exit');

      if (localStorage.accessToken) {
        entryButton.classList.add('d-none');
        registerButton.classList.add('d-none');
        exitButton.classList.remove('d-none');
      } else {
        entryButton.classList.remove('d-none');
        registerButton.classList.remove('d-none');
        exitButton.classList.add('d-none');
      }
    },

    logout() {
      localStorage.clear();

      document.querySelector('#entry').classList.remove('d-none');
      document.querySelector('#register').classList.remove('d-none');
      document.querySelector('#exit').classList.add('d-none');
    }
  },

  mounted() {
    this.check()
  }
}

</script>
```

* `Footer.vue`

Футер для каждой страницы

```vue
<template>
	<footer class="container-fluid pt-5 colors">
		<div class="row justify-content-between p-2">
			<div class="col-2 text-color">
				<h3>Ваш аккаунт</h3>
				<ul class="nav flex-column">
					<li class="nav-item mb-2"><a href="./personal-area.html" class="nav-link p-0 text-color">Личный кабинет</a></li>
					<li class="nav-item mb-2"><a href="./entry.html" class="nav-link p-0 text-color">Вход</a></li>
					<li class="nav-item mb-2"><a href="./reqistration.html" class="nav-link p-0 text-color">Регистрация</a></li>
				</ul>
			</div>

			<div class="col-2 text-color">
				<h3>Найти</h3>
				<ul class="nav flex-column">
					<li class="nav-item mb-2"><a href="./calendar.html" class="nav-link p-0 text-color">Календарь</a></li>
					<li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-color">Поиск мероприятий</a></li>
				</ul>
			</div>

			<div class="col-2 text-color">
				<h3>О нас</h3>
				<ul class="nav flex-column">
					<li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-color">ВКонтакте</a></li>
					<li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-color">Телеграм</a></li>
				</ul>
			</div>

			<div class="col-4 offset-1">
				<form>
					<h3 class="text-color">Подпишись на нас, чтобы не пропустить ничего интересного</h3>
					<div class="d-flex w-100 gap-2">
						<label for="newsletter1" class="visually-hidden">Ваша почта</label>
						<input id="newsletter1" type="text" class="form-control" placeholder="example@email.com">
						<button class="btn btn-primary" type="button">Подписаться</button>
					</div>
				</form>
			</div>
		</div>

		<div class="d-flex justify-content-between py-4 my-4 mb-0 border-top text-color">
			<p>&copy 2022, Кондратьев Алексей</p>
		</div>
	</footer>
</template>

<script>
export default{
	name: 'FooterBlock',
}

</script>
```

* `Main.vue`

Компонента основной страницы

```vue
<template>
  <svg display="none">
    <symbol id="search-icon" viewBox="0 0 16 16">
      <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
    </symbol>
  </svg>

  <main class="container-fluid background-main">
    <section class="row row-cols-2 pt-5">
      <div class="d-flex flex-column justify-content-center align-items-end col-5">
        <h1 class="w-75 h1 pb-3 text-color">События обьединяют</h1>
        <p class="w-75 pt-6 text-color">Посещайте конференции и лекции, ходите на выставки и концерты, занимайтесь саморазвитием и ищите единомышленников</p>
      </div>
      <img class="w-50" src="../assets/image/people.png" alt="Радующиеся люди">
    </section>

    <section class="d-flex flex-column align-items-center pt-5">
      <h2 class="h2 mb-4 text-color">Актуальные мероприятия</h2>
      <div class="d-flex justify-content-center m-0">
        <p class="fs-5 pe-3 text-color">Сортировать</p>
        <div class="dropdown me-3">
          <select class="form-select-sm event-type" aria-label=".form-select-lg example">
            <option value="ALL">Выберите, чем хотите заняться</option>
            <option value="Спорт">Спорт</option>
            <option value="Музыка">Музыка</option>
          </select>
        </div>
        <div class="dropdown me-3">
          <select class="form-select-sm city-type" aria-label=".form-select-lg example">
            <option value="ALL">Выберите город</option>
            <option value="Москва">Москва</option>
            <option value="Санкт-Петербург">Санкт-Петербург</option>
          </select>
        </div>
        <form class="search-form d-flex justify-content-end col-12 col-sm-2 col-lg-4 col-xl-6" @submit.prevent="filter">
          <button type="submit" id="search" class="btn btn-info btn-sm" style="background-color:#d2cb60; border: 1px solid #d2cb60;">
            Поиск
            <svg class="icon-main"><use xlink:href="#search-icon"></use></svg>
          </button>
        </form>
      </div>
      <div class="row justify-content-center pt-5">
        <div class="card me-4 card-colors background text-color mb-3" style="width: 18rem;" data-event-id="{{ id }}" v-for="card in filteredCards" :key="card.id">
          <card-note :title="card.title" :src="card.src" :description="card.description" :date="card.date" :id="card.id"></card-note>
        </div>
      </div>
    </section>
    
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h3 class="modal-title" id="exampleModalLabel">Вы записаны</h3>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Ждем вас на нашем мероприятие с хорошим настроением
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useCardsStore from "@/stores/cards.js"

import CardNote from "@/components/Card.vue"

export default {
  name: 'MainBlock',

  components: { CardNote },

  computed: {
    ...mapState(useCardsStore, ['cards']),

    filteredCards() {
      if (this.selectedCards.length) {
        return this.selectedCards;
      } else {
        return this.cards
      }
    }
  },

  methods: {
    ...mapActions(useCardsStore, ['loadCards']),

    async filter() {
      const eventT = document.querySelector('.event-type')
      const cityT = document.querySelector('.city-type')
      this.selectedCards = []

      console.log(eventT.value, cityT.value)
      this.cards.forEach((card) => {
        if ((eventT.value === card.mero && cityT.value === card.city) || (eventT.value === "ALL" && cityT.value === card.city) || (eventT.value === card.mero && cityT.value === "ALL")) {
          this.selectedCards.push(card);
        }
      })
    }
  },

  data() {
    return {
      selectedCards: []
    }
  },

  mounted() {
    this.loadCards();
  }
}
</script>
```

* `Personal.vue`

Компонента личного кабинета

```vue
<template>
  <main class="container-fluid background-main">
    <section class="pt-5 pb-5">
      <div class="d-flex flex-column align-items-center pt-5 pb-5">
        <div class="d-flex flex-column align-items-center">
          <h1 class="h2 p-0 mb-2 text-color">Ваш личный кабинет</h1>
          <p class="p-0 m-2 text-color">Ваши записи</p>
          <div class="row justify-content-center pt-5 pb-5">
            <div class="card me-4 card-colors background text-color mb-3" style="width: 18rem;" data-event-id="{{ id }}" v-for="card in personalCards" :key="card.id">
              <personal-card :title="card.title" :src="card.src" :description="card.description" :date="card.date" :primaryId="card.primaryId"></personal-card>
            </div>
          </div>
        </div>
        <div class="row justify-content-center" id="container">
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h2 class="modal-title" id="exampleModalLabel">Оповещение</h2>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  Вы были отписаны от мероприятия
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useCardsStore from "@/stores/cards.js"
import useUserEventsStore from "@/stores/userEvents.js"

import PersonalCard from "@/components/PersonalCard.vue"

export default {
  name: 'PersonalBlock',

  components: { PersonalCard },

  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
    ...mapState(useCardsStore, ['personalCards']),
  },

  methods: {
    ...mapActions(useUserEventsStore, ['getUserEventsById']),
    ...mapActions(useCardsStore, ['loadCardById', 'doClear']),

    async loadPage() {
      const response = await this.getUserEventsById(JSON.parse(localStorage.user).id);

      const result = Array.from(response.data);

      this.doClear();
      result.forEach((item) => {
        this.loadCardById(item.eventId, item.id)
      })
    }
  },

  mounted() {
    this.loadPage();
  }
}
</script>
```


* `FullCalendar.vue`

Компонента календаря

```vue
<template>
  <full-calendar :options="calendarOptions" />
</template>

<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

const DEFAULT_OPTIONS = {
  plugins: [ dayGridPlugin, interactionPlugin ],
  initialView: 'dayGridMonth',
  editable: true
}

export default {
  components: {
    FullCalendar
  },

  props: {
    options: {
      type: Object,
      default: DEFAULT_OPTIONS
    }
  },

  computed: {
    calendarOptions() {
      return { ...DEFAULT_OPTIONS, ...this.options }
    }
  }
}
</script>

<style>
.fc-day {
  cursor: pointer;
}
</style>
```

## Дальше представлены все файлы с API в нашей работе

* `index.js`

Файл с обьявлением всех API

```js
import instance from "@/api/instance.js"
import CardApi from "@/api/cards.js"
import CalendarEventsApi from "@/api/calendarEvents"
import LoginApi from "@/api/login";
import RegisterApi from "@/api/register";
import UserEventsApi from "@/api/userEvents";

const cardApi = new CardApi(instance);
const calendarEventsApi = new CalendarEventsApi(instance);
const loginApi = new LoginApi(instance);
const registerApi = new RegisterApi(instance);
const userEventsApi = new UserEventsApi(instance);

export { cardApi, calendarEventsApi, loginApi, registerApi, userEventsApi }
```

* `instance.js`

```js
import axios from 'axios'

const apiURL = 'http://localhost:3000'

const instance = axios.create({
	baseURL: apiURL
})

export default instance
```

* `cards.js`

API получения карточек

```js
export default class CardApi {
  constructor(instance) {
    this.API = instance
  }

  getAll = async () => {
    return this.API({
      url: '/events'
    })
  }

  getById = async (id) => {
    return this.API({
      url: `/events/${id}`
    })
  }
}
```

* `calendarEvents.js`

API для календаря

```js
class CalendarEventsApi {
  constructor(instance) {
    this.API = instance
  }

  getAll = async () => {
    return this.API({
      url: '/calendarEvents'
    })
  }

  getById = async (id) => {
    return this.API({
      url: `/calendarEvents/${id}`
    })
  }

  deleteEv = async (id) => {
    return this.API({
      url: `/calendarEvents/${id}`,
      method: 'DELETE'
    })
  }

  create = async (data) => {
    return this.API({
      url: '/calendarEvents',
      method: 'POST',
      data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }

}

export default CalendarEventsApi
```

* `login.js`

API для логина

```js
export default class LoginApi {
  constructor(instance) {
    this.API = instance
  }

  userLogin = async (data) => {
    return this.API({
      method: 'POST',
      url: '/login',
      data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }
}
```

* `register.js`

API для регистрации

```js
export default class RegisterApi {
  constructor(instance) {
    this.API = instance
  }

  userRegister = async (data) => {
    return this.API({
      method: 'POST',
      url: '/register',
      data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }
}
```

* `userEvents.js`

API для userEvents

```js
export default class UserEventsApi {
  constructor(instance) {
    this.API = instance
  }

  getAll = async () => {
    return this.API({
      url: '/userEvents'
    })
  }

  getById = async (id) => {
    return this.API({
      url: `/userEvents?userId=${id}`
    })
  }

  deleteById = async (id) => {
    return this.API({
      url: `/userEvents/${id}`,
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }

  createUserEvent = async (data) => {
    return this.API({
      url: '/userEvents',
      method: 'POST',
      data,
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }
}
```

## Все stores в проекте

* `index.js`

Общий store с pinia

```js
import { persist } from 'pinia-persists'
import { createPinia } from 'pinia'

const pinia = createPinia()

pinia.use(persist())

export default pinia
```

* `cards.js`

```js
import { defineStore } from 'pinia'
import { cardApi } from '@/api'

const useCardsStore = defineStore('cards', {
  state: () => ({
    cards: [],
    personalCards: []
  }),

  actions: {
    async loadCards() {
      const response = await cardApi.getAll();

      this.cards = response.data;

      return response;
    },

    async loadCardById(eventId, id) {
      const response = await cardApi.getById(eventId);

      response.data.primaryId = id;

      this.personalCards.push(response.data)

      return response
    },

    async doClear() {
      this.personalCards = []
    }
  }
})

export default useCardsStore
```

* `login.js`

store для логина

```js
import { defineStore } from 'pinia'
import { loginApi } from '@/api'

const useLoginStore = defineStore('users', {
  state: () => ({
    users: []
  }),

  actions: {
    async userLogin(data) {
      const response = await loginApi.userLogin(data)

      this.users = response.data

      return response
    }
  }
})

export default useLoginStore
```

* `register.js`

store для регистрации

```js
import { defineStore } from 'pinia'
import { registerApi } from '@/api'

const useRegisterStore = defineStore('users', {
  state: () => ({
    users: []
  }),

  actions: {
    async userRegister(data) {
      const response = await registerApi.userRegister(data)

      this.users = response.data

      return response
    }
  }
})

export default useRegisterStore
```

* `usrEvents.js`

store для userEvents

```js
import { defineStore } from 'pinia'
import { userEventsApi } from '@/api'

const useUserEventsStore = defineStore('userEvents', {
  state: () => ({
    userEvents: []
  }),

  actions: {
    async getUserEventsById(id) {
      const response = await userEventsApi.getById(id)

      return response
    },

    async addUserEvents(data) {
      const response = await userEventsApi.createUserEvent(data)

      this.userEvents = response.data

      return response
    },

    async deleteCardById(id) {
      const response = await userEventsApi.deleteById(id);

      return response
    }
  }
})

export default useUserEventsStore
```

* `calendarEvents.js`

store для calendarEvents

```js
import { defineStore } from 'pinia'
import { calendarEventsApi, cardApi } from '@/api'

const useCalendarEventsStore = defineStore('calendarEvents', {
  state: () => ({
    calendarEvents: [],
    selectedEvent: { title: '', date: '', description: '', id: "" }
  }),

  actions: {
    async loadCalendarEvents() {
      const response = await calendarEventsApi.getAll();
      const response2 = await cardApi.getAll();

      const jsonResponse = Array.from(response2.data);

      this.calendarEvents = response.data

      response2.data.forEach((item) => {
        this.calendarEvents.push(item)
      })
      
      console.log(this.calendarEvents)

      return response
    },

    async loadEventById(id) {
      this.selectedEvent = { title: '', date: '', description: '', id: '' }

      const response = await calendarEventsApi.getById(id)
      // const response = await cardApi.getById(id)

      this.selectedEvent = response.data

      return response
    },

    async createEvent(data) {
      const response = await calendarEventsApi.create(data)

      return response
    },

    async deleteEvent(id) {
      const response = await calendarEventsApi.deleteEv(id)

      return response
    }
  }
})

export default useCalendarEventsStore
```

## Все наши views, а именно странички

* `EntryView.vue`

Страничка для авторизации

```vue
<template>
  <header-block />
  <entry-block />
  <footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import useLoginStore from '../stores/login'

import HeaderBlock from '../components/Header.vue'
import EntryBlock from '../components/Entry.vue'
import FooterBlock from '../components/Footer.vue'

export default{
  name: 'EntryPage',

  components: { HeaderBlock, EntryBlock, FooterBlock },

  computed: {
    ...mapState(useLoginStore, ['users'])
  }
}
</script>
```

* `RegistrationView.vue`

Страничка регистрации нового пользователя

```vue
<template>
  <header-block />
  <registration-block />
  <footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import useRegisterStore from '../stores/register'

import HeaderBlock from '../components/Header.vue'
import RegistrationBlock from '../components/Registration.vue'
import FooterBlock from '../components/Footer.vue'

export default{
  name: 'RegistrationPage',

  components: { HeaderBlock, RegistrationBlock, FooterBlock },

  computed: {
    ...mapState(useRegisterStore, ['users'])
  }
}
</script>
```

* `MainView.vue`

Главная страничка проекта

```vue
<template>
	<header-block />
	<main-block />
	<footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import useCardsStore from '@/stores/cards'

import HeaderBlock from '@/components/Header.vue'
import MainBlock from '@/components/Main.vue'
import FooterBlock from '@/components/Footer.vue'

export default{
	name: 'MainPage',

	components: { HeaderBlock, MainBlock, FooterBlock },

  computed: {
    ...mapActions(useCardsStore, ['cards'])
  },

  methods: {
    ...mapActions(useCardsStore, ['loadCards']),
  },
}
</script>
```

* `PersonalView.vue`

Страничка личного кабинета

```vue
<template>
	<header-block />
	<personal-block />
	<footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import HeaderBlock from '../components/Header.vue'
import PersonalBlock from '../components/Personal.vue'
import FooterBlock from '../components/Footer.vue'

export default {
	name: 'PersonalPage',

	components: { HeaderBlock, PersonalBlock, FooterBlock }
}
</script>
```

* `CalendarView.vue`

Страничка с нашим календарем

```vue
<template>
  <header-block />
  <base-layout>
    <h1>Календарь событий</h1>

    <full-calendar
      :options="{
        events: calendarEvents,
        eventChange: handleEventChange,
        dateClick: handleDateClick,
        eventClick: handleEventClick
      }"
    />

    <!-- Modal -->
    <div class="modal fade" ref="detailEvent" tabindex="-1" aria-labelledby="detailEventLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="detailEventLabel">{{ selectedEvent.title }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p><strong>Описание:</strong> {{ selectedEvent.description }}</p>

            <p>{{ selectedEvent.formattedDate() }}</p>
          </div>
          <div class="modal-footer">
            <form action="" @submit.prevent="deleteMero(selectedEvent.id)">
              <button type="submit" class="btn btn-danger">Удалить</button>
            </form>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" ref="eventCreate" tabindex="-1" aria-labelledby="eventCreateLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="eventCreateLabel">Добавить событие</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm" class="d-flex flex-column" ref="eventForm">
              <input type="text" v-model="form.title" class="my-1">
              <input type="date" v-model="form.date" class="my-1">
              <textarea cols="30" rows="10" v-model="form.description" class="my-1" />

              <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </base-layout>
  <footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'
import { Modal } from 'bootstrap'

import useCalendarEventsStore from '@/stores/calendarEvents'

import BaseLayout from '@/layouts/BaseLayout.vue'
import HeaderBlock from '@/components/Header.vue'
import FullCalendar from '@/components/FullCalendar.vue'
import FooterBlock from '@/components/Footer.vue'

export default {
  name: 'CalendarPage',

  components: { BaseLayout, FullCalendar, HeaderBlock, FooterBlock},

  computed: {
    ...mapState(useCalendarEventsStore, {
      calendarEvents: 'calendarEvents',
      selectedEvent: (state) => {
        return {
          ...state.selectedEvent,
          formattedDate: () => {
            const date = state.selectedEvent.date
            return new Date(date).toLocaleDateString('ru-RU')
          }
        }
      }
    })
  },

  data() {
    return {
      form: {
        title: '',
        description: '',
        date: ''
      },

      eventCreateModal: null
    }
  },

  methods: {
    ...mapActions(useCalendarEventsStore, ['loadCalendarEvents', 'loadEventById', 'createEvent', 'deleteEvent']),

    handleEventChange(payload) {
      console.log('event change', payload)
    },

    handleDateClick(payload) {
      console.log('date clicked', payload)

      const { dateStr } = payload
      this.form.date = dateStr

      this.eventCreateModal = new Modal(this.$refs.eventCreate)
      this.eventCreateModal.show()
    },

    async handleEventClick(payload) {
      await this.loadEventById(payload.event._def.publicId)

      const eventModal = new Modal(this.$refs.detailEvent)
      eventModal.show()
    },

    async submitForm() {
      await this.createEvent(this.form)

      this.$refs.eventForm.reset()
      this.eventCreateModal.hide()

      await this.loadCalendarEvents()
    },

    async deleteMero(id) {
      this.deleteEvent(id);

      location.reload();
    }
  },

  mounted() {
    this.loadCalendarEvents()
  }
}
</script>
```

## Вывод

Мы переписали наш сайт с помощью фреймворка Vue.JS и научились работать с ним