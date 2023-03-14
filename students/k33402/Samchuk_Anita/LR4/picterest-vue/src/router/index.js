import Vue from 'vue'
import VueRouter from 'vue-router'
import DashboardView from '../views/DashboardView'
import LoginView from '../views/LoginView'
import PostView from '../views/PostView'
import ProfileView from '../views/ProfileView'
import SignUpView from '../views/SignUpView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: DashboardView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/post/:id',
    name: 'Post',
    component: PostView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
