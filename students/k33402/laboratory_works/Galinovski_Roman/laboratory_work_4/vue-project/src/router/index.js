import { createRouter, createWebHistory } from 'vue-router'
import Dog from "@/views/Dog.vue";
import DogCreate from "@/views/DogCreate.vue"
import DogRegistered from "@/views/DogRegistered.vue";
import DogRegisteredCreate from "@/views/DogRegisteredCreate.vue";
import DogRegisteredChange from "@/views/DogRegisteredChange.vue";
import Home from "@/views/Home.vue";
import Registration from "@/views/Registration.vue";
import Login from "@/views/Login.vue";
import Profile from "@/views/Profile.vue";
import ProfileChange from "@/views/ProfileChange.vue";
import DogChange from "@/views/DogChange.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/registration/',
      name: 'registration',
      component: Registration,
    },
    {
      path: '/login/',
      name: 'login',
      component: Login,
    },
    {
      path: '/profile/',
      name: 'profile',
      component: Profile
    },
    {
      path: '/profile/change/',
      name: 'profile_change',
      component: ProfileChange
    },
    {
      path: '/dog/',
      name: 'dogs',
      component: Dog
    },
    {
      path: '/dog/create/',
      name: 'dogs_create',
      component: DogCreate
    },
    {
      path: '/dog/:id/',
      name: 'dog_change',
      component: DogChange
    },
    {
      path: '/dog_reg/',
      name: 'dog_registered',
      component: DogRegistered
    },
    {
      path: '/dog_reg/create/',
      name: 'dog_registered_create',
      component: DogRegisteredCreate
    },
    {
      path: '/dog_reg/:id/',
      name: 'dog_registered_change',
      component: DogRegisteredChange
    }
  ]
})

export default router