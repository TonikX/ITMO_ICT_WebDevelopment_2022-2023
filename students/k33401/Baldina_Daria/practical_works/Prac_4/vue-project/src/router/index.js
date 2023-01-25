import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'greeting',
      component: () => import('../views/Greeting.vue')
 },
  ]
})

// const route = new VueRouter({
//   mode: 'history',
//   base: import.meta.env.BASE_URL,
//   router
// })

export default router