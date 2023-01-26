#Лабораторная работа №4 - Реализация клиентской части средствами Vue.js

####Лабораторная работа реализована и зачтена в рамках курса по [фронтенд-разработке](https://github.com/kantegory/ITMO-ICT-Frontend-2022).
##Цель 
* овладеть практическими навыками реализации клиентской части средствами Vue.js.
##Описание задачи:
Мигрировать ранее написанный сайт на фреймворк Vue.js.

##Листинги
###Роутер
* `router/index.js`
```json
import {createRouter, createWebHistory} from 'vue-router'
import AboutView from "@/views/AboutView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import MainView from "@/views/MainView.vue";
import WalletView from "@/views/WalletView.vue";
import ChartsView from "@/views/ChartsView.vue";



const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'about',
            component: AboutView
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView
        },
        {
            path: '/main',
            name: 'main',
            component: MainView
        },
        {
            path: '/personal',
            name: 'wallet',
            component: WalletView
        },
        {
            path: '/charts',
            name: 'chart',
            component: ChartsView
        },
    ]
})

export default router
```

###Компоненты
* `Header.vue` - header для авторизованного пользователя
```html
<template>
  <header class="d-flex justify-content-center py-3">
    <ul class="nav nav-pills">
      <li class="nav-item">
        <div class="nav-link pt-1">
          <svg class="nav-logo" style=" height: 27px">
            <use xlink:href="#logo">
            </use>
          </svg>
        </div>
      </li>
      <li class="nav-item"><a href="/main" class="nav-link">Купить криптовалюту</a></li>
      <li class="nav-item"><a href="#" @click="checkAuth" class="nav-link">Мой портфель</a></li>
<!--      <li class="nav-item"><a href="/charts" class="nav-link">Графики</a></li>-->
      <li class="nav-item" id="logout" :style="[this.isLogged ? {'display' : 'block'} : {'display' : 'none'}]">
        <button class="logout-button" @click="logout"
                style="border: none; background-color: white; padding-top:5px">
          <svg class="logout-img" style="width: 27px; height: 27px">
            <use xlink:href="#logout">
            </use>
          </svg>
        </button>
      </li>
    </ul>
  </header>
</template>

<script>
import router from "@/router";

export default {
  name: 'Header',
  data() {
    return {
      isLogged: false
    }
  },
  methods: {
    logout() {
      if (confirm('Вы действительно хотите выйти?')) {
        localStorage.clear()
        if (this.$route.path === '/personal') {
          router.push('/')
        } else {
          window.location.reload()
        }
      }
    },
    checkAuth() {
      if (!this.isLogged) {
        router.push('/login')
      } else {
        router.push('/personal')
      }
    }
  },
  mounted() {
    localStorage.getItem('pinia_users') ? this.isLogged = true : this.isLogged = false
  }
}
</script>

<style>
.nav-logo {
  width: 40%;
}

.nav-link {
  font-family: Tahoma, sans-serif;
  font-weight: bold;
  color: var(--link-color) !important;
}

.nav-link:hover {
  color: var(--link-hover) !important;
}
</style>
```

* `HeaderUnlogged.vue` - header для неавторизованного пользователя
```html
<template>
  <header class="d-flex justify-content-center px-10">
    <ul class="navigation-bar">
      <li class="nav-item">
        <a class="nav-link pt-1" href="#">
          <svg class="nav-logo" height="35px">
            <use xlink:href="#logo">
            </use>
          </svg>
        </a>
      </li>
      <li class="nav-item">
        <a href="/login" class="nav-link">Вход</a>
      </li>
    </ul>
  </header>
</template>

<script>
export default {
  name: 'HeaderUnlogged'
}
</script>

<style >
.navigation-bar {
  width: 100%;
  list-style-type: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 40px 8px 10px;
  margin: 0;
  border-bottom: 1px solid;
  border-bottom-color: var(--border-bottom);
}

.nav-link {
  font-family: Tahoma, sans-serif;
  font-weight: bolder;
  color: var(--link-color);
}

.nav-link:hover {
  color: var(--link-hover);
}

.nav-logo {
  width: 12%;
}
</style>
```

