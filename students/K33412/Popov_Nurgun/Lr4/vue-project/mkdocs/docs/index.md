# ЛАБОРАТОРНАЯ РАБОТА №4

>Мигрировать ранее написанный сайт на фреймворк Vue.JS.

 Минимальные требования:

- Должен быть подключён роутер
- Должна быть реализована работа с внешним API
- Разумное деление на компоненты

##Основные файлы проекта

* router/index.js
```javascript
import { createRouter, createWebHistory } from "vue-router";
import Main from "../views/Main.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import description from "../views/card_description.vue";
import calender from "../views/CalendarPage.vue";
import Profile from "../views/Profile.vue";
import Not_Found from "../views/404.vue";


const routes = [    
    {
       path: "/",
       name: "Main",
       component: Main,
       meta: {
           title: 'Home'
       }
    },
    {
        path: "/Login",
        name: "login",
        component: Login,
        meta: {
            title: 'Login'
        }
    },
    {
        path: "/Register",
        name: "register",
        component: Register,
        meta: {
            title: 'Register'
        }
    },
    {
        path: "/Description/:id",
        name: "description",
        component: description,
        meta: {
            title: 'description'
        }
    },
    {
        path: "/Calendar",
        name: "calendar",
        component: calender,
        meta: {
            title: 'calender'
        }
    },
    {
        path: "/Profile",
        name: "profile",
        component: Profile,
        meta: {
            title: 'Profile'
        }
    },
    {
        path: '/:pathMatch(.*)*',
        name: "Not_Found",
        component: Not_Found,
        meta:{
          title: '404'
        }
    
      }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    // массив с роутами
    routes,
});
router.beforeEach((to, from, next) =>
{
    document.title = `${to.meta.title} | Event`;
    next();
})

// экспортируем сконфигурированный роутер
export default router;
```


