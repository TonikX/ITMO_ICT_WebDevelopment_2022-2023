Web-программирование 2023
========================
Нургазизова Айсылу, Куканова Ульяна K33422
-------------------------
Лабораторная работа 4

- index.js 
```python
  import {createRouter, createWebHistory} from "vue-router"

import SignIn from '../views/reader/SignIn.vue'
import SignUp from '../views/reader/SignUp.vue'
import Home from '../views/Home.vue'
import Profile from '../views/reader/Profile.vue'
import ProfileEdit from '../views/reader/ProfileEdit.vue'
import LogOut from '../views/reader/LogOut.vue'
import Participation from "../components/Schedules.vue";
import Flights from "../components/Flights.vue";
import Participants from "../components/Planes.vue";


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
    path: '/planes',
    component: planes
},

{
    path: '/flights', // конкретный url-адрес
component: Flights // Ссылка на компонент
},
{
    path: '/schedules', // конкретный url-адрес
component: Schedules // Ссылка на компонент
},

]

const router = createRouter({
    history: createWebHistory(), routes
})

export default router
```
- Home.vue 

```python
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
<a href="/schedules">Расписание</a><br>
<a href="/flights">Рейсы</a><br>
<a href="/airplanes">Самолеты</a> <br>
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
- SignIn.vue
```python
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
    alert("Спасибо что Вы с нами")
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
- SignUp.vue 
```python
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

- LogOut.vue
```python
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

- Profile.vue
```python
<template>
  <div class="edit">
      <div>
        <h2>Личный кабинет</h2>
      </div>

      <h3>Форма регистрации рейса</h3>

     <form @submit.prevent="signFlights"
      ref="editForm"
      class="my-2">
      <div class="row">


        <div class="col-25">
          <label for="number">Номер рейса</label>
        </div>
        <div class="col-75">
          <input v-model="number" type="number" id="number" name="number" placeholder="Номер рейса">
        </div>
      </div>

<div class="row">
        <div class="col-25">
          <label for="distance">Расстояние до пункта назначения</label>
        </div>
        <div class="col-75">
          <input v-model="distance" type="number" id="distance" name="distance" placeholder="Расстояние в км">
        </div>
      </div>

<div class="row">
        <div class="col-25">
          <label for="departure">Пункт вылета</label>
        </div>
        <div class="col-75">
          <textarea v-model="departure" id="departure" name="departure" placeholder="Пункт вылета"></textarea>
        </div>
      </div>

<div class="row">
        <div class="col-25">
          <label for="arrival">Пункт назначения</label>
        </div>
        <div class="col-75">
          <textarea v-model="arrival" id="arrival" name="arrival" placeholder="Пункт назначения"></textarea>
        </div>
      </div>

     <div class="row">
             <div class="col-25">
               <label for="completed">Количество совершенных рейсов</label>
             </div>
             <div class="col-75">
               <input v-model="completed" type="number" id="completed" name="completed" placeholder="Количество совершенных рейсов">
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
      number: '',
      distance: '',
      departure: '',
      arrival: '',
      completed: ''
    },
  }),


  methods: {
    async signFlights () {
      
      $.ajax({
                type: "POST",
                data: {
                        number: this.number,
                        distance: this.distance,
                        departure: this.departure,
                        arrival: this.arrival,
                        completed: this.completed
                },
                url: "http://127.0.0.1:8000/schedule/create/"
            }).done(function () {
                console.log(this.data)
                //this.$router.push({ name: 'flights' })
            });
    },
   

    goHome () {
      this.$router.push({ name: 'home' })
    },

    //goEdit () {
      //this.$router.push({ name: 'profile_edit' })
    //}
  }
}
</script>

<style>

</style>
```

- ProfileEdit.vue
```python
<template>
  <div class="edit">
    <h2>Редактирование профиля</h2>
    <v-form
      @submit.prevent="saveChanges"
      ref="editForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

<!--          <v-text-field-->
<!--            label="Пароль"-->
<!--            v-model="editForm.password"-->
<!--            type="password"/>-->

          <v-text-field
            label="ФИО"
            v-model="editForm.name"
            name="name"/>

          <v-text-field
            label="Номер билета"
            v-model="editForm.library_pass"
            name="library_pass"
            type="number"/>

          <v-text-field
            label="Дата рождения"
            v-model="editForm.birth_date"
            name="birth_date"
            type="date"/>

          <v-select
            v-model="editForm.education_level"
            :items="educationOptions"
            name="education_level"
            label="Образование"
          ></v-select>

          <v-checkbox
            v-model="editForm.degree"
            :label="'Учёная степень'"
          ></v-checkbox>

          <v-text-field
            label="Адрес"
            v-model="editForm.address"
            name="address"/>

          <v-text-field
            label="Телефон"
            v-model="editForm.phone_number"
            name="phone_number"/>

          <v-btn type="submit" color="primary" dark>Сохранить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15"><router-link to="/show/profile">Назад</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'ProfileEdit',

  data: () => ({
    reader_old: Object,
    editForm: {
      // password: '',
      name: '',
      library_pass: '',
      birth_date: '',
      education_level: '',
      degree: '',
      address: '',
      phone_number: ''
    },
    educationOptions: ['e', 's', 'c']
  }),

  created () {
    this.loadReaderData()
  },

  methods: {
    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader_old = response.data

      this.editForm.planes = response.data.planes
      this.editForm.flights = response.data.flights
      this.editForm.schedules = response.data.schedules
    },

    async saveChanges () {
      for (const [key, value] of Object.entries(this.editForm)) {
        if (value === '') {
          delete this.editForm[key]
        }
      }

      try {
        const response = await this.axios
          .patch('http://127.0.0.1:8000/auth/users/me/',
            this.editForm, {
              headers: {
                Authorization: `Token ${localStorage.getItem('auth_token')}`
              }
            })
        console.log(response)

        this.$refs.editForm.reset()
        await this.$router.push({ name: 'profile' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.name) {
          alert('Имя: ' + e.response.data.name)
        } else if (e.response.data.library_pass) {
          alert('Номер билета: ' + e.response.data.library_pass)
        } else if (e.response.data.birth_date) {
          alert('Дата рождения: ' + e.response.data.birth_date)
        } else if (e.response.data.education_level) {
          alert('Образование: ' + e.response.data.education_level)
        } else if (e.response.data.degree) {
          alert('Учёная степень: ' + e.response.data.degree)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone_number) {
          alert('Телефон: ' + e.response.data.phone_number)
        } else {
          console.error(e.message)
        }
      }
    }
  }
}
</script>

<style>
</style>
```

