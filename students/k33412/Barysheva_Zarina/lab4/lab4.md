# Лабораторная работы №4
Реализация клиентской части приложения средствами vue.js.
* Настроить для серверной части, реализованной в лабораторной работе №3 CORS (Cross-origin resource sharing)
* Реализовать интерфейсы авторизации, регистрации и изменения учётных данных и настроить взаимодействие с серверной частью.
* Реализовать клиентские интерфейсы и настроить взаимодействие с серверной частью

## Серверная часть
Серверная часть реализована в рамках *Лабораторной работы №3*, основные материалы по ней в *Лабораторной работе №3*

## Клиентская часть

Директория `merofond-vue` содержит:
* `public` - использованные изображения
* `src/router/index.js` - роутинг, пути ссылок страниц
* `src/components` - реализованные компоненты
* `src/views` - реализованные Views

### Роутер
```
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/events',
      name: 'eventlist',
      component: () => import('../views/EventListView.vue')
    },
    {
      path: '/user',
      name: 'user',
      component: () => import('../views/User.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignUpView.vue')
    },
    {
      path: '/event',
      name: 'event',
      component: () => import('../views/EventView.vue')
    }
  ]
})

export default router
```

### Компоненты
LoginComp.vue - Компонент формы входа
```
<template>
  <span id="background">
    <div class="mb-3 text-center">
      <label for="login" class="form-label fs-5">Имя пользователя</label>
      <input
        :class="{ 'form-control': true, 'is-invalid': retryEnter }"
        id="login"
        v-model="username"
      />
    </div>
    <div class="mb-3 text-center">
      <label for="pass" class="form-label fs-5">Пароль</label>
      <input
        type="password"
        :class="{ 'form-control': true, 'is-invalid': retryEnter }"
        id="pass"
        v-model="password"
      />
      <div
        v-if="retryEnter"
        id="validationServerUsernameFeedback"
        :class="{ 'invalid-feedback': retryEnter }"
        class="text-center"
      >
        Неправильный логин или пароль. Попробуйте снова
      </div>
    </div>
    <div class="d-grid gap-2 mb-3">
      <button
        class="btn text-light"
        @click="authorize"
        style="background-color: #2a9d8f"
      >
        Войти
      </button>
    </div>
    <p class="text-center text-muted">Еще нет аккаунта?</p>
    <div class="d-grid gap-2">
      <button class="btn" @click="goSignUp" style="background-color: #e9c46a">
        Зарегистрироваться
      </button>
    </div>
  </span>
</template>

<script>

import axios from "axios";

export default {
  data() {
    return {
      password: "",
      username: "",
      retryEnter: false,
    };
  },
  methods: {
    goEvents() {
      this.$router.replace({ path: "/events" });
    },
    goSignUp() {
      this.$router.replace({ path: "/signup" });
    },
    goUser() {
      this.$router.replace({ path: "/about" });
    },
    authorize() {
      axios
        .post("http://127.0.0.1:7777/auth/token/login", {
          username: this.username,
          password: this.password,
        })
        .then((resp) => {
          localStorage.setItem("token", resp.data.auth_token);
          this.goEvents();
        })
        .catch((e) => {
          this.retryEnter = true;
        });
    },
  },
};
</script>

<style>
#background {
  background-color: white;
}
p {
  color: var(--main-font-color);
}
</style>
```

SignUpComp.vue - компонент формы регистрации
```
<template>
    <span id="background">
      <div class="mb-3 text-center">
        <label for="login" class="form-label fs-5">Имя пользователя</label>
        <input
          :class="{ 'form-control': true, 'is-invalid': retryEnter }"
          id="login"
          v-model="username"
        />
      </div>
      <div class="mb-3 text-center">
        <label for="pass" class="form-label fs-5">Пароль</label>
        <input
          type="password"
          :class="{ 'form-control': true, 'is-invalid': retryEnter }"
          id="pass"
          v-model="password"
        />
        <div
          v-if="retryEnter"
          id="validationServerUsernameFeedback"
          :class="{ 'invalid-feedback': retryEnter }"
          class="text-center"
        >
          Пароль не должен быть похож на имя пользователя и должен содержать больше 8 символов
          ИЛИ 
          Это имя уже занято, попробуйте другое
        </div>
      </div>
      <div class="d-grid gap-2 mb-3">
        <button class="btn text-light" @click="registration" style="background-color: #2A9D8F;">Зарегистрироваться</button>
      </div>
      <p class="text-center text-muted">Есть аккаунт?</p>
      <div class="d-grid gap-2">
        <button class="btn" @click="goLogin" style="background-color: #E9C46A;">
            Войти 
        </button>
      </div>
    </span>
  </template>
  
  <script>
  
  import axios from "axios";
  
  export default {
//   setup() {
//     if (localStorage.getItem("token")) {
//       router.replace({ path: "/user" });
//     }
//   },
  data() {
    return {
      password: "",
      username: "",
      retryEnter: false,
    };
  },
  methods: {
    goEvents() {
      this.$router.replace({ path: "/events" });
    },
    goLogin() {
      this.$router.replace({ path: "/login" });
    },
    registration() {
        axios
            .post("http://127.0.0.1:7777/auth/users/", {
            username: this.username,
            password: this.password,
            })
            .then((resp) => {
            this.authorize();
            })
            .catch((e) => {
            this.retryEnter = true;
            });
    },
    authorize() {
      axios
        .post("http://127.0.0.1:7777/auth/token/login", {
          username: this.username,
          password: this.password,
        })
        .then((resp) => {
          localStorage.setItem("token", resp.data.auth_token);
          this.goEvents();
        // })
        // .catch((e) => {
        //   this.retryEnter = true;
        });
    },
  },
};
</script>

<style>
#background {
  background-color: white;
}
p {
  color: var(--main-font-color);
}
</style>
```

