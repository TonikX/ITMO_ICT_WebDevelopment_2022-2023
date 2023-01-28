# **Лабораторная работа 4**

-------------------------

## Задание 
Создать программную систему, предназначенную для администрации аэропорта
некоторой компании-авиаперевозчика.
Рейсы обслуживаются бортами, принадлежащими разным авиаперевозчикам. О каждом самолете необходима следующая минимальная информация: номер самолета, тип, число мест, скорость полета, компания-авиаперевозчик. Один тип самолета может летать на разных маршрутах и по одному маршруту могут летать разные типы самолетов.
О каждом рейсе необходима следующая информация: номер рейса, расстояние до пункта назначения, пункт вылета, пункт назначения; дата и время вылета, дата и время прилета, транзитные посадки (если есть), пункты посадки, дата и время транзитных посадок и дат и время их вылета, количество проданных билетов. Каждый рейс обслуживается определенным экипажем, в состав которого входят командир корабля, второй пилот, штурман и стюардессы или стюарды. Каждый экипаж может обслуживать разные рейсы на разных самолетах. Необходимо предусмотреть наличие информации о допуске члена экипажа к рейсу.
Администрация компании-владельца аэропорта должна иметь возможность принять работника на работу или уволить. При этом необходима следующая информация: ФИО, возраст, образование, стаж работы, паспортные данные. Эта же информация необходима для сотрудников сторонних компаний.

## Основные файлы
* `index.js`
```js
import {createRouter, createWebHistory} from "vue-router"

import SignIn from '../views/reader/SignIn.vue'
import SignUp from '../views/reader/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/reader/Profile.vue'
import ProfileEdit from '../views/reader/ProfileEdit.vue'
import LogOut from '../views/reader/LogOut.vue'
import Workers from "../components/Workers.vue";


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
    path: '/workers',
    component: Workers
  },

]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router
```
* `SignUp.vue` - Регистрация
```js
<template>
  <div class="signup">
    <h2>Регистрация</h2>
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

          <button type="submit">Зарегистрироваться</button>

    </form>
    <p class="mt-15">Уже зарегистрированы? <router-link to="/show/signin">Войти</router-link></p>
  </div>
</template>

<script>
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
                this.$router.push({ name: 'signin' })
            });
    }
  }
}
</script>

<style>
</style>
```
* `SignIn.vue` - Авторизация
```js
<template>
  <div class="signIn">
    <h2>Авторизация</h2>
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
          <button type="submit">Авторизоваться</button>
    </form>
    <p class="mt-15">Ещё нет аккаунта?<br>
      <router-link to="/show/signup">Зарегистрироваться</router-link></p>
  </div>
</template>

<script>

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
                        alert("Авторизация успешно проведена")
                        sessionStorage.setItem("auth_token", response.auth_token)
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
* `LogOut.vue` - Выход
```js
<script>
import axios from 'axios'
//Vue.prototype.$axios = axios
//import Vue from 'vue'

