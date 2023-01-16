import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
 history: createWebHistory(import.meta.env.BASE_URL),

 routes: [
   {
     path: '/all_workers',
     name: 'workers',
     component: () => import('../views/WorkersPage.vue')
   },
     {
         path: '/login',
         name: 'login',
         component: () => import('../views/LoginPage.vue')
     },
     {
         path: '/singup',
         name: 'singup',
         component: () => import('../views/SingupPage.vue')
     },
     {
         path: '/',
         name: 'main',
         component: () => import('../views/MainPage.vue')
     },
     {
         path: '/rooms',
         name: 'rooms',
         component: () => import('../views/RoomsPage.vue')
     },
     {
         path: '/room_book',
         name: 'room_book',
         component: () => import('../views/CurrentBooksForRoomPage.vue')
     },
     {
         path: '/client',
         name: 'client',
         component: () => import('../views/ClientPage.vue')
     },
 ]
})
 
// экспортируем сконфигурированный роутер
export default router
