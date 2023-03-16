import {createRouter, createWebHistory} from "vue-router"

import SignIn from '../views/reader/SignIn.vue'
import SignUp from '../views/reader/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/reader/Profile.vue'
import ProfileEdit from '../views/reader/ProfileEdit.vue'
import LogOut from '../views/reader/LogOut.vue'
import Participation from "../components/Participation.vue";
import Flights from "../components/Flights.vue";
import Participants from "../components/Participants.vue";


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

    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/participation',
    component: Participation
  },

  {
    path: '/flights', // конкретный url-адрес
    component: Flights // Ссылка на компонент
  },
  {
    path: '/participants', // конкретный url-адрес
    component: Participants // Ссылка на компонент
  },

]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router