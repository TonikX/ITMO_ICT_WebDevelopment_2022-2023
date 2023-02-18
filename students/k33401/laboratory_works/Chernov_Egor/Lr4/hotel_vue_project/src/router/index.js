import {createRouter, createWebHistory} from 'vue-router'
import HotelView from '../views/HotelPage.vue'
import RoomTypeView from '../views/RoomTypePage.vue'
import RoomView from '../views/RoomPage.vue'
import RetrieveRoomView from '../views/RetrieveRoomPage.vue'
import LoginView from '../views/LoginPage.vue'
import BookingView from '../views/BookingPage.vue'
import RegView from '../views/RegPage.vue'
import ComView from '../views/ComPage.vue'
import ProfileView from '../views/ProfilePage.vue'
import UpdateRegView from "../views/UpdateRegPage.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'hotels',
            component: HotelView
        },
        {
            path: '/hotel/:id/',
            name: 'room_types',
            props: true,
            component: RoomTypeView
        },
        {
            path: '/hotel/room_type/:id/',
            name: 'rooms',
            props: true,
            component: RoomView
        },
        {
            path: '/hotel/room_type/room/:id/',
            name: 'room',
            props: true,
            component: RetrieveRoomView
        },
        {
            path: '/login/',
            name: 'login',
            component: LoginView
        },
        {
            path: '/booking/',
            name: 'booking',
            component: BookingView
        },
        {
            path: '/registrations/',
            name: 'registrations',
            component: RegView
        },
        {
            path: '/comments/',
            name: 'comments',
            component: ComView
        },
        {
            path: '/profile/',
            name: 'profile',
            component: ProfileView
        },
        {
            path: '/update/reg/:id/',
            name: 'update_reg',
            component: UpdateRegView
        },
    ]
})

export default router
