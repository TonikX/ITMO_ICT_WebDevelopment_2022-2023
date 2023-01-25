# Лабораторная работа 4

## Структура проекта

- `LR4` - основная директория веб-приложения
- `LR4/src` - исходный код исходного кода фронтенда приложения
- `LR4/src/components` - компоненты приложения
- `LR4/src/pages` - Views приложения


## Описание

Фронтенд приложения для сервиса управления цифровыми активами (биржа) из лабораторной работы 3.

Технологии: 
- Vue3 (vue-toastification, vue-router, axios, vue-chartjs)
- Django/DRF (djoser)


## Запуск приложения:

```bash
$ cd LR4 && npm i && npm run serve
```

## Исходный код приложения:

### Конфигурация

- App.vue

_Стартовая точка приложения_

```vue
<template>
    <router-view />
</template>

<script>
export default {
    name: "App",
};
</script>

<style></style>
```

- main.js

_Настройка приложения, подключение внешних модулей и их конфигурация_

```js
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import HomePage from "@/pages/HomePage";
import PageNotFound from "@/pages/PageNotFound";
import CryptoPage from "@/pages/CryptoPage";
import LoginPage from "@/pages/LoginPage";
import SignupPage from "@/pages/SignupPage";
import PortfolioPage from "@/pages/PortfolioPage";
import SearchPage from "@/pages/SearchPage";

import VueAxios from "vue-axios";
import axios from "axios";

const routes = [
    { path: "/", component: HomePage },
    { path: "/search", component: SearchPage },
    { path: "/login", component: LoginPage },
    { path: "/signup", component: SignupPage },
    { path: "/profile", component: PortfolioPage },
    { path: "/market/:id", component: CryptoPage },
    { path: "/:pathMatch(.*)*", component: PageNotFound },
];

import {
    Chart as ChartJS,
    CategoryScale,
    ArcElement,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from "chart.js";
import {Pie} from 'vue-chartjs'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

ChartJS.register(ArcElement, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

const app = createApp(App);
app.use(router);
app.use(VueAxios, axios);
app.use(Pie);
app.use(Toast, {
    transition: "Vue-Toastification__slideBlurred",
    maxToasts: 5,
    newestOnTop: true,
    position: "bottom-left",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: true,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
});
app.mount("#app");
```

### Компоненты:

- CryptoCard.vue

_Карточка с отображением инфорации о цифровом активе_

```vue
<template>
    <div class="card border-success mb-3" style="max-width: 18rem">
        <div class="card-header bg-transparent border-success">
            <router-link :to="'market/' + id">{{ title }}</router-link>
        </div>
        <div class="card-body text-success">
            <h5 class="card-title">{{ price }}$</h5>
            <img class="card-img" src="@/assets/chart.png" width="200" />
        </div>
        <div v-if="description" class="card-footer bg-transparent border-success">{{ description }}</div>
    </div>
</template>

<script>
export default {
    props: ["id", "title", "description"],
    name: "CryptoCard",
    data() {
        return {
            price: null,
        };
    },
    methods: {
        async fetchData() {
            this.axios
                .get(`http://127.0.0.1:8088/market/${this.id}/`)
                .then((res) => {
                    this.price = res.data.last_price;
                })
                .catch(() => null);
        },
    },
    async mounted() {
        await this.fetchData();
    },
};
</script>

<style>
.card-img {
    filter: blur(2px);
    -webkit-filter: blur(2px);
}
</style>
```

- CryptoDeals.vue

_Компонент для отображения списка предложений купли/продажи_

```vue
<template>
    <section>
        <p class="text-center lead py-5">Deals</p>
        <span v-if="deals.length">
            <ul class="list-group list-group-flush">
                <li
                    v-for="deal in deals"
                    :key="deal"
                    class="mx-auto list-group-item d-flex justify-content-between col-6"
                >
                    <span>@{{ deal.seller }} {{deal.type_offer}} {{ deal.count }}</span>
                    <button
                        @click="cancelDeal(deal.id)"
                        v-if="deal.my_request"
                        class="text-white badge bg-danger rounded-pill"
                    >
                        Cancel
                    </button>
                    <button v-else @click="processDeal(deal)" class="text-white badge bg-success rounded-pill">
                        Buy for {{ deal.price }}$
                    </button>
                </li>
            </ul>
        </span>
        <span v-else>
            <p class="lead text-center">Seems that no one are selling {{ name }} now...</p>
        </span>
    </section>
</template>

<script>
import { useToast } from "vue-toastification";

