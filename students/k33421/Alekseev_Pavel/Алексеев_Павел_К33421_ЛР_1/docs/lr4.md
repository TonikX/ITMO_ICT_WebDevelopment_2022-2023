# Описание 4 лабораторной работы






- `App.vue`

```HTML
<template>
  <v-app>
    <div>
      <v-toolbar dense
                 dark
                 color="blue"
      >

        <v-toolbar-title @click="goToHome" style="cursor: pointer">Hotel by Paul Alekseev</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn color="white" plain @click="goToRooms">
            Rooms
          </v-btn>
          <v-btn color="white" plain @click="goToGuests">
            Guests
          </v-btn>
          <v-btn color="white" plain @click="goToRegistration">
            Register
          </v-btn>
        </v-toolbar-items>
        <v-btn color="white" plain @click="logout">
          Exit
        </v-btn>
      </v-toolbar>
    </div>
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>

</template>

<script>
export default {
  name: 'App',
  data: () => ({}),
  methods: {
    logout () {
      localStorage.removeItem('auth_token')
      this.$router.push({ name: 'Login' })
    },
    goToGuests () {
      this.$router.push({ name: 'Guests' })
    },
    goToRooms () {
      this.$router.push({ name: 'Rooms' })
    },
    goToRegistration () {
      this.$router.push({ name: 'Registration' })
    },
    goToHome () {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>


```

- `index.js`

```python
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login'
import Registration from '@/views/Registration'
import Guests from '@/views/Guests'
import Rooms from '@/views/Rooms'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    alias: '/home',
    meta: { requiresAuth: true }
  },
  {
    path: '/guests',
    name: 'Guests',
    component: Guests,
    meta: { requiresAuth: true }
  },
  {
    path: '/rooms',
    name: 'Rooms',
    component: Rooms,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Registration',
    component: Registration
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!localStorage.getItem('auth_token')) {
      next({
        name: 'Login'
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router


###


class AllBook(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateBook(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Booking.objects.all()


class DeleteBook(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Booking.objects.all()

###


class AllBookWithInfo(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializerWithInfoAboutRoomAndTypeRoom


class RoomCount(generics.ListAPIView):
    serializer_class = RoomCountSerializer

    def get_queryset(self):
        c = Room.objects.annotate(num_rooms=Count('id_room')).count()
        return [{'count': c}]


class ClientCount(generics.ListAPIView):
    serializer_class = ClientCountSerializer

    def get_queryset(self):
        c = Client.objects.annotate(num_clients=Count('passport')).count()
        queryset = [{'count': c}]
        return queryset




```
# Views

- `Home.vue`

```HTML
<template>
  <div class="home">
    <h1>Вы успешно авторизовались!</h1>
    <h2>Спасибо, что вы с нами!</h2>
  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
  }
}
</script>

```

- `Rooms.vue`

