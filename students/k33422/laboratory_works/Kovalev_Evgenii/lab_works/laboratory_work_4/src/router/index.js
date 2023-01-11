// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        component: () => import('@/layouts/default/Default.vue'),
        children: [
            {
                name: 'Мои книги',
                path: '/',
                component: () => import('@/views/Home.vue'),
            },
            {
                path: '/books',
                name: 'Книги в библиотеке',
                component: () => import('@/views/Books.vue'),
            },
        ],
    },
    {
        path: '/auth',
        name: 'Authorization',
        component: () => import('@/views/Authorization.vue'),
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

export default router
