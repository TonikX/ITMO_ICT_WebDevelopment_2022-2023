import Index from "@/views/Index.vue"
import Login from "@/views/Login.vue"
import Dog from "@/views/Dogs.vue"
import Register from "@/views/Register.vue"
import Profile from "@/views/Profile.vue"
import Registration from "@/views/Registration.vue"
import CreateDog from "@/views/CreateDog.vue"
import ChangeDog from "@/views/ChangeDog.vue"
import CreateRegister from "@/views/CreateRegister.vue"
import ChangeRegister from "@/views/ChangeRegister.vue"
import ProfileChange from "@/views/ProfileChange.vue"
import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter)
const routes = [
  {
    path: "/",
    name: "Index",
    component: Index
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/register",
    name: "Registration",
    component: Registration
  },
  {
    path: "/dog",
    name: "dogs",
    component: Dog
  },
  {
    path: "/dog_reg",
    name: "Register",
    component: Register
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile
  },
  {
    path: "/dog/create/",
    name: "CreateDog",
    component: CreateDog
  },
  {
    path: "/dog/:id/",
    name: "ChangeDog",
    component: ChangeDog
  },
  {
    path: "/dog_reg/create/",
    name: "CreateRegister",
    component: CreateRegister
  },
  {
    path: "/dog_reg/:id/",
    name: "ChangeRegister",
    component: ChangeRegister
  },
  {
    path: "/profile/change",
    name: "ProfileChange",
    component: ProfileChange
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router