* `About.vue` - компонент стартовой страницы
```html
<template>
    <div class="container" style="padding-top: 100px">
        <div class="row">
            <div class="col-md-6">
                <div style="display: flex">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="HeroPill__NakedBitcoinIcon-sc-16ndsef-1 epDkoW"><path d="M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12z" fill="#1652F0"></path><path d="M17.274 10.515c.235-1.572-.962-2.417-2.599-2.981l.531-2.13-1.296-.323-.517 2.074c-.34-.086-.69-.165-1.039-.245l.521-2.087L11.58 4.5l-.53 2.13c-.283-.065-.56-.128-.829-.196l.002-.007-1.788-.446-.345 1.385s.962.22.942.234c.525.13.62.478.603.754L9.03 10.78c.036.01.083.023.135.043l-.137-.034-.848 3.4c-.064.158-.227.398-.595.307.014.019-.941-.235-.941-.235L6 15.745l1.688.42c.313.08.62.162.923.239l-.537 2.154 1.296.322.53-2.13c.355.096.698.184 1.034.268l-.53 2.121 1.297.323.536-2.15c2.211.419 3.873.25 4.573-1.75.564-1.61-.028-2.538-1.191-3.144.847-.195 1.485-.752 1.655-1.903zm-2.963 4.153c-.4 1.61-3.11.74-3.99.522l.713-2.854c.879.22 3.697.654 3.277 2.332zm.402-4.176c-.365 1.464-2.621.72-3.353.537l.645-2.587c.731.182 3.089.522 2.708 2.05z" fill="#fff"></path></svg>
                    <a href="/register" style="display: flex">&nbsp&nbspНачните формировать свой портфель</a>
                </div>
                <div>
                    <h1 style="font-size: 62px">
                        Начните<br>формировать<br>свой<br>криптовалютный<br>портфель
                    </h1>
                    <h3 style="font-size: 20px; line-height: 1.4">
                        Coinbase — самая удобная площадка для купли и продажи криптовалюты. Зарегистрируйтесь и начните прямо сегодня.
                    </h3>
                </div>
            </div>

            <div class="col-md-6" style="">
                <img src="@/assets/img/about_page.png" height="534px" width="526px" alt="">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'About'
}
</script>

<style scoped>

</style>
```

* `Register.vue` - компонент страницы регистрации
```html
<template @userrec>
  <section class="registration-page">
    <div class="container py-5 ">
      <div class="row justify-content-center align-items-center">
        <div class="col">
          <div class="card-registration">
            <div class="card-body">
              <p class="mb-10">Обязательные поля отмечены звездочкой: *</p>
              <form @submit.prevent="onRegSubmit">
                <div class="row">
                  <div class="col-3 mb-3 ">
                    <div class="form-outline">
                      <label class="form-label fw-bolder" for="firstName">Имя*</label>
                      <input v-model.trim.lazy="user.firstName" type="text" id="firstName"
                             class="form-control form-control-lg"
                             placeholder="Имя" name="firstName" autocomplete="off" required/>
                    </div>
                  </div>

                  <div class="col-md-3 mb-3">
                    <div class="form-outline">
                      <label class="form-label fw-bolder" for="lastName">Фамилия*</label>
                      <input v-model.trim.lazy="user.lastName" type="text" id="lastName"
                             class="form-control form-control-lg"
                             placeholder="фамилия" name="lastName" autocomplete="off" required/>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-11 mb-4 d-flex align-items-center">
                    <div class="form-outline w-100">
                      <label class="form-label fw-bolder" for="emailAddress">Электронная
                        почта*</label>
                      <input v-model.trim.lazy="user.email" type="email" id="emailAddress"
                             class="form-control form-control-lg"
                             placeholder="Электронная почта" name="email" autocomplete="off"
                             required/>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-11 mb-4 pb-2">
                    <div class="form-outline">
                      <label class="form-label fw-bolder" for="password">Пароль*</label>
                      <input v-model.trim.lazy="user.password" type="password" id="password"
                             class="form-control form-control-lg"
                             placeholder="Выберите пароль" name="password" autocomplete="off"
                             required/>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-11 mb-4">
                    <input class="form-check-input" type="checkbox" value="" id="invalidCheck" v-model="agree" required>
                    <label class="form-check-label" for="invalidCheck">
                      Я подтверждаю, что мне исполнилось 18, и принимаю положения следующих
                      документов: <a class="card-link"
                                     href="https://www.coinbase.com/legal/user_agreement">Пользовательское
                      Соглашение</a> и <a class="card-link m-0"
                                          href="https://www.coinbase.com/legal/privacy">Политика
                      конфеденциальности</a>.
                    </label>
                  </div>
                </div>

                <div class="row">
                  <div class="col-11">
                    <div class="d-grid gap-2 mt-20">
                      <button class="btn btn-primary fw-bolder" style="border-radius: 100px" type="submit" :disabled="!formReady">Создать учетную
                        запись
                      </button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {mapActions} from 'pinia';
import useUsersStore from "@/stores/users";
import router from "@/router";

export default {
  name: 'Register',
  data() {
    return {
      user: {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        coins: [],
      },
      agree: false
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['register']),
    async onRegSubmit() {

      await this.register(this.user);

    }
  },
  computed: {
    formReady() {
      return Object.values(this.user).every(value => value !== '') && this.agree
    }
  },
  beforeCreate() {
    localStorage.getItem('pinia_users') ? router.push('/personal') : router.push('/register')
  }
}
</script>

<style>
.form-check-label {
  font-size: 14px;
}

.form-control {
  height: 70px;
  border-radius: 8px;
}

.card-link {
  text-decoration: none;
}

.btn-primary {
  height: 70px;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}

.form-control {
  background-color: var(--bg-color);
  border-color: var(--border-input);
  color: var(--text-color);
}

.form-control:focus {
  background-color: var(--bg-color);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
  color: var(--text-color)
}

.btn-primary {
  background-color: var(--btn-color);
}

.btn-primary:hover {
  background-color: var(--btn-hover);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
}

.form-check-input:checked {
  background-color: var(--btn-hover);
  color: var(--btn-hover);
  box-shadow: 0 0 10px var(--btn-hover);
  border-color: var(--btn-hover);
}

.form-check-input:focus {
  box-shadow: 0 0 10px var(--btn-hover);
  border-color: var(--btn-hover);
}

.form-check-input {
  border-color: var(--btn-hover);
  margin-right: 10px;
}

a {
  color: var(--link-color);
}

a:hover {
  color: var(--link-hover);
}

@media (prefers-color-scheme: dark) {
  .nav-logo {
    filter: invert(10%);
  }
}
</style>
```