export default {
    setup() {
        const toast = useToast();
        return { toast };
    },
    name: "CryptoDeals",
    props: ["deals", "name"],
    methods: {
        async cancelDeal(deal_id) {
            this.axios.delete(`http://localhost:8088/market-requests/${deal_id}/`, {
                headers: {
                    Authorization: `Token ` + localStorage.getItem("token"),
                },
            });
            this.toast.info("Canceled");
        },
        async processDeal(deal) {
            this.axios
                .patch(
                    `http://localhost:8088/market-requests/${deal.id}/`,
                    {},
                    {
                        headers: {
                            Authorization: `Token ` + localStorage.getItem("token"),
                        },
                    }
                )
                .then((res) => this.toast.success(`Order ${res.data.id} processed!`))
                .catch(() => this.toast.error('Insufficient balance!'));
        },
    },
};
</script>

<style></style>
```


- CryptoGraph.vue

_Граф со стоимостью валюты за прошлый месяц (данные формируются на бекенде, компонент для отображения)_

```vue
<template>
    <Line :data="data" :options="options" />
</template>

<script>
import { Line } from "vue-chartjs";

export default {
    components: { Line },
    name: "CryptoGraph",
    props: ["data"],
    data() {
        return {
            options: {
                responsive: true,
                maintainAspectRatio: false,
            },
        };
    },
};
</script>
```

- JoinSection.vue

_Небольшой компонент для быстрой регистрации_

```vue
<template>
    <section class="px-4 py-5 my-5 text-center">
        <img class="d-block mx-auto mb-4" src="img/unclesam.png" alt="" width="200" />
        <h1 class="display-5 fw-bold">New here?</h1>
        <div class="col-lg-6 mx-auto">
            <p class="lead mb-4">Take a quick tour into investment world</p>
            <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
                <button
                    type="button"
                    class="btn btn-primary btn-lg px-4 gap-3"
                    data-bs-toggle="modal"
                    data-bs-target="#loginModal"
                >
                    Join us now
                </button>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "JoinSection",
};
</script>

<style></style>
```


- NavBar.vue

_Navigation Bar приложения_

```vue
<template>
    <header
        class="container d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-4"
    >
        <a href="/" class="d-flex align-items-center col-md-auto mb-2 mb-md-0 text-dark text-decoration-none">
            <img src="img/logo.svg" width="288" height="33" alt="TimofeevInvest" class="logo" />
        </a>
        <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
            <li>
                <a href="/" class="nav-link active px-2 link-dark text-decoration-underline"
                    ><router-link to="/">Home</router-link></a
                >
            </li>
            <li>
                <router-link
                    to="/search"
                    class="nav-link px-2 link-dark"
                    data-bs-toggle="modal"
                    data-bs-target="#searchModal"
                >
                    <i class="bi bi-search-heart"></i>
                </router-link>
            </li>
            <li>
                <router-link to="/profile" class="nav-link px-2 link-dark"> <i class="bi bi-wallet2"></i> </router-link>
            </li>
            <li v-if="!user">
                <router-link to="/login" class="nav-link px-2 link-dark"
                    ><i class="bi bi-person-circle"></i>
                </router-link>
            </li>
            <span v-else>
                <li>
                    <p class="nav-link px-2 link-dark">
                        Welcome, {{ user.username }}! {{ user.balance }}$
                        <a class="btn btn-sm btn-primary" @click="logout">Exit</a>
                    </p>
                </li>
            </span>
        </ul>
    </header>
</template>

<script>
export default {
    name: "NavBar",
    data() {
        return {
            user: null,
        };
    },
    methods: {
        async getMeData(token) {
            await this.axios
                .get("http://127.0.0.1:8088/auth/users/me/", {
                    headers: {
                        Authorization: `Token ` + token,
                    },
                })
                .then((res) => {
                    this.user = res.data;
                })
                .catch(() => null);
        },
        async logout() {
            localStorage.clear();
            this.$router.go();
        },
    },
    async mounted() {
        const token = localStorage.getItem("token");
        if (token) {
            await this.getMeData(token);
        }
    },
};
</script>
```

- PageFooter.vue

_Переиспользуемый футер приложения_

```vue
<template>
    <footer class="footer py-5">
        <div class="row">
            <div class="col-6 col-md-2 mb-3">
                <h5>TI LLC</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Home</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Stocks</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Crypto</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Legal</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">About</a></li>
                </ul>
            </div>

            <div class="col-6 col-md-2 mb-3">
                <h5>Buy Crypto</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Buy Ethereum</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Buy Bitcoin</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Buy USDT</a></li>
                </ul>
            </div>
            <div class="col-6 col-md-2 mb-3"></div>

            <div class="col-md-5 offset-md-1 mb-3">
                <form>
                    <h5>Subscribe to our newsletter</h5>
                    <p>Monthly digest of what's new and exciting from us.</p>
                    <div class="d-flex flex-column flex-sm-row w-100 gap-2">
                        <label for="newsletter1" class="visually-hidden">Email address</label>
                        <input id="newsletter1" type="text" class="form-control" placeholder="Email address" />
                        <button class="btn btn-primary" type="button">Subscribe</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
            <p>&copy; 2022 TimofeevInvest INC INT LTD. All rights reserved.</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: "PageFooter",
};
</script>