export default {
  name: 'LogOut',
  methods: {
    LogOut () {
      try {
        const token = sessionStorage.getItem('auth_token')
        const data = {}
        if (token) {
          console.log(token)
          //this.axios.defaults.headers.common.Authorization = `token ${token}`
          //console.log(this.axios)

          sessionStorage.setItem('auth_token', '-1')
          //console.log('h ' + token)
          axios.post('http://127.0.0.1:8000/auth/token/logout/', data, {
            headers: {
            'Authorization': `token ${token}` 
            }
          }).then(response => {
            console.log('SIGN OUT RESPONSE', response)
          // localStorage.removeItem('token')
          // this.$bus.$emit('logged', 'User logged out')
            this.$router.push({ name: 'home' })
        })
        }

      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    this.LogOut()
  }
}
</script>

<style scoped>
</style>
```
* `Home.vue` - Главная
```js
<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Аэропорт</h2><br>
        <h3 style='color: black; text-decoration: none'>
        <a href="/flights">Рейсы</a><br>
        <a href="/airplanes">Самолеты</a><br>
        <a href="/workers">Работники</a><br>
        </h3>
      </v-card-title>
      <v-card-text>
        <h3>
          <template  v-if="this.authorized">
            <a @click="goProfile">Личный кабинет</a><br>
            <a @click="goLogOut">Выйти</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn">Войти</a><br>
            <router-link to="/show/signup">Зарегистрироваться</router-link>
          </template>
        </h3>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',

  data: () => ({
    authorized: false
  }),

  created () {
    console.log('hehe' + ' ' + sessionStorage.getItem('auth_token'))
    if (sessionStorage.getItem('auth_token')) {
      if (sessionStorage.getItem('auth_token') !== '-1') {
        this.authorized = true
      }
    }
  },

  methods: {
    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goProfile () {
      this.$router.push({ name: 'profile' })
    },

    goLogOut () {
      this.$router.push({ name: 'logout' })
    },

    goSignIn () {
      this.$router.push({ name: 'signin' })
    }
  }
}
</script>

```
* `Workers.vue`
```js
<template>
   <div class="app">
     <h1>Работники</h1>
       <a href="/">Главная</a><br><br>
     <button v-on:click="fetchWorker">Вывести список работников</button>

     <workers-list
         v-bind:workers="workers"
     > 
     </workers-list>
   </div>
</template>

<script>

import WorkersList from "./WorkersList.vue";
import axios from "axios";

export default {
 components: {
   WorkersList
 },

 data() { 
   return {
     workers: [],
   }
 },
 methods: { 
   async fetchWorker () {
     try {
       const response = await axios.get('http://localhost:8000/airport/workers/?format=json')
       console.log(response.data)
       this.workers = response.data
     } catch (e) {
       alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchWorker()

 }
}
</script>
```
* `WorkersList.vue` - Вывод списка сотрудников
```js
<template>
<div>
 <div  v-for="worker in workers" :key="worker.worker_id">
   <div><strong>Имя:</strong> {{ worker.name }}</div>
   <div><strong>Возраст:</strong> {{ worker.age }}</div>
   <div><strong>Образование:</strong> {{ worker.education }}</div>
   <div><strong>Опыт работы:</strong> {{ worker.work_exp }}</div>
   <div><strong>Серия и номер паспорта:</strong> {{ worker.passport }}</div>
   <div><strong>Должность:</strong> {{ worker.occupation }}</div>
   <div><strong>Доступ к рейсам:</strong> {{ worker.access }}</div>
   <div><strong>Работодатель:</strong> {{ worker.employer }}</div>
   <div><strong>Статус:</strong> {{ worker.status }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: { 
   workers: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>

</style>
```
* `Profile.vue` - Форма регистрации сотрудников
```js
<template>
  <div class="edit">
      <div>
        <h2>Личный кабинет</h2>
      </div>

      <h3>Форма регистрации работника</h3>

     <form @submit.prevent="signWorkers"
      ref="editForm"
      class="my-2">
      <div class="row">


        <div class="col-25">
          <label for="name">Имя</label>
        </div>
        <div class="col-75">
          <input v-model="name" type="text" id="name" name="name" placeholder="Имя">
        </div>
      </div>


      <div class="row">
        <div class="col-25">
          <label for="age">Возраст</label>
        </div>
        <div class="col-75">
          <input v-model="age" id="age" name="age" placeholder="Возраст">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="education">Образование</label>
        </div>
        <div class="col-75">
          <textarea v-model="education" id="education" name="education" placeholder="Образование"></textarea>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="work_exp">Опыт работы</label>
        </div>
        <div class="col-75">
          <input v-model="work_exp" id="work_exp" name="work_exp" placeholder="Опыт работы">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="passport">Паспортные данные</label>
        </div>
        <div class="col-75">
          <input v-model="passport" id="passport" name="passport" placeholder="Серия и номер">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="occupation">Должность</label>
        </div>
        <div class="col-75">
          <select v-model="occupation" id="occupation" name="occupation">
            <option value="COMMANDER">commander</option>
            <option value="RELIEF PILOT">relief pilot</option>
            <option value="NAVIGATOR">navigator</option>
            <option value="ATTENDANT">attendant</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="employer">Работодатель</label>
        </div>
        <div class="col-75">
          <select v-model="employer" id="employer" name="employer">
            <option value="S7">S7</option>
            <option value="POBEDA">Pobeda</option>
            <option value="AEROFLOT">Aeroflot</option>
            <option value="NORDSTAR">Nordstar</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="status">Статус</label>
        </div>
        <div class="col-75">
          <select v-model="status" id="status" name="status">
            <option value="WORKING">working</option>
            <option value="RETIRED">retired</option>
            <option value="FIRED">fired</option>
          </select>
        </div>
      </div>

      <button type="submit">Зарегистрировать</button>
       
  </form>
  <br>
    <div>
      <div style="margin-top:1cm">
        <!--<a @click.prevent="goCatalogue">Каталог</a><br>-->
        <a @click.prevent="goHome">На главную</a>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
export default {
  name: 'Profile',

  data: () => ({
    editForm: {
      name: '',
      age: '',
      education: '',
      work_exp: '',
      passport: '',
      occupation: '',
      employer: '',
      status: ''
    },
    //options: ['COMMANDER', 'RELIEF PILOT', 'NAVIGATOR', 'ATTENDANT'], ['S7', 'POBEDA', 'AEROFLOT', 'NORDSTAR'], ['WORKING', 'RETIRED', 'FIRED']
  }),


  methods: {
    async signWorkers () {
      
      $.ajax({
                type: "POST",
                data: {
                        name: this.name,
                        age: this.age,
                        education: this.education,
                        work_exp: this.work_exp,
                        passport: this.passport,
                        occupation: this.occupation,
                        employer: this.employer,
                        status: this.status,
                        access: false
                },
                url: "http://127.0.0.1:8000/airport/worker/create"
            }).done(function () {
                console.log(this.data)
                //this.$router.push({ name: 'workers' })
            });
    },
   

    goHome () {
      this.$router.push({ name: 'home' })
    },

  }
}
</script>

<style>

</style>
```