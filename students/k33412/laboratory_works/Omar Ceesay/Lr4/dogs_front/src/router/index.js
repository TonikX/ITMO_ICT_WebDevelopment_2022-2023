import Vue from 'vue';
import VueRouter from 'vue-router';


import LogIn from '../views/reader/LogIn.vue'
import SignUp from '../views/reader/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/reader/Profile.vue'
import ProfileEdit from '../views/reader/ProfileEdit.vue'
import LogOut from '../views/reader/LogOut.vue'
import ExpertsView from "@/components/ExpertsView.vue";
import ParticipantsView from "@/components/ParticipantsView.vue";
import DogRegister from "@/views/reader/DogRegister.vue"

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
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/participation', // конкретный url-адрес
    component: ParticipationView // Ссылка на компонент
  },
  {
    path: '/participants', // concreat url-adress 
    component: ParticipantsView //link to the components
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