<style></style>
```


- PortfolioChart.vue

_Pie-chart для наглядного отображения количества валют в портфолио_

```vue
<template>
    <Pie :options="options" :data="data"></Pie>
</template>

<script>
import { Pie } from "vue-chartjs";

export default {
    name: "PieChart",
    components: { Pie },
    props: {
        data: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            options: {
                responsive: true,
                maintainAspectRatio: false,
            },
        };
    },
};
</script>
```

### Views 

- CryptoPage.vue

_Страница для отображения полной информации об активе (цена, график, описание, название, предложения на рынке)_

```vue
<template>
    <body class="container">
        <nav-bar></nav-bar>
        <section v-if="showBuy">
            <hr class="opacity-100 m-0" />

            <div class="container d-flex justify-content-between align-items-start py-3 align-baseline">
                <h1 class="lead">Asset management</h1>
                <span>
                    <button
                        class="button badge bg-success rounded-pill"
                        data-bs-toggle="modal"
                        data-bs-target="#buyCryptoModal"
                        @click="showBuy = false"
                    >
                        <i class="bi bi-currency-dollar"></i>Back to graph
                    </button>
                </span>
            </div>

            <hr class="opacity-100 m-0" />

            <h1 class="lead text-center py-3">Manage {{ name }}</h1>

            <div class="text-center">
                <input :placeholder="'amount'" @input="(e) => (buyCount = e.target.value)" />
                <input :placeholder="'price'" @input="(e) => (buyPrice = e.target.value)" />
            </div>
            <div class="row">

                <div class="text-center">
                    <button class="btn btn-primary my-2" @click="createDeal('b')">Buy</button>
                </div>
                <div class="text-center">
                    <button class="btn btn-danger my-2" @click="createDeal('s')">Sell</button>
                </div>
            </div>
        </section>
        <section v-else>
            <hr class="opacity-100 m-0" />
            <div class="container d-flex justify-content-between align-items-start py-3 align-baseline">
                <h1 class="lead">
                    {{ this.name }} <span class="badge bg-primary rounded-pill">{{ price }}$</span>
                </h1>
                <span>
                    <span class="badge bg-info rounded-pill">{{ label }}</span>
                </span>
                <span>
                    <button
                        class="button badge bg-success rounded-pill"
                        data-bs-toggle="modal"
                        data-bs-target="#buyCryptoModal"
                        @click="showBuy = true"
                    >
                        <i class="bi bi-currency-dollar"></i>Manage
                    </button>
                </span>
            </div>
            <hr class="opacity-100 m-0" />

            <section id="mainChart" class="container py-5">
                <crypto-graph v-if="name" :data="graphData" />
            </section>

            <hr class="opacity-100 m-0" />
            <section>
                <p class="lead py-5">
                    {{ description }}
                </p>
            </section>

            <hr class="opacity-100 m-0" />

            <crypto-deals :name="name" :deals="deals" />

            <hr class="opacity-100 m-0" />
        </section>
        <page-footer></page-footer>
    </body>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";
import CryptoGraph from "@/components/CryptoGraph.vue";
import CryptoDeals from "@/components/CryptoDeals.vue";

import { useToast } from "vue-toastification";