* `Login.vue` - компонент страницы авторизации
```html
<template>
  <section class="vh-100">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-start h-100">
        <div class="col-5">
          <div class="card" style="border-radius: 1rem;">
            <div class="card-body p-4">
              <div class="row p-3">
                <svg class="img-logo" href="/" style="height: 50px">
                  <use xlink:href="#logo">
                  </use>
                </svg>
              </div>

              <div class="row py-5 px-3">
                <h3 class="mb-0">Войдите в систему Coinbase</h3>
              </div>

              <form type="submit" @submit.prevent="onLogSubmit">
                <div class="row mb-4 px-3">
                  <div class="form-outline col-12 ">
                    <label class="form-label fw-bolder" for="typeEmailX">Электронная почта</label>
                    <input v-model.trim.lazy="user.email" type="email" id="typeEmailX"
                           class="form-control input form-control-md"
                           placeholder="Ваш адрес электронной почты" name="email" autocomplete="off"
                           required/>
                  </div>
                </div>

                <div class="row mb-4 px-3">
                  <div class="form-outline col-12  ">
                    <label class="form-label fw-bolder" for="typePasswordX">Пароль</label>
                    <input v-model.trim.lazy="user.password" type="password" id="typePasswordX"
                           class="form-control input form-control-md"
                           placeholder="Ваш пароль" name="password" autocomplete="off" required/>
                  </div>
                </div>

                <div class="row px-3">
                  <p class=" mb-4">
                    <a class="password-forgot" href="#">Забыли пароль?</a>
                  </p>
                </div>

                <div class="row px-3">
                  <a href="" class="login-link">
                    <button class="btn btn-primary col-12 mb-3" style="border-radius: 100px"
                            :disabled="!formReady" type="submit">Войти
                    </button>
                  </a>
                </div>
              </form>

              <div class="row px-3 mb-4">
                <a href="/register" class="">
                  <button class="btn btn-light col-12" style="border-radius: 100px" type="submit">Создать учетную запись</button>
                </a>
              </div>

              <div class="row col-md-6 mx-auto">
                <a href="#" class="extra-link">Войти в бизнес-аккаунт</a>
              </div>

              <div class="row col-md-7 mx-auto mb-2">
                <a href="https://www.coinbase.com/legal/privacy" class="extra-link">Политика
                  конфиденциальности</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>



<script>
import {mapActions} from "pinia";
import useUsersStore from "@/stores/users";
import router from "@/router";

export default {
  name: 'Login',
  data() {
    return {
      user: {
        email: "",
        password: "",
      }
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['signUp']),
    async onLogSubmit() {

      await this.signUp(this.user)

    }
  },
  computed: {
    formReady() {
      return Object.values(this.user).every(value => value !== '')
    }
  },
  beforeMount() {
    localStorage.getItem('pinia_users') ? router.push('/personal') : router.push('/login')
  }
}
</script>

<style>
.img-logo {
  width: 50% !important;
}

.container {
  padding-top: 100px;
}

.form-control {
  height: 60px;
  border-radius: 1rem;
}

.btn {
  height: 60px;
  border-radius: 100px;
}

.password-forgot {
  text-decoration: none;
}

.extra-link {
  text-decoration: none;
}

.btn-primary {
  background-color: var(--btn-color);
}

.btn-primary:hover {
  background-color: var(--btn-hover);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
}

body {
  background-color: var(--bg-color);
}

.card {
  background-color: var(--card-color);
  border-color: var(--border-input);
}

a {
  color: var(--link-color);
}

a:hover {
  color: var(--link-hover);
}

h3 {
  color: var(--text-color);
}

label {
  color: var(--text-color);
}

.form-control {
  background-color: var(--bg-color);
  border-color: var(--border-input);
  color: var(--text-color);
}

.form-control:focus {
  background-color: var(--bg-color);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
  color: var(--text-color)
}

.btn-light, .btn-light:hover {
  background-color: var(--btn-secondary);
  color: var(--text-color);
  border-color: var(--btn-secondary);
}

</style>
```

