import {createRouter, createWebHistory} from 'vue-router'
import MainPage from "@/views/MainPage.vue";
import EventPage from "@/views/EventPage.vue";
import SignUpPage from "@/views/SignUpPage.vue";
import SignInPage from "@/views/SignInPage.vue";
import ProfilePage from "@/views/ProfilePage.vue";
import CalendarPage from "@/views/CalendarPage.vue";

// массив с роутами
const routes = [
    {path: "/main", component: MainPage},
    {path: "/event/:id", component: EventPage},
    {path: "/signup", component: SignUpPage},
    {path: "/signin", component: SignInPage},
    {path: "/profile", component: ProfilePage},
    {path: "/calendar", component: CalendarPage}
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

// экспортируем сконфигурированный роутер
export default router
