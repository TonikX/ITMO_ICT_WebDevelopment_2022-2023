import {createRouter, createWebHistory} from 'vue-router'
import WelcomeView from "../views/WelcomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import CurrencyView from "../views/CurrencyView.vue";
import MarketView from "../views/MarketView.vue";
import ProfileView from "../views/ProfileView.vue";

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
        },
        {
            path: '/market',
            name: 'market',
            component: MarketView,
            meta: {
                layout: 'DefaultLayout'
            }
        },
        {
            path: '/profile',
            name: 'profile',
            component: ProfileView,
            meta: {
                layout: 'DefaultLayout'
            }
        }
    ]
})

export default router