```HTML
<template>
  <div>
    <h1>Список <span v-if="filter">свободных</span> комнат</h1>
    <ul class="greeting-list">
      <li
        v-for="room in filteredRooms"
        :key="room.number"
      >
        {{ room.number }} - {{room.type}} beds
      </li>
    </ul>
    <v-btn
      color="blue"
      dark
      @click="dialog = true"
    >
      Edit
    </v-btn>
    <v-btn
      color="blue"
      dark
      v-if="!filter"
      @click="filter = true"
      class="mx-2"
    >
      Show empty rooms
    </v-btn>
    <v-btn
      color="blue"
      dark
      v-if="filter"
      @click="filter = false"
      class="mx-2"
    >
      Show all rooms
    </v-btn>
    <v-row>
      <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
      >
        <v-card>
          <v-card-title>
            <span class="headline">Room info</span>
            <v-spacer></v-spacer>
            <v-btn
              icon
              @click="dialog = false"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    v-model="roomNumber"
                    label="Room number"
                    required
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-select v-model="roomType"
                            :items="['1', '2', '3']"
                            label="Type"
                  ></v-select>
                </v-col>
                <v-col
                  cols="12"
                  sm="6"
                  md="4"
                >
                  <v-text-field
                    label="Price"
                    persistent-hint
                    required
                    v-model="roomPrice"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6"
                       md="4">
                  <v-text-field
                    label="Floor"
                    required
                    v-model="roomFloor"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn icon @click="search">
              <v-icon>mdi-magnify</v-icon>
            </v-btn>
            <v-btn
              color="cancel"
              text
              @click="doDelete"
            >
              Delete
            </v-btn>
            <v-btn
              color="info"
              text
              @click="update"
            >
              Update
            </v-btn>
            <v-btn
              color="success"
              text
              @click="add"
            >
              Add
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Rooms',
  data: () => ({
    rooms: [],
    busyRooms: [],
    filter: false,
    dialog: false,
    roomType: '',
    roomPrice: '',
    roomNumber: '',
    roomFloor: ''
  }),
  methods: {
    search () {
      console.log(this.rooms)
      const room = this.rooms.filter(room => room.number === Number.parseInt(this.roomNumber))[0]
      if (room) {
        this.roomType = room.type
        this.roomPrice = room.price
        this.roomFloor = room.floor
      } else {
        this.roomType = ''
        this.roomPrice = ''
        this.roomFloor = ''
      }
    },
    async add () {
      const body = {
        number: this.roomNumber,
        type: this.roomType,
        price: this.roomPrice,
        floor: this.roomFloor
      }
      const response = await this.axios.post(this.$hostname + 'hotel/rooms/',
        body,
        {
          headers:
            {
              Authorization: 'Token ' + localStorage.getItem('auth_token')
            }
        }
      )
      console.log(response)
      this.dialog = false
      if (response.status === 201) {
        this.rooms.push(body)
      }
    },
    async update () {
      const body = {
        type: this.roomType,
        price: this.roomPrice,
        floor: this.roomFloor
      }
      const response = await this.axios.patch(this.$hostname + 'hotel/rooms/' + this.roomNumber + '/',
        body,
        {
          headers:
            {
              Authorization: 'Token ' + localStorage.getItem('auth_token')
            }
        }
      )
      console.log(response)
      this.rooms = this.rooms.filter(room => room.number !== Number.parseInt(this.roomNumber))
      if (response.status === 200) {
        body.number = this.roomNumber
        this.rooms.push(body)
      }
      this.dialog = false
    },
    doDelete () {
      this.axios.delete(this.$hostname + 'hotel/rooms/' + this.roomNumber + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      this.rooms = this.rooms.filter(room => room.number !== Number.parseInt(this.roomNumber))
      this.dialog = false
    }
  },
  computed: {
    filteredRooms () {
      if (this.filter) {
        return this.rooms.filter(room => !this.busyRooms.includes(room.number))
      }
      return this.rooms
    }
  },
  created () {
    this.axios.get(this.$hostname + 'hotel/rooms/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
      .then(response => {
        this.rooms = response.data
      })
      .catch(error => {
        console.log(error)
      })
    this.axios.get(this.$hostname + 'hotel/guests/', { headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') } })
      .then(response => {
        this.busyRooms = response.data.map(guest => guest.room)
        console.log(this.busyRooms)
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>
</style>


```
- `Registration.vue`

```HTML
<template>
  <v-layout column justify-center align-center>
    <v-form v-model="valid"
    >
      <v-text-field
        v-model="username"
        label="Username"
        :rules="[v => !!v || 'Username is required']"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Password"
        type="Password"
        :rules="[v => !!v || 'Password is required']"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        label="Email"
        type="email"
        :rules="emailRules"
        required
      ></v-text-field>

      <v-btn
        color="blue"
        @click="submit"
        :disabled="!valid"
      >
        Login
      </v-btn>
    </v-form>
  </v-layout>
</template>

<script>
export default {
  name: 'Registration',
  data: () => ({
    username: '',
    password: '',
    email: '',
    emailRules: [
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
    ]
  }),
  methods: {
    async submit () {
      const body = {
        valid: false,
        username: this.username,
        password: this.password,
        email: this.email
      }
      const response = await this.axios.post(this.$hostname + 'auth/users/', body)
      if (response.status === 201) {
        this.$router.push({ name: 'Login' })
      } else {
        alert('Something went wrong')
      }
    }
  }
}
</script>

<style scoped>
</style>

```

- `Login.vue`

```HTML
<template>
  <v-layout column justify-center align-center>
    <v-form
    >
      <v-text-field
        v-model="username"
        label="Username"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Password"
        type="Password"
        required
      ></v-text-field>

      <v-btn
        color="success"
        @click="submit"
      >
        Login
      </v-btn>
    </v-form>
  </v-layout>
</template>

<script>
export default {
  name: 'Login',
  data: () => ({
    username: '',
    password: ''
  }),
  methods: {
    async submit () {
      const body = {
        username: this.username,
        password: this.password
      }
      const response = await this.axios.post(this.$hostname + 'auth/token/login/', body)
      if (response.status === 200) {
        localStorage.setItem('auth_token', response.data.auth_token)
        this.$router.push({ name: 'Home' })
      } else {
        if (response.status === 400) {
          alert('Wrong username or password')
        } else {
          alert('Unknown error')
        }
      }
    }
  }
}
</script>

<style scoped>
</style>


```

- `Страница входа`
![Вход](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/first.png)

- `Регистрация`
![Рега](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/reg.png)

- `Комнаты`
![Комнаты](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/room.png)

- `Свободные комнаты`
![Свободные комнаты](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/free rooms.png)

- `Домашняя страница`
![Домашняя страница](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/home.png)

- `Гости`
![Гости](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/guests.png)

- `Редактирование комнаты`
![Редактирование комнаты](/Users/pavelalekseev/Desktop/ITMO_ICT_WebDevelopment_2022-2023/Алексеев_Павел_К33421_ЛР_1/site/assets/images/edit room.png)



