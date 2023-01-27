# ЛАБОРАТОРНАЯ РАБОТА №4

# Dogshowcase project 

* login.js 

# исходни код Регистрация библиотекарей в views

  ```js
<template>
  <div class="signIn">
    <h2>Authorizations</h2>
    <form
      @submit.prevent="setLogin"
      ref="signInForm"
      class="my-2">
          <input type="text"
                 label="Логин"
                 placeholder="Логин"
                 v-model="login"
                 name="login">
          <input
            label="Пароль"
            placeholder="Пароль"
            v-model="password"
            name="password"
            type="password">
          <button type="submit">Authorize</button>
    </form>
    <p class="mt-15">Still no account?<br>
      <router-link to="/show/signup" style="text-decoration: none; color: #198754">Register</router-link></p>
  </div>
</template>

<script>
/* eslint-disable */

import $ from "jquery";
import axios from "axios";
    export default {
      name: "AuthModals",
      data() {
        return {
          login: '',
          password: '',
        }
      },
      methods: {
        setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem("auth_token", response.auth_token)
                        sessionStorage.setItem("username", this.login)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            }
      }
    }
</script>

<style>
</style>
```

# исходни код Регистрация библиотекарей  в views

* signup.vue

```js
<template>
  <div class="signup">
    <h2>Registration</h2>
    <form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2">

          <input type="text"
            label="Логин" placeholder="Логин" v-model="login" name="login">

          <input
            label="Пароль"
            placeholder="Пароль"
            v-model="password"
            name="password"
            type="password">

          <button type="submit">Register</button>

    </form>
    <p class="mt-15">Already register? <router-link to="/show/signin" style="text-decoration: none; color: #198754">Log in</router-link></p>
  </div>
</template>

<script>
/* eslint-disable */
import $ from "jquery";
export default {
  name: 'SignUp',
  data() {
    return {
      login: '',
      password: '',
    }
  },
  methods: {
    async signUp () {
      console.log("1")
      $.ajax({
                type: "POST",
                data: {
                        username: this.login,
                        password: this.password
                },
                url: "http://127.0.0.1:8000/auth/users/"
            }).done(function () {
                console.log(this.data)
                alert("Спасибо за регистрацию")
                //this.$router.push({ name: 'signin' })
            });
    }
  }
}
</script>

<style>
</style>
```
#  исходни код "router"
 
* index.vue

```js
import Vue from 'vue';
import VueRouter from 'vue-router';


import SignIn from '../views/reader/SignIn.vue'
import SignUp from '../views/reader/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/reader/Profile.vue'
import ProfileEdit from '../views/reader/ProfileEdit.vue'
import LogOut from '../views/reader/LogOut.vue'
import ParticipationView from "@/components/ParticipationView.vue";
import ExpertsView from "@/components/ExpertsView.vue";
import ParticipantsView from "@/components/ParticipantsView.vue";
import DogRegister from "@/views/reader/DogRegister.vue"
import DogGrade from "@/views/reader/DogGrade.vue"

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
    path: '/experts', // конкретный url-адрес
    component: ExpertsView // Ссылка на компонент
  },
  {
    path: '/participants', // конкретный url-адрес
    component: ParticipantsView // Ссылка на компонент
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
```

# исходни код Редактирование профиля в components

* ParticipantsView.vue

```js
<template>
   <div class="app">
     <h1>Participants</h1>
       <a href="/" style="text-decoration: none; color: ##198754">Main</a><br><br>
     <!--<button v-on:click="fetchParticipants">Получить список участников'</button>-->

     <participants-list
         v-bind:participants="participants"
     > 
     </participants-list>
   </div>
</template>

<script>


import ParticipantsList from "./ParticipantsList.vue";
import axios from "axios";
/* eslint-disable */
export default {
 components: {
   ParticipantsList
 },

 data() { 
   return {
     participants: [], 
   }
 },
 methods: { 
   async fetchParticipants () { 
     try {
       const response = await axios.get('http://127.0.0.1:8000/participants/?format=json') 
       console.log(response.data)
       this.participants = response.data 
     } catch (e) {
       alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchParticipants() 

 }
}
</script>
```