# Лабораторная работа №2

## Описание работы

- Реализовать интерфейсы авторизации, регистрации и изменения учётных данных и настроить взаимодействие с серверной частью
- Реализовать клиентские интерфейсы и настроить взаимодействие с серверной частью
- Подключить vuetify или аналогичную библиотеку
- Реализовать документацию, описывающую работу разработанных интерфейсов средствами MkDocs

## Файлы

* `App.vue`
```JavaScript
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

* `router/index.js`
```html
<template>
  <v-app>
    <v-app-bar
      app
      color="#8D6E63"
      dark
    >
      <div class="d-flex align-center"> 
        <v-icon size="46">mdi-dog</v-icon>
        <div class="text-h4">DogsApp</div>
      </div>

      <v-spacer></v-spacer>


    </v-app-bar>

    <v-main>
       <router-view/>
    </v-main>
  </v-app>
</template>

<script>
//import Home from "@/views/Home.vue"

export default {
  name: 'App',

  // components: {
  //   Home
  // },

  data: () => ({
    //
  }),
};
</script>
```

## Views 

* `Home.vue`
```html
<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Добро пожаловать на шоу собак!</h2>
      </v-card-title>  
      <v-card-text>
        <h2>
          <a href="/participation" style="text-decoration: none; color: #4E342E">Участия</a><br>
          <a href="/experts" style="text-decoration: none; color: #4E342E">Эксперты</a><br>
          <a href="/participants" style="text-decoration: none; color: #4E342E">Участники</a> <br>
          <template  v-if="this.authorized">
            <a @click="goProfile" style="text-decoration: none; color: #4E342E">Личный кабинет</a><br>
            <a @click="goLogOut" style="text-decoration: none; color: #4E342E">Выйти</a><br>
          </template>
          <template v-else>
            <a @click="goSignIn" style="text-decoration: none; color: #4E342E">Войти</a><br>
            <router-link to="/show/signup" style="text-decoration: none; color: #4E342E">Зарегистрироваться</router-link>
          </template>
        </h2>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src
/* eslint-disable */