EventCard - компонент карточки мероприятия
```
<template>
    <div class="card" style="width: 100%; height: 45rem;">
        <img src="eventcard.jpg" class="card-img-top" alt="...">
        <div class="card-body" style="height: 100%;">
            <h5 class="card-title"> {{ event.title }}</h5>
            <p class="card-text">{{ event.description }}</p>
        </div>
        <ul class="list-group list-group-flush" style="height: 30%;">
            <li class="list-group-item">
                <h6> Дата: {{ event.datetime }}</h6>
            </li>
            <li class="list-group-item">
                <h6> Тип мероприятия:</h6>
                <span v-for="event_type in type" :key="event_type.id" >
                    {{ event_type.title }}
                </span>
            </li>
            <li class="list-group-item">
                <h6> Место проведения:</h6>
                <span v-for="event_location in location" :key="event_location.id" >
                    {{ event_location.title }}
                </span>
            </li>
        </ul>
        <div class="card-body" style="height: 10%;">
            <a id="clickable" @click="goEvent(event.id)" class="btn text-light" style="background-color: #2A9D8F; width:100%;">Перейти на страницу мероприятия</a>
        </div>
    </div>
</template>

<script>

import axios from "axios";
export default {
  props: {
    event: Object,
  },

  data(){
    return {
        location: Object,
        type: Object,
    }
  },

  methods: {
    goEvent(event_id) {
      localStorage.setItem("event", event_id);
      this.$router.replace({ path: "/event" });
    },
    },
    mounted() {
        axios
          .get(`http://127.0.0.1:7777/event/type/${this.event.event_type}`, {
              headers: {
                  Authorization: `Token ` + localStorage.getItem("token"),
              },
          })
          .then((res) => {
              this.type = res.data;
          })
          .catch(() => null);
        axios
          .get(`http://127.0.0.1:7777/event/location/${this.event.location}`, {
              headers: {
                  Authorization: `Token ` + localStorage.getItem("token"),
              },
          })
          .then((res) => {
              this.location = res.data;
          })
          .catch(() => null);
    },
};
</script>

<style>

