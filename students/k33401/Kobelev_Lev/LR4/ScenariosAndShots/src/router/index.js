import {createRouter, createWebHistory} from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    mode: "history",
    routes: [
        {
            path: '/scenarios',
            name: 'scenarios',
            component: () => import('../views/HomeView.vue')
        },
        {
            path: '/scenarios/:id',
            name: 'scenario',
            component: () => import('../views/ScenarioView.vue'),
            props: true
        }
    ]
})

export default router
