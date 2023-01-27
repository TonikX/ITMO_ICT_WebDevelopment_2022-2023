import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/products/:id',
      name: 'product',
      component: () => import('@/views/ProductView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/ProfileView.vue')
    },
  ]
})

export default router
