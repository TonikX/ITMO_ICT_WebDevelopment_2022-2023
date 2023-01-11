import { createRouter, createWebHistory } from 'vue-router'
import Dog from "@/views/Dog.vue";
import DogCreate from "@/views/DogCreate.vue"
import DogParticipation from "@/views/DogParticipation.vue";
import DogParticipationCreate from "@/views/DogParticipationCreate.vue";
import DogParticipationChange from "@/views/DogParticipationChange.vue";
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
      name: 'dog_participation',
      component: DogParticipation
    },
    {
      path: '/dog_reg/create/',
      name: 'dog_participation_create',
      component: DogParticipationCreate
    },
    {
      path: '/dog_reg/:id/',
      name: 'dog_participation_change',
      component: DogParticipationChange
    }
  ]
})

export default router