* Main.vue
```javascript
<template>
  <section>
    <div class="container justify-content-between mt-5 row mx-auto">
      <div class="container-xxl pt-5">
        <div class="row">
          <div class="col-12 col-xl-6 col-md-12">
            <h1>Сделай свой день интереснее с нами</h1>
            <p class="w-70 pt-3">Чем бы вы ни планировали заняться в этом году, вы всегда можете рассчитывать на помощь Meetings. С помощью Meetings люди приобретают друзей, обращаются за поддержкой, развивают свой бизнес и находят людей с общими интересами. Каждый день проводятся тысячи мероприятий — присоединяйтесь!</p>
          </div>
          <div class="col-12 col-xl-6 col-md-12">
            <img class="rounded w-100" src="../assets/Meeting.webp" alt="Meeting">
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container justify-content-between">
      <div class="row py-5">
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Карьерный рост</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Читайте с друзьями</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Двигайтесь с нами</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Пишите вместе</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Про природу</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Духовный рост</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="eventsection">
    <div class="container justify-content-between mt-5 row mx-auto">
      <div class="container-xxl pt-2">
        <div class="filters-row row">
          <div class="col-12 col-xl-6 col-md-12">
            <h2>Предстояющие мероприятия</h2>
          </div>
          <div class="col-12 col-xl-6 col-md-12">
            <div class="d-flex justify-content-end" @change="checkfilter">
              <div class="dropdown ms-3">
                <select class="form-select dropdown-color" aria-label=".form-select-lg example" id="event-type">
                  <option>Тип мероприятия</option>
                  <option value="Кино">Кино</option>
                  <option value="Вечеринка">Вечеринка</option>
                  <option value="Туризм">Туризм</option>
                </select>
              </div>          
              <div class="dropdown ms-3">
                <select class="form-select dropdown-color" aria-label=".form-select-lg example" id="event-place">
                  <option>Место проведения</option>
                  <option value="Онлайн">Онлайн</option>
                  <option value="Лично">Лично</option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <div class="row mt-4" id="event_cards">
        </div>
        <Card :cardInfo=APIResponse></Card>
        <Card :cardInfo=filteredArray></Card>
      </div>
    </div>
  </section>

  <seсtion>
    <div class="row justify-content-center text-center mt-3">
      <div class="col-auto">
        <h1 class="mt-5 mb-4">Как работает Meetings</h1>
        <p>Знакомьтесь с новыми людьми, которые разделяют ваши интересы,</p>
        <p>на онлайн- и очных мероприятиях. Создайте аккаунт бесплатно.</p>
      </div>
    </div>
  </seсtion>

  <section>
    <div class="container justify-content-between mb-5">
      <div class="row py-5">
        <div class="col">
          <div class="text-center mb-3">
            <img class="rounded w-50 mb-3" src="../assets/HandsUp.png" alt="HandsUp">
            <p class="lower-text-size mb-3">Вступить в группу</p>
              <p>Занимайтесь тем, что вам нравится, встречайтесь с другими людьми, которым это нравится, найдите свое сообщество. Остальное уже история!</p>
          </div>
        </div>
        <div class="col">
          <div class="text-center mb-3">
            <img class="rounded w-50 mb-3" src="../assets/Ticket.png" alt="Ticket">
            <p class="lower-text-size mb-3">Найти мероприятие</p>
              <p>Есть мероприятия практически на любую тему, о которой вы только можете подумать, от онлайн-игр и фотографии до йоги и пеших прогулок.</p>
          </div>
        </div>
        <div class="col">
          <div class="text-center mb-3">
            <img class="rounded w-50 mb-3" src="../assets/Group.png" alt="Group">
            <p class="lower-text-size mb-3">Создать группу</p>
              <p>Вам не нужно быть экспертом, чтобы собирать людей вместе и увлекаться общими интересами.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
  
<script>
  import axios from "axios";
  import Card from "../components/Card.vue"
  export default {
    name: "Main",
    data: function (){
      return{
        APIResponse: [],
        filteredArray: [],
      }
    },
    components:{
      Card
    },
    methods:{
      async APIData(){
        try{
          const res = await axios.get(`http://localhost:3000/events`);
          this.APIResponse = res.data;
          // console.log(this.APIResponse)
        }catch (error){
          console.log("error", error)
        }
      },
      checkfilter(){
        const eventTypeValue = document.getElementById("event-type").value;
        const categoryValue = document.getElementById("event-place").value;
        for (let i = 0; i < this.APIResponse.length; i++) {
          if ((this.APIResponse[i].eventtype===(eventTypeValue) || eventTypeValue==="Тип мероприятия") && 
              (this.APIResponse[i].eventplace===(categoryValue) || categoryValue==="Место проведения")) {
               this.filteredArray.push(this.APIResponse[i])
          } else {
            console.log("API data error")
          }
        }
        console.log(this.filteredArray)
      }
    },
      mounted() {
      this.APIData()
      // this.checkfilter()
      // console.log(this.APIResponse)
    }
  }
</script>

<style scoped>
</style>
```


* Login.vue
```javascript
<template>
  <section class="mt-5 mb-5 py-5">
    <div class="card container-xxl col-5 p-5">
      <form>
        <h1 class="text-center ">Meetings</h1>
        <p class="login-text-size text-center mb-5">Вход</p>

        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" name="email" v-model="email" placeholder="name@example.com">
        </div>

				<div class="mb-4">
          <label for="password" class="form-label">Пароль</label>
          <input type="password" class="form-control" id="password" name="password" v-model="password" placeholder="* * * * * * * *">
        </div>

        <button type="submit" class="btn btn-dark w-100 py-3 mt-4" @click.prevent="LogIn">Войти</button>

        <p class="text-center mt-3">Не зарегистрированы?  <router-link :to="{name: 'register'}" class="fw-bold text-body"><u>Регистрация</u></router-link></p>
      </form>
    </div>
  </section>
</template>