export default {
  name: 'Home',

  data: () => ({
    authorized: false
  }),

  created () {
    console.log('hehe' + ' ' + sessionStorage.getItem('auth_token'))
    console.log('hehe' + ' ' + sessionStorage.getItem('username'))
    if (sessionStorage.getItem('auth_token')) {
      if (sessionStorage.getItem('auth_token') !== '-1') {
        this.authorized = true
      }
    }
  },

  methods: {

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

* `DogGrade.vue`
```html
<template>
  <div class="edit">
    <h3>Оценка собаки</h3>
    <v-form
      @submit.prevent="signPart" 
      ref="editFormPart"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">
          
          <v-select
            v-model="editFormPart.participant"
            :items="participants"
            item-text="name"
            item-value="id"
            name="participant"
            label="Участник"
          ></v-select>

          <v-select
            v-model="editFormPart.medal"
            :items="medals"
            name="medal"
            label="Медаль"
          ></v-select>

          <v-text-field
            label="Дата вакцинации"
            v-model="editFormPart.vaccinated"
            name="vaccinated"
            type="date"/>

          <v-checkbox
            v-model="editFormPart.dismissed"
            :label="'Пропуск участия'"
          ></v-checkbox>


          <v-text-field
            label="Оценка"
            v-model="editFormPart.final_grade"
            type='number'
            name="final_grade"/>

            <v-btn type="submit" color="#4E342E" dark>Оценить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goProfile" style="text-decoration: none; color: #4E342E">Назад</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import $ from "jquery";
const array1 = [];
import axios from "axios";

export default {
  name: 'DogGrade',
  data: () => ({

    editFormPart: {
      medal: "",
      vaccinated: "",
      dismissed: "",
      final_grade: "",
      participant: "",
    },

    medals: ['g', 's', 'b'],
    participants: array1, 
  }),
    methods: {
        
        async signPart () {
            console.log(1)
        
        $.ajax({
                    type: "POST",
                    data: {
                            medal: this.editFormPart.medal,
                            vaccinated: this.editFormPart.vaccinated,
                            dismissed: this.editFormPart.dismissed,
                            final_grade: this.editFormPart.final_grade,
                            participant: this.editFormPart.participant,
                    },
                    url: "http://127.0.0.1:8000/participation/"
                }).done(function () {
                    console.log(this.data)
                    alert("Готово")
                    //this.$router.push({ name: 'participants' }) //сделать Participants.vue
                });
        },

        goProfile () {
        this.$router.push({ name: 'profile' })
    }
    },
      beforeMount: function () {
        this.$nextTick(async function () {
            const response = await axios.get('http://127.0.0.1:8000/participants/?format=json')
            for (let part of response.data) {
                array1.push(part);
      }
    })
  }
        
}


</script>
```

* `DogRegister.vue`
```html
<template>
   <div class="edit">
    <h3>Регистрация собаки</h3>
      <v-form
      @submit.prevent="signDogs"
      ref="editForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

          <v-text-field
            label="Кличка"
            v-model="editForm.name"
            name="name"/>

          <v-select
            v-model="editForm.breed"
            :items="options"
            name="breed"
            label="Порода"
          ></v-select>

          <v-text-field
            label="Возраст"
            v-model="editForm.age"
            name="age"
            type="number"/>

          <v-text-field
            label="Родословная"
            v-model="editForm.family"
            name="family"/>


          <v-text-field
            label="Данные хозяина"
            v-model="editForm.owner_data"
            name="owner_data"/>

            <v-btn type="submit" color="#3E2723" dark>Зарегистрировать</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goProfile" style="text-decoration: none; color: #4E342E">Назад</a>
      </v-card-text>
    </v-card>
   </div>
</template>

<script>
import $ from "jquery";
export default {
  name: 'DogRegister',
  data: () => ({ 
    editForm: {
      //participant: Object,
      name: '',
      breed: '',
      age: '',
      family: '',
      owner_data: '',
      //club,

    },

    options: ['h', 'b', 't'],
    //participants: 
  }),
    methods: {
        async signDogs () {
            console.log(1)

        $.ajax({
                    type: "POST",
                    data: {
                            name: this.editForm.name,
                            breed: this.editForm.breed,
                            age: this.editForm.age,
                            family: this.editForm.family,
                            owner_data: this.editForm.owner_data
                    },
                    url: "http://127.0.0.1:8000/participants/"
                }).done(function () {
                    console.log(this.data)
                    alert("Собака добавлена")
                    //this.$router.push({ name: 'participants' }) //сделать Participants.vue
                });
        },

        goProfile () {
        this.$router.push({ name: 'profile' })
    },
    }
}

</script>
```

* `LogOut.vue`
```html
<script>
import axios from 'axios'
/* eslint-disable */
//Vue.prototype.$axios = axios
//import Vue from 'vue'

export default {
  name: 'LogOut',
  methods: {
    LogOut () {
      try {
        const token = sessionStorage.getItem('auth_token')
        if (token) {     
          const data = {}    
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

* `Profile.vue`
```html
<template>
  <div class="edit">
    <h2>Личный кабинет</h2>
    <h3>Добро пожаловать, {{login ()}} </h3>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <div class="text--primary">
          Имя: <b>{{ this.first_name }}</b> <br>
          Фамилия: <b>{{ this.last_name }} </b><br>
          Телефон: <b>{{ this.tel }} </b><br>
        </div><br><br>
        <a @click.prevent="goRegister" style="text-decoration: none; color: #4E342E">Зарегистрировать собаку</a> <br>
        <a @click.prevent="goGrade" style="text-decoration: none; color: #4E342E">Оценить собаку</a> <br>
        <a @click.prevent="goEdit" style="text-decoration: none; color: #4E342E">Редактировать профиль</a> <br>
        <a @click.prevent="goHome" style="text-decoration: none; color: #4E342E">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
import $ from "jquery";
export default {
  name: 'Profile',
  data () {
    return {
      userme: Object,
      first_name: '',
      last_name: '',
      tel: '',
    }
  },
  created () {
    this.loadReaderData()
  },

  methods: {

    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
      this.first_name = response.data.first_name
      this.last_name = response.data.last_name
      this.tel = response.data.tel
    },

    goHome () {
      this.$router.push({ name: 'home' })
    },

    goRegister () {
      this.$router.push({ name: 'regdog' })
    },

    goEdit () {
      this.$router.push({ name: 'profile_edit' })
    },

    goGrade () {
      this.$router.push({ name: 'grading' })
    },

    login () {
      return (sessionStorage.getItem('username'))
}
  }
}
</script>

<style>

</style>
```


* `ProfileEdit.vue`
```html
<template>
  <div class="edit">
    <h2>Редактирование профиля</h2>
    <v-form
      @submit.prevent="saveChanges"
      ref="changeForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

          <v-text-field
            label="Имя"
            v-model="changeForm.first_name"
            name="first_name"/>

          <v-text-field
            label="Фамилия"
            v-model="changeForm.last_name"
            name="last_name"/>

          <v-text-field
            label="Телефон"
            v-model="changeForm.tel"
            name="tel"/>

          <v-btn type="submit" color="#3E2723" dark >Сохранить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15"><router-link to="/show/profile" style="text-decoration: none; color: #4E342E">Назад</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'ProfileEdit',

  data: () => ({
    reader_old: Object,
    changeForm: {
      // password: '',
      first_name: '',
      last_name: '',
      tel: '',
    },
  }),

  methods: {
    // async loadReaderData () {
    //   const response = await this.axios
    //     .get('http://127.0.0.1:8000/auth/users/me/', {
    //       headers: {
    //         Authorization: `Token ${sessionStorage.getItem('auth_token')}`
    //       }
    //     })
    //   this.reader_old = response.data
    //   this.changeForm.first_name = response.data.first_name
    //   this.changeForm.last_name = response.data.last_name
    //   this.changeForm.tel = response.data.tel
    // },
    async saveChanges () {
      for (const [key, value] of Object.entries(this.changeForm)) {
        if (value === '') {
          delete this.changeForm[key]
        }
      }
      try {
        const response = await this.axios
          .patch('http://127.0.0.1:8000/auth/users/me/',
            this.changeForm, {
              headers: {
                Authorization: `Token ${sessionStorage.getItem('auth_token')}`
              }
            })
        console.log(response)
        this.$refs.changeForm.reset()
        await this.$router.push({ name: 'profile' })
      } catch (e) {
          console.error(e.message)
        }
      }
    }
  }

</script>

<style>
</style>
```

* `SignIn.vue`
```html
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
      <router-link to="/show/signup" style="text-decoration: none; color: #4E342E">Зарегистрироваться</router-link></p>
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

* `SignUp.vue`
```html
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
    <p class="mt-15">Уже зарегистрированы? <router-link to="/show/signin" style="text-decoration: none; color: #4E342E">Войти</router-link></p>
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