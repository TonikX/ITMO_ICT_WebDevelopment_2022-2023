import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/registration',
      name: 'Registration',
      component: () => import('@/views/RegistrationView.vue')
    },
    {
      path: '/finish_complete_info',
      name: 'FinishCompleteInfoView',
      component: () => import('@/views/FinishCompleteInfoView.vue')
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/books',
      name: 'Books',
      component: () => import('@/views/BooksView.vue')
    },
    {
      path: '/books/:id',
      name: 'Book',
      component: () => import('@/views/BookView.vue')
    },
    {
      path: '/reader',
      name: 'Reader',
      component: () => import('@/views/ReaderInfoView.vue')
    },
    {
      path: '/reader/edit',
      name: 'EditReader',
      component: () => import('@/views/EditReaderView.vue')
    }
  ]
})

export default router
