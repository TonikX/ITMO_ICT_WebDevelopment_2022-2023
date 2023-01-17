import {createRouter, createWebHistory} from 'vue-router'
import WelcomeView from "../views/WelcomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import CurrencyView from "../views/CurrencyView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'welcome',
            component: WelcomeView,
            meta: {
                layout: 'DefaultLayout'
            }
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView,
            meta: {
                layout: 'AuthLayout'
            }
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
            meta: {
                layout: 'AuthLayout'
            }
        },
        {
            path: '/currency/:id',
            name: 'currency',
            component: CurrencyView,
            meta: {
                layout: 'DefaultLayout'
            }
        }
    ]
})

export default router
