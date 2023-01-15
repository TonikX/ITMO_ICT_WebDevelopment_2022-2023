// Composables
import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'greeting',
      component: () => import('../views/Greeting.vue')
    },
    {
      path: '/nasa',
      name: 'Nasa',
      component: () => import('../views/Nasa.vue')
 }
  ]
})
  
export default router