</style>
```

UserComp.vue - компонент страницы пользователя
```
<template>
  <div class="my-3">
    <div class="mb-3 text-center">
    <img src="avatar.jpg" id="av" />
    <p class="m-3 fs-1">{{ user.username }}</p>
  </div>
    <div class="container-md">
      <span v-if="count() === 0">
        Вы не зарегистрированы ни на одно мероприятие
      </span>
      <span v-else>
        <div
          class="accordion accordion-flush border"
          id="accordionFlushExample"
        >
          <span v-for="event in user_regs" :key="event.id">
            <div class="accordion-item">
              <h2 class="accordion-header" id="flush-headingOne">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#flush-collapseOne"
                  aria-expanded="false"
                  aria-controls="flush-collapseOne"
                >
                  <h5>Мероприятие # {{ event.id }}</h5>
                </button>
              </h2>
              <div
                id="flush-collapseOne"
                class="accordion-collapse collapse"
                aria-labelledby="flush-headingOne"
                data-bs-parent="#accordionFlushExample"
              >
                <div class="accordion-body">
                  <div class="card mb-3" style="width: 100%">
                    <div class="row g-0">
                      <div class="col-md-4">
                        <img
                          src="eventcard.jpg"
                          class="img-fluid rounded-start"
                          alt="..."
                        />
                      </div>
                      <div class="col-md-8">
                        <div class="card-body">
                          <h5 class="card-title">{{ event.title }}</h5>
                          <p class="card-text">{{ event.description }}</p>
                        </div>
                        <ul class="list-group list-group-flush">
                          <li class="list-group-item">
                            <h6>Дата: {{ event.datetime }}</h6>
                          </li>
                          <li class="list-group-item">
                            <h6>Тип мероприятия:</h6>
                            <span
                              v-for="theevent_type in event_types"
                              :key="theevent_type.id"
                            >
                              <span
                                v-if="theevent_type.id === event.event_type"
                              >
                                {{ theevent_type.title }}
                              </span>
                            </span>
                          </li>
                          <li class="list-group-item">
                            <h6>Место проведения:</h6>
                            Театр
                          </li>
                        </ul>
                        <div class="card-body justify-content-end">
                          <button
                            @click="goEvent(event.id)"
                            class="btn text-light"
                            style="background-color: #2a9d8f; width: 100%"
                            >Перейти на страницу мероприятия</button
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </span>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: [],
      user_regs: [],
      event_types: [],
      event_locations: [],
    };
  },
  mounted() {
    const token = localStorage.getItem("token");
    if (!token) {
      console.log("No user logged");
      return;
    }
    axios
      .get("http://127.0.0.1:7777/auth/users/me", {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.user = resp.data;
        axios.get(`http://127.0.0.1:7777/user/${resp.data.id}/events`, {
          headers: {
            accept: "application/json",
            Authorization: `Token ${token}`,
          },
        }).then((r) => this.user_regs = r.data);
      });

    // this.user_regs = await axios
    //   .get(`http://127.0.0.1:7777/user/${this.user.id}`, {
    //     headers: {
    //       accept: "application/json",
    //       Authorization: `Token ${token}`,
    //     },
    //   })
    //   .then((resp) => {
    //     this.user_regs = resp.data;
    //   });

    axios
      .get("http://127.0.0.1:7777/event/type", {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.event_types = resp.data;
      });

    axios
      .get(`http://127.0.0.1:7777/event/location`, {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.event_locations = resp.data;
      });
  },

  methods: {
    goEvent(event_id) {
      localStorage.setItem("event", event_id);
      this.$router.replace({ path: "/event" });
    },
    goLogin() {
      localStorage.clear();
      this.$router.replace({ path: "/login" });
    },
    count() {
      return this.user_regs.length;
    },
  },
};
</script>

<style>
#av {
  width: 15%;
  height: 15%;
  border-radius: 25px;
}
</style>
```

Navbar.vue - компонент навигационной панели
```
<template>
  <span>
  <nav class="navbar sticky-top mb-3" style="background-color: #13242A;">
    <div class="container-fluid">
      <a class="navbar-brand d-inline-block" id="clickable" @click="goEvents">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="white" class="bi bi-calendar-check d-inline-block align-text-bottom" viewBox="0 0 16 16">
                    <path d="M10.854 7.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 9.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                    <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                </svg>
                <h2 class="d-inline-block text-light mx-2"> Мерофонд</h2>
            </a>
        <span v-if="isToken">
            <li class="d-inline-block">
              <div class="d-grid gap-4 d-md-flex justify-content-end align-top">
                <button type="button" @click="goUser" class="btn text-light" style="background-color:#2A9D8F">
                   Личный кабинет
                </button>
            <button type="button" @click="goLogin" class="btn text-light" style="background-color:#E24D28">
                Выйти
            </button>
            </div>
            </li>
        </span>
    </div>
  </nav>
</span>
</template>

<script>

export default {
    props: {
      page: "",
    },
    data() {
        return {
            isToken: null,
        }
    },
    mounted() {
        const token = localStorage.getItem("token");
        if (!token) {
            this.isToken = 0;
        }
        else {
            this.isToken = 1;
        }
    },
  methods: {
    goUser() {
      this.$router.replace({ path: "/user" });
    },
    goEvents() {
      this.$router.replace({ path: "/events" });
    },
    goLogin() {
      localStorage.clear();
      this.$router.replace({ path: "/login" });
    },
  },
};
</script>

<style>
#clickable {
  cursor: pointer;
}
</style>
```

### Views
User.vue - личный кабинет
```
<template>
  <span>
    <Navbar />
    <user-comp />
</span>
</template>

<script>

import Navbar from "../components/Navbar.vue";
import UserComp from '../components/UserComp.vue';

export default {
  components: { Navbar, UserComp },
}

