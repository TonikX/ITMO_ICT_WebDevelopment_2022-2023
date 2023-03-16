import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Book from '@/components/Book'
import Sched from '@/components/Sched'
import BookUpdate from '@/components/BookUpdate'
import Lk from '@/components/Lk'
import ClientAdd from '@/components/ClientAdd'
import SchedDel from '@/components/SchedDel'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/book',
      name: 'book',
      component: Book
    },
    {
      path: '/sched',
      name: 'sched',
      component: Sched
    },
    {
      path: '/bookupdate',
      name: 'bookupdate',
      component: BookUpdate
    },
    {
      path: '/lk',
      name: 'lk',
      component: Lk
    },
    {
      path: '/clientadd',
      name: 'clientadd',
      component: ClientAdd
    },
    {
      path: '/scheddel',
      name: 'scheddel',
      component: SchedDel
    },
  ]
})
