import Vue from 'vue';
import VueRouter from 'vue-router';


import SignIn from '../views/reader/SignIn.vue'
import SignUp from '../views/reader/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/reader/Profile.vue'
import ProfileEdit from '../views/reader/ProfileEdit.vue'
import LogOut from '../views/reader/LogOut.vue'
import ParticipationView from "@/components/ParticipationView.vue";
import ParticipantsView from "@/components/ParticipantsView.vue";
import DogRegister from "@/views/reader/DogRegister.vue"
import DogGrade from "@/views/reader/DogGrade.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/show/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/show/logout',
    name: 'logout',
    component: LogOut
  },
  {
    path: '/show/signin',
    name: 'signin',
    component: SignIn
  },
  {
    path: '/show/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/show/profile/edit',
    name: 'profile_edit',
    component: ProfileEdit
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/participation',
    component: ParticipationView
  },
  {
    path: '/participants',
    component: ParticipantsView
  },
  
  {
    path: '/show/profile/regdog',
    name: 'regdog',
    component: DogRegister
  },
  {
    path: '/show/profile/grading',
    name: 'grading',
    component: DogGrade
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router