<script>
  import axios from "axios";
  import { useStateStore } from '../store/UserStatus.js'
  export default {
    name: "Login",
    data: function (){
      return{
        email: '',
        password: '',
      }
    },
    methods:{
      async LogIn(){
        if(this.email !== "" && this.password !== ""){
          const res = await axios.get(`http://localhost:3000/users?email=${this.email}&password=${this.password}`)
          if(res.status==200 && res.data.length>0){
            localStorage.setItem('userInfo', JSON.stringify(res.data));
            await this.$router.push({name: "Main"})
            const { StateChecker } = useStateStore()
            StateChecker(true);
          }else{
            alert("Ошибка, попробуйте еще раз")
          }
        }else{
          alert("Пожалуйста заполните все строки")
        }
      }
    }
  }
</script>

<style scoped>
  .login-text-size {
    font-size: large;
    font-weight: 500;
  }
</style>
```


* Register.vue
```javascript
<template>
  <section class="mt-5 mb-5 py-5">
		<div class="card container-xxl col-5 p-5">
			<form>
        <h1 class="text-center ">Meetings</h1>
        <p class="login-text-size text-center mb-5">Регистрация</p>

        <div class="mb-3">
          <label for="firstname" class="form-label">Имя</label>
          <input type="text" class="form-control" id="firstname" v-model="firstname" placeholder="Иван">
        </div>

        <div class="mb-3">
          <label for="lastname" class="form-label">Фамилия</label>
          <input type="text" class="form-control" id="lastname" v-model="lastname" placeholder="Иванов">
        </div>

        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" v-model="email" placeholder="name@example.com">
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Пароль</label>
          <input type="password" class="form-control" id="password" v-model="password" placeholder="* * * * * * * *">
        </div>

        <button type="submit" class="btn btn-dark w-100 py-3 mt-4" @click.prevent="Reg">Зарегистрироваться</button>
        
        <p class="text-center mt-3">Уже есть профиль?  <router-link :to="{name: 'login'}" class="fw-bold text-body"><u>Войти</u></router-link></p>
	    </form>
		</div>
	</section>
</template>

<script>
import axios from "axios";
import { useStateStore } from '../store/UserStatus.js'
export default {
  name: "Register",
  data: function (){
    return{
        email: '',
        password: '',
        lastname: '',
        firstname: ''
    }
  },
  methods:{
    async Reg(){
      if(this.email === '' && this.password === '' && this.lastname === '' && this.firstname === ''){
        alert('Пожалуйста заполните все строки')
      }else{
        const result = await axios.post(`http://localhost:3000/users`, {
          email: this.email,
          password: this.password,
          lastname: this.lastname,
          firstname: this.firstname
        });
        console.log(result);
        if(result.status == 201){
          console.log(result.status)
          // await this.$router.push({name: "Main"});
          localStorage.setItem('userInfo', JSON.stringify(result.data));
          await this.$router.push({name: "Main"})
          const { StateChecker } = useStateStore()
            StateChecker(true);
        }
      }
    }
  }
}
</script>

<style scoped>
  .login-text-size {
    font-size: large;
    font-weight: 500;
  }
