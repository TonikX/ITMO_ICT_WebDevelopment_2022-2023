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