* `Personal.vue` - компонент страницы валютного портфеля пользователя
```html
<template>
  <section class="dataTable-wrapper">
    <div class="dataTable-wrapper d-flex justify-content-center">
      <table class="table align-middle border-light mt-5 w-75">
        <tr class="head-row border-light ">
          <th class="align-middle fw-bold">Название
<!--            <sort-button/>-->
          </th>
          <th class="align-middle fw-bold">Цена
<!--            <sort-button/>-->
          </th>
          <th class="fw-bold">Количество
<!--            <sort-button/>-->
          </th>
          <th class="fw-bold">Итого</th>
          <th class="fw-normal">
            <div class="">
              <select-sort
                  v-model="sortName"
                  :options="sortOptions"
              />
            </div>
          </th>
          <th class="d-flex justify-content-center">
            <div>
              <p class="balance m-0">Баланс:</p>
              <p class="balance fw-light m-0">{{ balance() }}
              </p>
            </div>
          </th>
        </tr>
        <wallet :coins="coins" @buyEvent="buyCoin" @sellEvent="sellCoin"/>
      </table>
    </div>
  </section>
</template>

<script>
import Wallet from "@/components/lists/Wallet.vue";
import {mapActions, mapState} from "pinia";
import useCoinsStore from "@/stores/coins";
import useUsersStore from "@/stores/users";

export default {
  name: 'Personal',
  components: {
    Wallet
  },
  data() {
    return {
      coins: [],
      sortName: '',
      sortOptions: [
        {value: 'name ASC', name: 'По названию (ASC)'},
        {value: 'name DESC', name: 'По названию (DESC)'},
        {value: 'current_price ASC', name: 'По цене (ASC)'},
        {value: 'current_price DESC', name: 'По цене (DESC)'},
        {value: 'amount ASC', name: 'По количеству (ASC)'},
        {value: 'amount DESC', name: 'По количеству (DESC)'},
      ]
    }
  },
  methods: {
    ...mapActions(useCoinsStore, ['getWallet', "loadCoins", "loadCustomCoins"]),
    ...mapActions(useUsersStore, ['commitActions']),

    async getCoins() {
      let current = await this.getWallet(this.user.id);
      const data = await this.loadCustomCoins()
      for (let i = 0; i < current.coins.length; i++) {
        for (let j = 0; j < data.length; j++) {
          if (current.coins[i].id === data[j].id) {
            this.coins[i] = data[j]
            this.coins[i].amount = current.coins[i].amount
          }
        }
      }
    },

    balance() {
      let res = 0;
      for (let i = 0; i < this.coins.length; i++) {
        res += this.coins[i].amount * this.coins[i].current_price;
      }
      return res.toFixed(2)
    },

    async buyCoin(id, amount) {
      let newCoin = true
      for (let i = 0; i < this.user.coins.length; i++) {
        if (id === this.user.coins[i].id) {
          this.user.coins[i].amount += amount
          newCoin = false
        }
      }

      if (newCoin) {
        this.user.coins.push({id: id, amount: amount})
      }

      await this.commitActions(this.user);
      await this.getCoins()
    },

    async sellCoin(id, amount) {
      let index;
      for (let i = 0; i < this.user.coins.length; i++) {
        if (id === this.user.coins[i].id) {
          this.user.coins[i].amount -= amount;
          index = i;
        }
      }

      if (this.user.coins[index].amount === 0) {
        this.user.coins = this.user.coins.filter(coin => coin.id !== id)
      }

      await this.commitActions(this.user);
      await this.getCoins()
      location.reload()
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user'])
  },
  mounted() {
    this.getCoins()
  },
  watch: {
    async sortName(sortName) {
      const sortSplit = sortName.split(' ')
      const type = sortSplit[0]
      const order = sortSplit[1]
      if (type === 'name') {
        this.coins.sort((a, b) => a[type].localeCompare(b[type]))
      } else {
        this.coins.sort((a, b) => a[type] - b[type])
      }
      if (order === 'DESC') {
        this.coins.reverse()
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Tahoma', sans-serif
}

.table {
  border: 2px solid;
}

.head-row {
  border-bottom: 2px solid;
  font-weight: normal;
}

.head-row {
  font-weight: normal;
}

.table thead th {
  padding: 30px;
  font-weight: normal;
}

.dataTable-wrapper {
  margin: 20px auto;
  overflow-x: auto
}


::placeholder {
  color: black;
  font-weight: 600;
}


.table tbody td {
  padding: 30px;
  margin: 0;
}

.btn-pagination {
  border: none;
  background-color: white;
  margin-left: 15px;
}


body {
  background-color: var(--bg-color) !important;
  color: var(--text-color) !important;
  border-color: var(--card-color) !important;
}

.page-number {
  border-color: var(--text-color);
}

tr {
  border-color: var(--card-color) !important;
}
</style>
```

