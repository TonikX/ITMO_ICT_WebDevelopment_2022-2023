import { createRouter, createWebHistory } from 'vue-router'

import Homepage from '../views/Homepage.vue'
import Signup from '../views/SignUp.vue'
import Signin from '../views/SignIn.vue'
import Staff from '../views/staff.vue'
import RequestCreation from '../views/RequestCreation.vue'
import Services from '../views/Services.vue'
import Materials from '../views/Materials.vue'
import addClient from '../views/addClient.vue'
import Clients from '../views/Clients.vue'
import addRequest from '../views/addRequest.vue'
import addService from '../views/addService.vue'
import addMaterial from '../views/addMaterial.vue'
import Requests from '../views/Requests.vue'
import stuffAddition from '../views/stuffAddition.vue'
import createService from '../views/createService.vue'
import createMaterial from '../views/createMaterial.vue'
import createStaff from '../views/createStaff.vue'
import addWorkGroup from '../views/addWorkGroup.vue'
import PaymentOrder from '../views/addPaymentOrder.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
     {
    path: '/',
    name: 'homepage',
    component: Homepage
  },
    {
    path: '/staff',
    name: 'staffList',
    component: Staff
  },
   {
    path: '/createstaff',
    name: 'createstaff',
    component: createStaff
  },
  {
    path: '/createservice',
    name: 'createservice',
    component: createService
  },
  {
    path: '/creatematerial',
    name: 'creatematerial',
    component: createMaterial
  },
  {
    path: '/requestcreation',
    name: 'requestcreation',
    component: RequestCreation
  },
  {
    path: '/services',
    name: 'services',
    component: Services
  },
  {
    path: '/addrequest',
    name: 'addrequest',
    component: addRequest
  },
  {
    path: '/clients',
    name: 'clients',
    component: Clients
  },
  {
    path: '/addclient',
    name: 'addclient',
    component: addClient
  },
  {
    path: '/signin',
    name: 'signin',
    component: Signin
  },
   {
    path: '/materials',
    name: 'materials',
    component: Materials
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/addservice',
    name: 'addservice',
    component: addService
  },
  {
    path: '/addmaterial',
    name: 'addmaterial',
    component: addMaterial
  },
   {
    path: '/addworkgroup',
    name: 'addworkgroup',
    component: addWorkGroup
  },
  {
    path: '/addPaymentOrder',
    name: 'addPaymentOrder',
    component: PaymentOrder
  },
  {
    path: '/requests',
    name: 'requests',
    component: Requests
  },
  {
    path: '/addstuff',
    name: 'addstuff',
    component: stuffAddition
  },

  ]
})

export default router

