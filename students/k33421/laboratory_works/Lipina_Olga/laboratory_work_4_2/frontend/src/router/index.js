import Vue from 'vue'
import VueRouter from 'vue-router'

import SignIn from '@/views/reader/SignIn'
import SignUp from '@/views/reader/SignUp'
import Home from '@/views/Home'
import ReaderProfile from '@/views/reader/ReaderProfile'
import ReaderProfileEdit from '@/views/reader/ReaderProfileEdit'
import Instance from '@/views/library/Instance'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
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
    path: '/library/profile',
    name: 'reader_profile',
    component: ReaderProfile
  },
  {
    path: '/library/profile/edit',
    name: 'reader_profile_edit',
    component: ReaderProfileEdit
  },
  {
    path: '/library/instances/:id',
    name: 'instance',
    component: Instance
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
