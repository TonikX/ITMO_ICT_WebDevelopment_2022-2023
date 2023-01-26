import { createRouter, createWebHistory } from 'vue-router'
import stores from '../stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/sign-up/',
      name: 'SignUp', 
      component: () => import('../views/SignUp.vue')
    },
    {
      path: '/log-in/',
      name: 'LogIn', 
      component: () => import('../views/LogIn.vue')
    },
    {
      path: '/my-account/',
      name: 'MyAccount',
      component: () => import('../views/MyAccount.vue'),
      meta: {
      requireLogin: true
    }
    },
    {
      path: '/guests/',
      name: 'Guests',
      component: () => import('../views/Guests.vue')
    },
    {
      path: '/guests/create/',
      name: 'AddGuest',
      component: () => import('../views/AddGuest.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/guests/:id',
      name: 'Guest',
      component: () => import('../views/Guest.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/guests/update/:id',
      name: 'EditGuest',
      component: () => import('../views/EditGuest.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/bookings/create/',
      name: 'AddBooking',
      component: () => import('../views/AddBooking.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/bookings/update/:id',
      name: 'EditBook',
      component: () => import('../views/EditBook.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/cleanings/',
      name: 'Cleaners',
      component: () => import('../views/Cleaners.vue'),
    },
    {
      path: '/cleanings/create/',
      name: 'AddCleaning',
      component: () => import('../views/AddCleaning.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutRooms.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !stores.state.isAuthenticated) {
    next('/log-in/')
  } else {
    next()
  }
}) 

export default router
