import {createRouter, createWebHistory} from 'vue-router'
import AllRoomsView from "@/views/AllRoomsView.vue";
import RoomView from "@/views/RoomView.vue";
import AllGuestsView from "@/views/AllGuestsView.vue";
import ReportView from "@/views/ReportView.vue";
import GuestView from "@/views/GuestView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'rooms',
            component: AllRoomsView
        },
        {
            path: '/room/:id',
            name: 'room',
            props: true,
            component: RoomView
        },
        {
            path: '/guests',
            name: 'guests',
            component: AllGuestsView
        },
        {
            path: '/guest/:id',
            name: 'guest',
            props: true,
            component: GuestView
        },
        {
            path: '/report',
            name: 'report',
            component: ReportView
        },
    ]
})

export default router
