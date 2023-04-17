import { createRouter, createWebHistory } from 'vue-router';
import Login from "@/views/LogIn.vue";
import Signup from "@/views/SignUp.vue";
import Main from "@/views/Main.vue";
import Home from "@/views/Home.vue";
import FlightAdd from "@/views/FlightAdd.vue";


const router = createRouter({
    routes: [
        {
            path: '/', // конкретный url-адрес
            component: Main // Ссылка на компонент
        },
        {
            path: '/login/', // конкретный url-адрес
            name: 'Login',
            component: Login // Ссылка на компонент
        },
        {
            path: '/signup/', // конкретный url-адрес
            name: 'Signup',
            component: Signup // Ссылка на компонент
        },
        {
            path: '/home/', // конкретный url-адрес
            name: 'Home',
            component: Home // Ссылка на компонент
        },
        {
            path: '/fladd/', // конкретный url-адрес
            name: 'FlightAdd',
            component: FlightAdd // Ссылка на компонент
        },
    ],
    history: createWebHistory()
})

export default router
