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