* `Main.vue` - компонент страницы покупки криптовалюты
```html
<template>
  <section class="dataTable-wrapper d-flex justify-content-center">
    <table class="table align-middle mt-5 w-75 bg-white border-light">
      <tr class="search-row p-2 bg-light">
        <td colspan="2" class="align-middle search-header  justify-content-between">
          <div class="form d-flex">
            <search-input v-model="search" @send-search="findCoins" style="width: 350px !important;"/>
          </div>
        </td>
        <td colspan="3" class="">
          <div class="d-flex justify-content-end">
            <select-sort
                v-model="sortName"
                :options="sortOptions"
            />
          </div>
        </td>
      </tr>
      <tr class="head-row p-2 border-light">
        <th class="fw-normal ps-4 align-middle">Название
          <sort-button v-model="sortName"/>
        </th>
        <th class="fw-normal align-middle">Цена
          <sort-button/>
        </th>
        <th class="fw-normal align-middle">Изменение
          <sort-button/>
        </th>
        <th class="fw-normal align-middle">Дата добавления
          <sort-button/>
        </th>
        <th class="fw-normal">
          <div class="pagination d-flex justify-content-center align-content-center p-0">
            <button class="btn-pagination m-0 btn-prev" @click="getPrevPage" :style="[this.page > 1 ? {'display' : 'block'} : {'display':'none'}]">
              <svg style="width: 30px; height: 30px;">
                <use xlink:href="#arrow">
                </use>
              </svg>
            </button>
            <div class="page-number m-0 mx-1"
                 style="display: flex; justify-content: center">
              <input v-model="page">
            </div>
            <button class="btn-pagination btn-next m-0" @click="getNextPage" :style="[this.page < 3 ? {'display' : 'block'} : {'display':'none'}]">
              <svg style="width: 30px; height: 30px; transform: rotate(180deg)">
                <use xlink:href="#arrow">
                </use>
              </svg>
            </button>
          </div>
        </th>
      </tr>
      <coins-list :coins="coins" @buyEvent="buyCoin"/>
    </table>
  </section>
</template>

<script>
import useCoinsStore from "@/stores/coins";
import {mapActions, mapState} from "pinia";
import CoinsList from "@/components/lists/CoinsList.vue";
import useUsersStore from "@/stores/users";


export default {
  name: 'Main',
  components: {
    CoinsList
  },
  data() {
    return {
      coins: [],
      page: 1,
      limit: 10,
      total: 3,
      search: '',
      sortName: '',
      sortOptions: [
        {value: 'name ASC', name: 'По названию (ASC)'},
        {value: 'name DESC', name: 'По названию (DESC)'},
        {value: 'current_price ASC', name: 'По цене (ASC)'},
        {value: 'current_price DESC', name: 'По цене (DESC)'},
        {value: 'price_change_percentage_24h ASC', name: 'По изменению (ASC)'},
        {value: 'price_change_percentage_24h DESC', name: 'По изменению (DESC)'},
        {value: 'atl_date ASC', name: 'По дате (ASC)'},
        {value: 'atl_date DESC', name: 'По дате (DESC)'},
      ]
    }
  },
  methods: {
    ...mapActions(useCoinsStore, ['loadCoins']),
    ...mapActions(useUsersStore, ['commitActions']),
    async getCoins() {
      this.coins = await this.loadCoins(this.search, this.sortName);
    },
    buyCoin(id, amount) {
      let newCoin = true
      for (let i = 0; i < this.user.coins.length; i++) {
        if (id === this.user.coins[i].id) {
          this.user.coins[i].amount += amount;
          newCoin = false;
        }
      }
      if (newCoin) {
        this.user.coins.push({id: id, amount: amount});
      }

      this.commitActions(this.user);
    },
    async findCoins() {
      this.coins = await this.loadCoins(this.search, this.sortName);
    },
    async getPrevPage() {
      if (this.page > 1) {
        this.page--;
        this.coins = await this.loadCoins(this.search, this.sortName, this.page);
      }

    },
    async getNextPage() {
      if (this.page < this.total) {
        this.page++;
        this.coins = await this.loadCoins(this.search, this.sortName, this.page);
      }
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user'])
  },
  mounted() {
    this.getCoins();
  },
  watch: {
    async sortName(sortName) {
      this.coins = await this.loadCoins(this.search, sortName);
    }
  }
}
</script>

<style scoped>
.table {
  border: 2px solid var(--card-color) !important;
}

.head-row {
  border-bottom: 2px solid;
  font-weight: normal;
}


.btn-pagination {
  border: none;
  background-color: white;
  margin-left: 15px;
}


.page-number {
  border-color: var(--text-color);
  border: 2px solid;
  border-radius: 20px;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
}

tr {
  border-color: var(--card-color);
}

input {
  width: 9px;
  height: 20px;
  border: none;
}

</style>
```