</style>
```


* card_description.vue
```javascript
<template>
  <section id="about_event">
    <div class="container-xxl col-10 mt-4">
      <h2 class="mb-3">{{this.dataToUsed.title}}</h2>
      <div class="row mb-5">
        <div class="col-8">
          <img class="rounded w-100 mb-3" :aria-labelledby="dataToUsed.id" :src="dataToUsed.img_src">
          <p class="lower-text-size py-3"><strong>Детали</strong></p>
          <p class="event-text-size mb-3">{{this.dataToUsed.description}}</p>
        </div>
        <div class="col">
          <div class="rounded-3 p-3 event-right-card mx-auto mb-3" style="width: 350px;">
            <div class="container justify-content-between col-12 row">
              <div class="col-4">
                <img class="rounded w-100" :src="dataToUsed.img_src_2" alt="books">
              </div>
              <div class="col">
                <p class="event-text-size">{{this.dataToUsed.group_name}}</p>
                <p class="event-text-size event-bottom-text">{{this.dataToUsed.group_type}}</p>
              </div>
            </div>
          </div>
          <div class="rounded-3 event-right-card mx-auto mb-3" style="width: 350px;">
            <div class="p-3">
              <p class="event-text-size">Дата и время:</p>
              <p class="event-text-size event-bottom-text mb-3">{{this.dataToUsed.date}}</p>
              <p class="event-text-size">Место:</p>
              <p class="event-text-size event-bottom-text">{{this.dataToUsed.location}}</p>
            </div>
            <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1998.99229034957!2d30.3539683!3d59.9322701!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469631a5b366e8cd%3A0x5db5df3c54a9e502!2sMama%20Roma!5e0!3m2!1sru!2sru!4v1668966318386!5m2!1sru!2sru" height="300" style="border:0;" class="w-100" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map"></iframe>
          </div>
          <div class="rounded-3 p-3 event-right-card mx-auto mb-3" style="width: 350px;">
            <div class="text-center">
              <a href="#" @click.prevent="joinEvent(this.dataToUsed.id)" class="btn btn-primary">Присоединиться к мероприятию</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import axios from "axios";
  import Card from "../components/Card.vue"
  import { storeToRefs } from 'pinia'
  import { useStateStore } from '../store/UserStatus.js'
  export default {
    name: "card_description",
    components:{
        Card
    },
    data: function (){
      return{
          dataToUsed: [],
          URLParam: this.$route.params.id,
          generalCardData:[],
          CheckUserState: null
      }
    },
    methods:{
      async fetMethod(){
        const res = await axios.get(`http://localhost:3000/events/${this.URLParam}`);
        this.dataToUsed = res.data;
        console.log(this.dataToUsed)
        console.log(localStorage.getItem('userInfo.'))
      },
      async Gennral (){
        const test = await axios.get(`http://localhost:3000/events`);
        this.generalCardData = test.data;
      },
      async joinEvent(sth){
        if (this.CheckUserState === false){
          alert ("Register Or log in first please")
        }else{
          let uidFromLocalStorage = JSON.parse(localStorage.getItem('userInfo'));
          const sender = await axios.post(`http://localhost:3000/user_joined_events`,{
            user_id: uidFromLocalStorage[0].id ,
            event_id: sth,
          });
          alert('Event Has added to your Profile')
          console.log(sender)
        }
      },
      checkState(){
        const  { userState } = storeToRefs(useStateStore())
        this.CheckUserState= userState;
      }
    },
    mounted() {
      this.fetMethod()
      this.Gennral()
      this.checkState()
    }
  }
</script>

<style scoped>
  .event-right-card {
    background-color: #f1f1f1;
  }
  .event-text-size {
    font-size: medium;
    font-weight: 500;
  }
  .event-bottom-text {
    opacity: .7;
  }
