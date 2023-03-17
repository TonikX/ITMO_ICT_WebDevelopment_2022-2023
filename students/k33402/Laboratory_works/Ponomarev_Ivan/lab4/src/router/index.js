import { createRouter, createWebHistory } from 'vue-router'
import EventsView from "@/views/EventsView.vue" 
import ProfileView from "@/views/ProfileView.vue"
import Calendar from "@/views/Calendar.vue"
import EventView from "@/views/EventView.vue"
import SignUpView from "@/views/SignUpView.vue"

const routes = [
  {
    path: '/',
    name: 'home',
    component: EventsView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: `/events/:id`,
    name: 'event',
    component: EventView
  },
  {
    path: '/signup',
    name :'sign_up',
    component: SignUpView
  },
  {
    path: '/calendar',
    name: 'calendar',
    component: Calendar
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