###Представления
* `AboutView.vue` - стартовая страница
```html
<template>
    <HeaderUnlogged/>
    <About/>
</template>

<script>
import HeaderUnlogged from "@/components/headers/HeaderUnlogged.vue";
import About from "@/components/About.vue";

export default {
    components: {
        HeaderUnlogged,
        About
    }
}
</script>
```

* `RegisterView.vue` - страница регистрации
```html
<template>
  <HeaderUnlogged/>
  <Register/>
</template>

<script>
import Register from "@/components/auth/Register.vue";
import HeaderUnlogged from "@/components/headers/HeaderUnlogged.vue";

export default {
  components: {
    Register,
    HeaderUnlogged
  }
}
</script>
```

* `LoginView.vue` - страница авторизации
```html
<template>
  <div>
    <Login/>
  </div>
</template>

<script>
import Login from "@/components/auth/Login.vue";

export default {
  components: {
    Login
  }
}
</script>
```

* `WalletView.vue` - валютный портфель пользователя
```html
<template>
    <Header/>
    <Personal/>
    <br>
    <chart/>
</template>

<script>
import Header from "@/components/headers/Header.vue";
import Personal from "@/components/Personal.vue";
import {Chart} from "vue-tradingview-widgets";

export default {
  components: {
    Header,
    Personal,
    Chart
  }
}
</script>
```

* `MainView.vue` - страница покупки криптовалюты
```html
<template>
  <Header/>
  <Main/>
</template>

<script>
import Main from "@/components/Main.vue";
import Header from "@/components/headers/Header.vue";

export default {
  components: {
    Header,
    Main
  }
}
</script>
```

