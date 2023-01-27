import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/components/Login.vue'
import Doctor from '@/components/Doctor'
import Signup from '@/components/Signup'
import Profile from '@/components/Profile'
import EditProfile from '@/components/EditProfile'
import Doctorlist from '@/components/Doctorlist'
import Cabinet from '@/components/Cabinet'
import Cabinetlist from '@/components/Cabinetlist'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/profile/edit',
    name: 'EditProfile',
    component: EditProfile
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/doctor/:id',
    name: 'Doctor',
    component: Doctor
  },
  {
    path: '/doctorlist',
    name: 'Doctorlist',
    component: Doctorlist
  },
  {
    path: '/cabinetlist',
    name: 'Cabinetlist',
    component: Cabinetlist
  },
  {
    path: '/cabinet',
    name: 'Cabinet',
    component: Cabinet
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
