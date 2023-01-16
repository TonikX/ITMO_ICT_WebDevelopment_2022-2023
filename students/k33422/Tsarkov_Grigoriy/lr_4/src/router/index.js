import Vue from 'vue';
import VueRouter from 'vue-router';


import SignIn from '../views/profile/SignIn.vue'
import SignUp from '../views/profile/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/profile/Profile.vue'
import ProfileEdit from '../views/profile/ProfileEdit.vue'
import LogOut from '../views/profile/LogOut.vue'
import ParticipationView from "@/components/ParticipationView.vue";
import ExpertsView from "@/components/ExpertsView.vue";
import ParticipantsView from "@/components/ParticipantsView.vue";
import CosRegister from "@/views/profile/CosRegister.vue";
import CosScoring from "@/views/profile/CosScoring.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/cosplay/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/cosplay/logout',
    name: 'logout',
    component: LogOut
  },
  {
    path: '/cosplay/signin',
    name: 'signin',
    component: SignIn
  },
  {
    path: '/cosplay/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/cosplay/profile/edit',
    name: 'edit',
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
    path: '/experts', // конкретный url-адрес
    component: ExpertsView // Ссылка на компонент
  },
  {
    path: '/participants', // конкретный url-адрес
    component: ParticipantsView // Ссылка на компонент
  },
  
  {
    path: '/cosplay/profile/reg',
    name: 'reg',
    component: CosRegister
  },

  {
    path: 'cosplay/profile/scoring',
    name: 'scoring',
    component: CosScoring
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router