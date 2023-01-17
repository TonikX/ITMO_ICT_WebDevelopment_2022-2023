import { createRouter, createWebHistory } from 'vue-router'
import HotelView from '../views/HotelPage.vue'
import RoomTypeView from '../views/RoomTypePage.vue'
import RoomView from '../views/RoomPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'hotels',
      component: HotelView
    },
    {
      path: '/hotel/:id/',
      name: 'room_types',
      props: true,
      component: RoomTypeView
    },
    {
      path: '/hotel/room_type/:id/',
      name: 'rooms',
      props: true,
      component: RoomView
    },
    // {
    //   path: '/',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
