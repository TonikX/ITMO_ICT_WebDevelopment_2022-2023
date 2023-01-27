import {createRouter, createWebHistory} from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'books',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/BooksPage.vue')
        },
        {
            path: '/book/',
            name: 'book',
            component: () => import('../views/BookPage.vue')
        },
        {
            path: '/profile/',
            name: 'profile',
            component: () => import('../views/Profile.vue')
        }
    ]
})

export default router
