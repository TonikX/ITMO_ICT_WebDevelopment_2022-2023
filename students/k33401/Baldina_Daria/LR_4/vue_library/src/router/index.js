import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/reg',
      name: 'Registration',
      component: () => import('@/views/RegistrationView.vue')
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
      path: '/take_book/:id',
      name: 'TakeBook',
      component: () => import('@/views/TakeBookView.vue')
    },
    {
      path: '/return/:id',
      name: 'ReturnBook',
      component: () => import('@/views/ReturnBookView.vue')
    },
    {
      path: '/reader',
      name: 'Reader',
      component: () => import('@/views/ReaderInfoView.vue')
    },
    {
      path: '/edit',
      name: 'EditReader',
      component: () => import('@/views/EditProfileView.vue')
    }
  ]
})
  
export default router