export default {
    setup() {
        const toast = useToast();
        return { toast };
    },
    components: { NavBar, PageFooter, CryptoGraph, CryptoDeals },
    name: "CryptoPage",
    data() {
        return {
            err: null,
            name: ``,
            price: ``,
            description: ``,
            label: ``,
            deals: [],
            graphData: [],
            showBuy: false,
            buyCount: 0,
            buyPrice: 0,
        };
    },
    methods: {
        async getAssetInfo() {
            this.axios
                .get(`http://127.0.0.1:8088/market/${this.$route.params.id}/`)
                .then((res) => {
                    this.name = res.data.name;
                    this.description = res.data.description;
                    this.label = res.data.label;
                    this.price = res.data.last_price;

                    // fields for bar chart
                    const labels = [];
                    const datasets = [];

                    for (const obj of res.data.max_prices_last_month) {
                        labels.push(obj.date);
                        datasets.push(obj.max_total_price);
                    }

                    this.graphData = {
                        labels,
                        datasets: [
                            {
                                label: this.name,
                                backgroundColor: "#f87979",
                                data: datasets,
                            },
                        ],
                    };
                })
                .catch(() => {
                    this.err = "Currency not listed in our market";
                    this.$router.push("/404");
                });
        },
        async getAllDeals() {
            this.axios
                .get(`http://127.0.0.1:8088/market-requests/?entry=${this.$route.params.id}`, {
                    headers: {
                        Authorization: `Token ` + localStorage.getItem("token"),
                    },
                })
                .then((res) => {
                    this.deals = res.data;
                });
        },
        async createDeal(type) {
            this.axios
                .post(
                    `http://localhost:8088/market-requests/`,
                    {
                        entry: this.$route.params.id,
                        count: this.buyCount,
                        price: this.buyPrice,
                        type: type,
                    },
                    {
                        headers: {
                            Authorization: `Token ` + localStorage.getItem("token"),
                        },
                    }
                )
                .then((res) => this.toast.success(`Order ${res.data.id} created!`))
                .catch(() => this.toast.error(`Insufficient balance!`));
            this.showBuy = false;
        }
    },
    async mounted() {
        await this.getAssetInfo();
        await this.getAllDeals();
    },
};
</script>
```

- HomePage.vue

_Главная страница приложения_

```vue
<template>
    <div class="container">
        <nav-bar></nav-bar>
        <body class="container">
            <hr class="opacity-100 m-0" />

            <join-section v-if="!logged"></join-section>

            <hr class="opacity-100 m-0" />
            <section>
                <h2 class="text-center lead my-5">
                    The global cryptocurrency market cap today is <span class="text-success">$949.09B</span>, a
                    <span class="text-success">+0.14%</span> change from 24 hours ago.
                </h2>
            </section>

            <hr class="opacity-100 m-0" />
            <section class="px-4 mt-0 py-2 my-5 text-center">
                <h2 class="display-4 fw-bold">Trending positions:</h2>
                <div class="row d-flex justify-content-around">
                    <crypto-card
                        :id="1"
                        :title="'Bitcoin'"
                        :price="'19821.5'"
                        :description="'Digital gold'"
                    ></crypto-card>
                    <crypto-card
                        :id="2"
                        :title="'Ethereum'"
                        :price="'1803.22'"
                        :description="'The future of POS'"
                    ></crypto-card>
                    <crypto-card
                        :id="3"
                        :title="'Tesla'"
                        :price="'142.53'"
                        :description="'High potential'"
                    ></crypto-card>
                    <crypto-card
                        :id="4"
                        :title="'USDT'"
                        :price="'1.01'"
                        :description="'1USDT=1$, stable as hell'"
                    ></crypto-card>
                </div>
            </section>

            <hr class="opacity-100 m-0" />
            <section class="px-4 mt-0 py-2 my-5 text-center">
                <h2 class="display-4 fw-bold">Worldwide currencies:</h2>
                <div class="row d-flex justify-content-around">
                    <crypto-card :id="5" :title="'Ruble'" :price="'0.018'"></crypto-card>
                    <crypto-card :id="6" :title="'Lirasi'" :price="'0.054'"></crypto-card>
                    <crypto-card :id="7" :title="'Lari'" :price="'0.36'"></crypto-card>
                    <crypto-card :id="8" :title="'Euro'" :price="'0.94'"></crypto-card>
                </div>
            </section>
            <hr class="opacity-100 m-0" />
            <page-footer></page-footer>
        </body>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";
import CryptoCard from "@/components/CryptoCard.vue";
import JoinSection from "@/components/JoinSection.vue";
export default {
    components: { NavBar, PageFooter, CryptoCard, JoinSection },
    computed: {
        logged() {
            return Boolean(localStorage.getItem('token'))
        }
    }
};
</script>

