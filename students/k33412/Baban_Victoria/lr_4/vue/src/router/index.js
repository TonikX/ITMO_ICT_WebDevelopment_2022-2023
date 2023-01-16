import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/registration',
      name: 'registration',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LogInView.vue')
    },
    {
      path: '/',
      name: 'main',
      component: () => import('../views/MainView.vue')
    },
    {
      path: '/lk',
      name: 'lk',
      component: () => import('../views/LkView.vue')
    },
      {
      path: '/lk/data',
      name: 'lk_data',
      component: () => import('../views/LkData.vue')
    },
    {
      path: '/events/:id',
      name: 'eventInfo',
      props: true,
      component: () => import('../views/CardView.vue')
    }
  ]
})

export default router
