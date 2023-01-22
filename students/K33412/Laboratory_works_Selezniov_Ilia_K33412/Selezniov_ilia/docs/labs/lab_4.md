#Лабораторная работа 4. Реализация клиентской части средствами Vue.js.
## Цель работы: Ознакомится с базовыми конструкциями JavaScript. Текст "Практической работы №4.1 (сдавать не нужно, можно не делать, если базово знаете JS).

* router `index.js`
```js
import {createRouter, createWebHistory} from 'vue-router'
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import MainView from "@/views/MainView.vue";
import WalletView from "@/views/WalletView.vue";
import ChartsView from "@/views/ChartsView.vue";
import Mainpage from "@/views/Mainpage.vue";



const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
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
            path: '/search',
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
        {
            path: '/',
            name: 'mainpage',
            component: Mainpage
        }
    ]
})

export default router

```

* реализация api
* `coins.js`
```js
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
* `users.js`
```js
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

* `index.js`

```js
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
```js
import axios from "axios";

const apiURL = 'http://localhost:3000'

const instance = axios.create({
    baseURL: apiURL
})

export default instance
```

* управление состоянием
* `coins.js`
```js
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
* `users.js`
```js
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

* `index.js`
```js
import { persist } from 'pinia-persists'
import { createPinia } from 'pinia'

const pinia = createPinia()

pinia.use(persist())

export default pinia
```