<style></style>
```

- LoginPage.vue

_Страница авторизации пользователя_

```vue
<template>
    <div class="container">
        <nav-bar></nav-bar>
        <hr class="opacity-100 m-0" />
        <h1 class="text-center mt-3">Login</h1>

        <form class="container d-flex justify-content-center" onsubmit="return false;">
            <div class="col-4">
                <div class="form-group">
                    <label for="emailInput">Username</label>
                    <input
                        class="form-control"
                        id="emailInput"
                        :value="username"
                        @input="(e) => (username = e.target.value)"
                    />
                    <p class="lead" v-if="err">{{ err }}</p>
                </div>
                <div class="form-group">
                    <label for="passwordInput">Password</label>
                    <input
                        type="password"
                        class="form-control"
                        id="passwordInput"
                        :value="password"
                        @input="(e) => (password = e.target.value)"
                    />
                </div>
                <div class="d-flex justify-content-between mt-3">
                    <button @click="loginUser" type="button" class="btn btn-primary">Login</button>
                    <div class="border-right pr-3 mr-3"></div>
                    <button type="button" class="btn btn-secondary">
                        <router-link class="text-white" to="/signup">Sign Up</router-link>
                    </button>
                </div>
            </div>
        </form>

        <hr class="opacity-100" />
        <page-footer />
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    components: { NavBar, PageFooter },
    data() {
        return {
            username: "",
            password: "",
            err: "",
        };
    },
    methods: {
        loginUser() {
            this.err = "";
            this.axios
                .post("http://127.0.0.1:8088/auth/token/login/", {
                    username: this.username,
                    password: this.password,
                })
                .then((resp) => {
                    localStorage.setItem("token", resp.data.auth_token);
                    this.$router.push("/");
                })
                .catch((e) => {
                    this.err = "Oops... Try again!";
                    console.log(e);
                    this.username = "";
                    this.password = "";
                });
        },
    },
};
</script>
```

- PageNotFound.vue

_Страница 404_

```vue
<template>
    <div class="container">
        <nav-bar></nav-bar>
        <section>
            <hr class="opacity-100 m-0" />
            <h1 class="d-flex p-2 justify-content-center">404</h1>
            <p class="lead d-flex justify-content-center">Page {{ this.$route.path }} not found</p>
            <div class="text-center">
                <a class="btn btn-primary text-center"
                    ><router-link class="text-white" to="/">Bring me home</router-link></a
                >
            </div>
            <hr class="opacity-100" />
        </section>
        <page-footer></page-footer>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    components: { PageFooter, NavBar },
};
</script>
```

- PortfolioPage.vue

_Страница с портфолио пользователя (активы пользователя)_

```vue
<template>
    <body class="container">
        <nav-bar />
        <hr class="opacity-100 m-0" />

        <p class="lead text-center py-1 my-1">My Portfolio</p>
        <section class="px-4 py-5 my-5">
            <span class="row align-content-center">
                <span class="col">
                    <portfolio-chart v-if="graphData.length != 0" :data="graphData"/>
                </span>

                <span class="d-flex col justify-content-center">
                    <div class="card" style="width: 30rem">
                        <div class="card-header">Your assets</div>
                        <ul class="list-group">
                            <li
                                v-for="asset in assets"
                                :key="asset"
                                class="list-group-item d-flex justify-content-between align-items-center"
                            >
                                {{ asset.meta }}
                                <span class="badge bg-primary rounded-pill">{{ asset.amount }}</span>
                            </li>
                        </ul>
                    </div>
                </span>
            </span>
        </section>

        <hr class="opacity-100 m-0" />
        <page-footer />
    </body>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";
import PortfolioChart from "@/components/PortfolioChart.vue";