###API
* `api/index.js`
```json
import instance from "@/api/instance.js";
import CoinsAPI from "@/api/coins.js";
import UsersAPI from "@/api/users.js";
import ChartsAPI from "@/api/charts.js";

const coinsAPI = new CoinsAPI(instance);
const usersAPI = new UsersAPI(instance);
const chartsAPI = new ChartsAPI(instance);

export {
    coinsAPI,
    usersAPI,
    chartsAPI
}
```

* `instance.js`
```json
import axios from "axios";

const apiURL = 'http://localhost:3000'

const instance = axios.create({
    baseURL: apiURL
})

export default instance
```

* `users.js`
```json
export default class UsersAPI {
    constructor(instance) {
        this.API = instance
    }

    getAllUsers = async () => {
        return this.API({
            method: 'GET',
            url: '/users'
        })
    }

    getCurrentUser = async (id) => {
        return this.API({
            method: 'GET',
            url: `/users/${id}`
        })
    }

    push = async (user) => {
        return this.API({
            method: 'PUT',
            url: `/users/${user.id}`,
            data: user,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }


    createNewUser = async (data) => {
        return this.API({
            method: 'POST',
            url: '/users',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
}
```

* `coins.js`
```json
class CoinsAPI {
    constructor(instance) {
        this.API = instance
    }

    getCoins = async (search, sort, order, page, limit) => {
        return this.API({
            url: `/coins?q=${search}&_sort=${sort}&_order=${order}&_limit=${limit}&_page=${page}`
        })
    }

    getCustomList = async () => {
        return this.API({
            url: `/coins`
        })
    }
}

export default CoinsAPI
```

###Stores
* `stores/index.js`
```json
import { persist } from 'pinia-persists'
import { createPinia } from 'pinia'

const pinia = createPinia()

pinia.use(persist())

export default pinia
```

* `users.js`
```json
import {usersAPI} from "@/api";
import {defineStore} from "pinia"
import router from "@/router";


const useUsersStore = defineStore('users', {
    state: () => ({
        user: {
            id: null,
            coins: []
        }
    }),

    actions: {
        async signUp(credentials) {
            const response = await usersAPI.getAllUsers()
            const data = response.data

            const validUser = this.isValid(credentials, data)

            if (validUser !== undefined) {
                this.user.id = validUser.id;
                this.user.coins = validUser.coins;
                await router.push('/personal')
            } else {
                localStorage.clear()
                alert('Ошибка! Проверьте email или пароль')
            }
        },

        isValid(credentials, data) {
            for (let i = 0; i < data.length; i++) {
                if (data[i].email === credentials.email && data[i].password === credentials.password) {
                    return {id: data[i].id, coins: data[i].coins}
                }
            }
        },

        async commitActions(user) {
            const rawUser = JSON.parse(JSON.stringify(user))
            const currentUser = await usersAPI.getCurrentUser(rawUser.id)
            currentUser.data.coins = rawUser.coins
            const response = await usersAPI.push(currentUser.data)
            return response.data
        },

        async register(credentials) {
            const response = await usersAPI.createNewUser(credentials)
            const data = response.data

            let {id} = data

            this.user = {
                'id': id,
                'coins': [],
            }
        }
    }
})

export default useUsersStore
```

* `coins.js`
```json
import {defineStore} from "pinia";
import {coinsAPI, usersAPI} from "@/api";

const useCoinsStore = defineStore('coins', {
    state: () => ({
        coins: []
    }),
    actions: {
        async loadCoins(search = '', sortName = '', page = 1, limit = 10) {
            const sortSplit = sortName.split(' ');
            const sort = sortSplit[0];
            const order = sortSplit[1];
            const response = await coinsAPI.getCoins(search, sort, order, page, limit);
            this.coins = response.data;
            return response.data;
        },
        async getWallet(idx) {
            const actual = await usersAPI.getCurrentUser(idx);
            const {id, coins} = actual.data;
            return {id, coins};
        },
        async loadCustomCoins() {
            const response = await coinsAPI.getCustomList();
            this.coins = response.data;
            return response.data;
        },
        async loadCoinsList(search = '') {
            const response = await coinsAPI.getCoins(search, '', '', '', '');
            this.coins = response.data;
            return response.data;
        }
    }
})

export default useCoinsStore
```