</style>
```


* CalendarPage.vue
```javascript
<template>
  <base-layout class="mt-3">
    <h1>Календарь мероприятий</h1>
    <full-calendar class="mb-5"
      :options="{
        events: calendarEvents,
        eventChange: handleEventChange,
        dateClick: handleDateClick,
        eventClick: handleEventClick
      }"
    />

    <div class="modal fade" ref="detailEvent" tabindex="-1" aria-labelledby="detailEventLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="detailEventLabel">{{selectedEvent.title}}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p><strong>Описание:</strong> {{ selectedEvent.description }}</p>

            <p>{{ selectedEvent.formattedDate() }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" ref="eventCreate" tabindex="-1" aria-labelledby="eventCreateLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="eventCreateLabel">Добавить событие</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm" class="d-flex flex-column" ref="eventForm">
              <input type="text" v-model="form.title" class="my-1">
              <input type="date" v-model="form.date" class="my-1">
              <textarea cols="30" rows="10" v-model="form.description" class="my-1" />

              <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </base-layout>
</template>

<script>
  import { mapActions, mapState } from 'pinia'
  import { Modal } from 'bootstrap'
  import useCalendarEventsStore from '../store/calendarEvents'
  import BaseLayout from '../layouts/BaseLayout.vue'
  import FullCalendar from '../components/FullCalendar.vue'

  export default {
    name: 'CalendarPage',
    components: { BaseLayout, FullCalendar },
    computed: {
      ...mapState(useCalendarEventsStore, {
        calendarEvents: 'calendarEvents',
        selectedEvent: (state) => {
          return {
            ...state.selectedEvent,
            formattedDate: () => {
              const date = state.selectedEvent.date
              return new Date(date).toLocaleDateString('ru-RU')
            }
          }
        }
      })
    },
    data() {
      return {
        form: {
          title: '',
          description: '',
          date: ''
        },
        eventCreateModal: null
      }
    },
    methods: {
      ...mapActions(useCalendarEventsStore, ['loadCalendarEvents', 'loadEventById', 'createEvent']),
      handleEventChange(payload) {
        console.log('event change', payload)
      },
      handleDateClick(payload) {
        console.log('date clicked', payload)
        const { dateStr } = payload
        this.form.date = dateStr
        this.eventCreateModal = new Modal(this.$refs.eventCreate)
        this.eventCreateModal.show()
      },
      async handleEventClick(payload) {
        await this.loadEventById(payload.event._def.publicId)
        const eventModal = new Modal(this.$refs.detailEvent)
        eventModal.show()
      },
      async submitForm() {
        await this.createEvent(this.form)
        this.$refs.eventForm.reset()
        this.eventCreateModal.hide()
        await this.loadCalendarEvents()
      }
    },
    mounted() {
      this.loadCalendarEvents()
    }
  }
</script>
```


* Profile.vue
```javascript
<template>
  <section>
    <div class="container-xxl col-11" style="margin-top: 50px;">
      <div class="row justify-content-center">
        <div class="col-md-3">
          <div class="py-3 bg-dark rounded-top">
            <img src="../assets/person.jpeg" class="w-50 mx-auto d-block mt-3" alt="person">
            <p class="login-text-size text-white text-center mt-4"> {{this.CurrentUser.firstname}} {{this.CurrentUser.lastname}}</p>
            <p class="text-white text-center">{{this.CurrentUser.email}}</p>
          </div>
          <ul class="list-group">
            <li class="list-group-item">
              <a class="text-danger text-decoration-none link-dark" @click.prevent="logout">Выйти</a>
            </li>
          </ul>
        </div>

        <div class="col-md-9 mb-5" style="padding-left: 50px;">
          <h3>Предстояющие мероприятия</h3>
          <Card :card-info="eventData"></Card>
        </div>		
      </div>
    </div>	
  </section>
</template>

<script>
  import axios from "axios";
  import Card from '../components/Card'
  import { useStateStore } from '../store/UserStatus.js'
  export default {
    name: "Profile",
    data:function (){
      return{
        eventData: [],
        CurrentUser: ''
      }
    },
    components:{
      Card
    },
    methods:{
      async dataFromAPI(){
        try{
          const user = JSON.parse(localStorage.getItem('userInfo'));
          const CurrentUID = user[0].id;
          this.CurrentUser = user[0];
          const res = await axios.get(`http://localhost:3000/user_joined_events?user_id=${CurrentUID}`);
          for(let i =0; i <res.data.length; i++){
            let selectedEvents= (await axios.get(`http://localhost:3000/events/${res.data[i].event_id}`)).data
            this.eventData.push(selectedEvents)
          }
        }catch (error){
          console.log("error", error)
        }
      },
      logout(){
        const { StateChecker } = useStateStore()
        localStorage.clear();
        StateChecker(false);
        window.location.reload();
        this.$router.push({name: "Main"})
      }
    },
    mounted() {
      this.dataFromAPI()
    }
  }
</script>

<style scoped>
  .login-text-size {
    font-size: large;
    font-weight: 500;
  }
</style>
```


# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