export default {
    components: { NavBar, PageFooter, PortfolioChart },
    name: "PortfolioPage",
    data() {
        return {
            assets: [],
            graphData: [],
        };
    },
    async mounted() {
        await this.getPortfolio();
    },
    methods: {
        async getPortfolio() {
            const assets = await this.axios.get(`http://localhost:8088/assets/`, {
                headers: {
                    Authorization: `Token ` + localStorage.getItem("token"),
                },
            });
            this.assets = assets.data.assets;
            this.prepareData(assets.data.assets)
            return assets.data.assets
        },
        prepareData(assets) {
            const labels = [];
            const datasets = [];

            for (const obj of Object.entries(assets)) {
                labels.push(obj[1].meta);
                datasets.push(obj[1].amount);
            }

            this.graphData = {
                labels,
                datasets: [
                    {
                        label: "Amount",
                        backgroundColor: "#f87979",
                        data: datasets,
                    },
                ],
            };
        }
    },
};
</script>
```

- SearchPage.vue

_Страница поиска активов доступных на сервисе_

```vue
<template>
    <body class="container">
        <nav-bar />
        <hr class="opacity-100 m-0" />

        <h1 class="text-center m-2">Find any listed currency:</h1>

        <div class="container d-flex justify-content-center col-8">
            <div class="mb-2 input-group">
                <input type="text" class="form-control" placeholder="USDT" @input="(e) => (query = e.target.value)" />
                <button class="btn btn-outline-primary" @click="searchCrypto" type="button" id="button-addon2">
                    Lookup
                </button>
                <button
                    v-if="retrieveLast"
                    class="btn btn-outline-info"
                    @click="getLastSearchRes"
                    type="button"
                    id="button-addon2"
                >
                    Last
                </button>
            </div>
        </div>

        <section v-if="results" class="container d-flex justify-content-center py-2">
            <div class="list-group col-8">
                <router-link
                    v-for="result in results"
                    :key="result"
                    :to="'/market/' + result.id"
                    href="#"
                    class="list-group-item list-group-item-action"
                >
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{ result.name }}</h5>
                        <small class="text-muted">{{ result.last_price }}$</small>
                    </div>
                    <p class="mb-1">{{ result.description }}</p>
                    <small class="text-muted">{{ result.group }}. {{ result.label }}</small>
                </router-link>
            </div>
        </section>

        <hr class="opacity-100 m-0" />
        <page-footer />
    </body>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    components: { NavBar, PageFooter },
    name: "SearchPage",
    data() {
        return {
            query: "",
            results: [],
        };
    },
    methods: {
        async searchCrypto() {
            this.axios.get(`http://127.0.0.1:8088/market/?search=${this.query}`).then((res) => {
                this.results = res.data;
            });
            await this.saveSearch(this.query);
        },
        async retrieveLast() {
            return localStorage.getItem("lastSearch") || null;
        },
        async saveSearch() {
            localStorage.setItem("lastSearch", this.query);
        },
        async getLastSearchRes() {
            this.query = await this.retrieveLast();
            await this.searchCrypto();
        },
    },
};
</script>
```

- SignupPage.vue

_Страница регистрации нового пользователя_

```vue
<template>
    <div class="container">
        <nav-bar></nav-bar>
        <hr class="opacity-100 m-0" />
        <h1 class="text-center mt-3">Sign Up</h1>

        <form class="container d-flex justify-content-center" onsubmit="return false;">
            <div class="col-4">
                <div class="form-group">
                    <label for="usernameInput">Username</label>
                    <input
                        class="form-control"
                        id="usernameInput"
                        aria-describedby="emailHelp"
                        :value="username"
                        @input="(e) => (username = e.target.value)"
                    />
                </div>
                <div class="form-group">
                    <label for="emailInput">Email address</label>
                    <input
                        type="email"
                        class="form-control"
                        id="emailInput"
                        aria-describedby="emailHelp"
                        :value="email"
                        @input="(e) => (email = e.target.value)"
                    />
                </div>
                <div class="form-group">
                    <label for="passwordInput">Password</label>
                    <input
                        type="password"
                        class="form-control"
                        id="passwordInput"
                        :value="password"
                        @input="(e) => (password = e.target.value)"
                    />
                </div>
                <div class="d-flex justify-content-between mt-3">
                    <button type="submit" class="btn btn-primary" @click="signUp">Sign Up</button>
                    <div class="border-right pr-3 mr-3"></div>
                    <button type="button" class="btn btn-secondary">
                        <router-link class="text-white" to="/">Cancel</router-link>
                    </button>
                </div>
            </div>
        </form>

        <hr class="opacity-100" />
        <page-footer />
    </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import PageFooter from "@/components/PageFooter.vue";

import { useToast } from "vue-toastification";

export default {
    setup() {
        const toast = useToast();
        return { toast };
    },
    components: { NavBar, PageFooter },
    data() {
        return {
            username: "",
            email: "",
            password: "",
        };
    },
    methods: {
        async signUp() {
            if (!this.username || !this.email || !this.password) {
                this.toast.error('Enter credentials!')
                return
            }
            try {   
                await this.axios.post('http://localhost:8088/auth/users/', {
                    username: this.username,
                    password: this.password,
                    email: this.email,
                }, {})
            } catch (e) {
                this.toast.warning('An error occured, try later');
                return
            }
            this.$router.push('/');
            this.toast.success(`Welcome, ${this.username}! You may login with entered creadentials`)
        },
    },
};
</script>
```
