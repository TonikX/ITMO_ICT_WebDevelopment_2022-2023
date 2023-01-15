import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import Main from '../views/Main'
import Rooms from '../views/Rooms'
import RoomsCreate from '../views/RoomsCreate'
import RoomsUpdate from '../views/RoomsUpdate'
import Clients from '../views/Clients'
import ClientsCreate from '../views/ClientsCreate'
import ClientsUpdate from '../views/ClientsUpdate'
import Bookings from '../views/Bookings'
import BookingsCreate from '../views/BookingsCreate'
import Employees from '../views/Employees'
import EmployeesCreate from '../views/EmployeesCreate'
import EmployeesUpdate from '../views/EmployeesUpdate'
import SignIn from '../views/SignIn'
import SignUp from '../views/SignUp'
import Logout from '../views/Logout'
import Hello from '../components/Hello.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/main/',
    name: 'Main',
    component: Main
  },
  {
    path: '/rooms/',
    name: 'Rooms',
    component: Rooms
  },
  {
    path: '/rooms/create/',
    name: 'RoomsCreate',
    component: RoomsCreate
  },
  {
    path: '/rooms/update/:room_id/',
    name: 'RoomsUpdate',
    component: RoomsUpdate
  },
  {
    path: '/clients/',
    name: 'Clients',
    component: Clients
  },
  {
    path: '/clients/create/',
    name: 'ClientsCreate',
    component: ClientsCreate
  },
  {
    path: '/clients/update/:client_id/',
    name: 'ClientsUpdate',
    component: ClientsUpdate
  },
  {
    path: '/bookings/',
    name: 'Bookings',
    component: Bookings
  },
  {
    path: '/bookings/create/',
    name: 'BookingsCreate',
    component: BookingsCreate
  },
  {
    path: '/employees/',
    name: 'Employees',
    component: Employees
  },
  {
    path: '/employees/create/',
    name: 'EmployeesCreate',
    component: EmployeesCreate
  },
  {
    path: '/employees/update/:emp_id/',
    name: 'EmployeesUpdate',
    component: EmployeesUpdate
  },
  {
    path: '/sign-in/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/',
    name: 'Hello',
    component: Hello
  },
  {
    path: '/sign-up/',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/logout/',
    name: 'Logout',
    component: Logout
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router