</script>
```

Login.vue - страница авторизации
```
<template>
  <span>
    <Navbar></Navbar>
    <div class="container-fluid">
      <br />
      <div class="row d-flex justify-content-center">
        <div class="col-xs-2 col-md-6 col-sm-6 col-lg-4 align-self-center">
          <div class="p-3 border bg-white text-center">
            <p class="fs-2">Вход</p>
          </div>
          <div class="p-3 border bg-white">
            <LoginComp />
          </div>
        </div>
      </div>
    </div>
  </span>
</template>
  
  <script>
  import LoginComp from "../components/LoginComp.vue";
  import Navbar from "../components/Navbar.vue";
  
  export default {
    components: { LoginComp, Navbar },
  };
  </script>
  
  <style scoped>
  /* .col-custom {
    min-width: inherit;
  } */
  </style>
```

SignUpView.vue - страница регистрации
```
<template>
    <span>
      <Navbar></Navbar>
      <div class="container-fluid">
        <br />
        <div class="row d-flex justify-content-center">
          <div class="col-xs-2 col-md-6 col-sm-6 col-lg-4 align-self-center">
            <div class="p-3 border bg-white text-center">
              <p class="fs-2">Регистрация</p>
            </div>
            <div class="p-3 border bg-white">
              <SignUpComp />
            </div>
          </div>
        </div>
      </div>
    </span>
  </template>
    
    <script>
    import SignUpComp from "../components/SignUpComp.vue";
    import Navbar from "../components/Navbar.vue";
    
    export default {
      components: { SignUpComp, Navbar },
    };
    </script>
    
    <style scoped>
    /* .col-custom {
      min-width: inherit;
    } */
    </style>
```

EventListView.vue - страница с карточками мероприятий
```
<template>
    <span><Navbar />
    <div class="m-3 text-center">
      <h1>Календарь мероприятий</h1>
    </div>
    <div class="container my-5">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-3">
          <span v-for="event in events" :key="event.id">
            <div class="col">
              <event-card :event="event" />
            </div>
        </span>
        </div>
    </div>
  </span>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import EventCard from "../components/EventCard.vue";
import axios from "axios";

export default {
  components: { Navbar, EventCard },
  data() {
    return {
      events: [],
      location: []
    };
  },
  // methods: {
  //   },
    mounted() {
      axios
          .get("http://127.0.0.1:7777/event/list", {
              headers: {
                  Authorization: `Token ` + localStorage.getItem("token"),
              },
          })
          .then((res) => {
              this.events = res.data;
          })
          .catch(() => null);
      },
};
</script>
```

EventView.vue - страница мероприятия
```
<template>
    <span>
        <navbar />
        <div class="container-fluid">
            <span v-for="theevent in event" :key="theevent.id">
        <div class="my-3 text-center">
            <img src="eventcard.jpg" style="width: 20%; height: 20%;" />
            
            <p class="m-3 fs-1">{{ theevent.title }}</p>
        </div>
        <div class="container-md my-3">
            <p class="m-3 fs-2">Описание</p>
            <p class="fs-4">{{ theevent.description }}</p>
            <p class="m-3 fs-2">Дата: {{ theevent.datetime }}</p>
            <p class="m-3 fs-2">Тип мероприятия:</p>
            <p class="fs-4">{{ theevent.event_type }}</p>
            <p class="m-3 fs-2">Место проведения:</p>
            <p class="fs-4">{{ theevent.location }}</p>
        </div>
    </span>
    <div class="text-center">
    <button @click="goRegEvent" class="btn text-light" style="background-color: #2A9D8F; width:50%;">Зарегистрироваться на мероприятие</button>
</div>
  </div>

    </span>
</template>

<script>
import axios from "axios";
import Navbar from '../components/Navbar.vue';


export default {
  components: { Navbar },
  data() {
    return {
      user: {},
      event: {},
    //   event_id_: null,
    };
  },
  mounted() {
    const token = localStorage.getItem("token");
    const event_id = localStorage.getItem("event");
    if (!token) {
      console.log("No user logged");
      return;
    }
    if (event_id) {
    axios
      .get(`http://127.0.0.1:7777/event/${event_id}`, {
        headers: {
          accept: "application/json",
        //   Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.event = resp.data;
      });

    }
    axios
      .get("http://127.0.0.1:7777/auth/users/me", {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.user = resp.data;
      });
  },

  methods: {
    goRegEvent() {
    //   localStorage.removeItem("event");
      this.axios
      .post("http://127.0.0.1:7777/event/reg", {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },

        user: this.user,
        event: this.event,
      })
      .then(() => {
        this.$router.replace({ path: "/event" });
      });
    },

  },
};
</script>

<style>
#av {
  width: 15%;
  height: 15%;
  border-radius: 25px;
}
</style>
```