import Vue from 'vue'
import VueRouter from 'vue-router'

import About from '@/views/About.vue'
import Signup from '@/views/SignUp.vue'
import Signin from '@/views/SignIn.vue'
import AccountDetails from '@/views/AccountDetails.vue'
import Login from '@/views/Login.vue'
import Client from '@/views/data/Client'
import ServicePL from '@/views/data/ServicePL'
import MaterialsPL from '@/views/data/MaterialsPL'
import Executor from '@/views/data/Executor'
import Request from '@/views/data/Request'
import ChosenServices from '@/views/data/ChosenServices'
import ChosenMaterials from '@/views/data/ChosenMaterials'
import WorkGroup from '@/views/data/WorkGroup'
import Invoice from '@/views/data/Invoice'
import PaymentOrder from '@/views/data/PaymentOrder'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'about',
    component: About
  },

  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },

  {
    path: '/signin',
    name: 'signin',
    component: Signin
  },

  {
    path: '/accountdetails',
    name: 'accountdetails',
    component: AccountDetails
  },

  {
    path: '/login',
    name: 'login',
    component: Login
  },

  {
    path: '/client',
    name: 'client',
    component: Client
  },

  {
    path: '/servicepl',
    name: 'servicepl',
    component: ServicePL
  },

  {
    path: '/materialspl',
    name: 'materialspl',
    component: MaterialsPL
  },
  {
    path: '/executor',
    name: 'executor',
    component: Executor
  },

  {
    path: '/request',
    name: 'request',
    component: Request
  },

  {
    path: '/chosenservices',
    name: 'chosenservices',
    component: ChosenServices
  },
  {
    path: '/chosenmaterials',
    name: 'chosenmaterials',
    component: ChosenMaterials
  },

  {
    path: '/workgroup',
    name: 'workgroup',
    component: WorkGroup
  },

  {
    path: '/invoice',
    name: 'invoice',
    component: Invoice
  },

  {
    path: '/paymentorder',
    name: 'paymentorder',
    component: PaymentOrder
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
