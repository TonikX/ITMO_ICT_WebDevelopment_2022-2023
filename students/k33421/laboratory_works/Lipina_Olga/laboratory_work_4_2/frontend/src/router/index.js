import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView'

import SignIn from '@/views/reader/SignIn'
import SignUp from '@/views/reader/SignUp'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/library/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/library/signin',
    name: 'signin',
    component: SignIn
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
