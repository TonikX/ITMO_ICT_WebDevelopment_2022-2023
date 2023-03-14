# Лабораторная №4

## Picterest
Альтернатива популярного сайта Pinterest, где пользователи могут просматривать различные фотографии и сохранять их
![](img/LR4/Снимок экрана 2023-03-14 в 23.12.59.png)

### Views
#### DashboardView.vue
```
<template>
  <div class="container-fluid">
    <NavbarWithFilters></NavbarWithFilters>

    <section class="photos mt-4">
      <div class="pinterest-grid">
        <router-link
          v-for="photo in photos"
          :key="photo.id"
          :to="'/post/' + photo.id">
          <img
            class="main-image"
            alt="dashboard-photo-1"
            :src="photo.urls.small"
          />
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
import NavbarWithFilters from '@/components/NavbarWithFilters'

export default {
  name: 'DashboardView',

  components: {
    NavbarWithFilters
  },

  beforeMount () {
    this.loadPhotos()
  },

  computed: {
    photos () {
      return this.$store.getters.photos
    }
  },

  methods: {
    loadPhotos () {
      this.$store.dispatch('getPhotos')
    }
  },

  head: {
    title: 'Picterest- Home'
  }
}
</script>
```

#### PostView.vue
```
<template>
  <div class="container-fluid">
    <NavbarMinimal></NavbarMinimal>
    <div class="container">
      <section class="d-flex post-wrap mt-3">
        <img class="w-50 post-image" :src="photo ? photo.urls.regular : ''" />
        <div class="w-50 p-4 post-wrap">
          <div class="d-flex align-items-center justify-content-between">
            <h5 class="mb-1">{{ photo ? photo.user.name : '' }}</h5>
            <button @click="like" class="btn btn-primary btn-sm">Like</button>
          </div>
          <div>{{ date }}</div>
          <div class="mb-3">{{ photo ? photo.location.name : '' }}</div>
          <div>{{ photo ? photo.description : '' }}</div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import NavbarMinimal from '@/components/NavbarMinimal'
import axios from 'axios'

export default {
  name: 'PostView',

  components: {
    NavbarMinimal
  },

  beforeMount () {
    this.$store.dispatch('loadPhoto', this.$route.params.id)
  },

  computed: {
    photo () {
      return this.$store.getters.postPhoto
    },

    date () {
      const photo = this.photo

      return new Date(photo.created_at).toDateString()
    }
  },

  methods: {
    async like () {
      try {
        const userId = JSON.parse(localStorage.getItem('user')).id

        const response = await axios.post(
          'http://localhost:3000/600/likedPhotos',
          {
            photo: this.photo.id,
            url: this.photo.urls.small,
            userId
          },
          {
            headers: {
              Authorization: 'Bearer ' + localStorage.accessToken
            }
          }
        )

        if (response.status === 201) {
          console.log('liked')
        }
      } catch (e) {
        alert(e.response.data)
      }
    }
  }
}
</script>

<style scoped></style>
```

#### LoginView.view
```
<template>
  <div class="container">
    <div class="row justify-content-center mt-5 p-5">
      <div class="col-12">
        <div class="login-wrap d-flex">
          <div
            class="login-img w-50"
          ></div>

          <div class="w-50 p-5">
            <h3 class="mb-4">Sign In</h3>

              <div class="form-group mb-3">
                <label class="label" for="name">Email</label>
                <input
                  id="name"
                  type="text"
                  class="form-control"
                  placeholder="Email"
                  v-model="form.email"
                  required
                />
              </div>
              <div class="form-group mb-3">
                <label class="label" for="password">Password</label>
                <input
                  id="password"
                  type="password"
                  class="form-control"
                  placeholder="Password"
                  v-model="form.password"
                  required
                />
              </div>
              <div class="form-group">
                <button
                  @click="login()"
                  class="form-control btn btn-primary submit px-3"
                >
                  Sign In
                </button>
              </div>
              <div class="form-group d-flex">
                <div class="w-50">
                  <label class="checkbox-wrap checkbox-primary mb-0">Remember Me
                    <input type="checkbox" checked="" />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="w-50 text-right">
                  <a href="#">Forgot Password</a>
                </div>
              </div>

            <p class="text-center">
              Not a member? <router-link to="/signup">Sign Up</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',

  data () {
    return {
      form: {
        email: null,
        password: null
      }
    }
  },

  beforeMount () {
    if (localStorage.getItem('accessToken')) {
      this.$router.push('/')
    }
  },

  methods: {
    async login () {
      try {
        const response = await axios.post('http://localhost:3000/login', this.form)

        if (response.status === 200) {
          localStorage.setItem('accessToken', response.data.accessToken)
          localStorage.setItem('user', JSON.stringify(response.data.user))
          this.$router.push('/')
        }
      } catch (e) {
        alert(e.response.data)
      }
    }
  }
}
</script>

<style scoped>
.text-right  {
  text-align: right;
}

.login-img {
  background-image: url("@/assets/img/logo-photo.jpeg");
}
</style>
```

#### SignUpView.vue
```
<template>
  <div class="container">
    <div class="row justify-content-center mt-5 p-5">
      <div class="col-12">
        <div class="login-wrap d-flex">
          <div class="w-100 p-5">
            <div class="d-flex">
              <div class="w-100">
                <h3 class="mb-4">Sign Up</h3>
              </div>
            </div>

            <div class="form-group mb-3">
              <label class="label" for="email">Email</label>
              <input
                id="email"
                type="text"
                class="form-control"
                placeholder="Username"
                v-model="form.email"
                required
              />
            </div>
            <div class="form-group mb-3">
              <label class="label" for="name">Username</label>
              <input
                id="name"
                type="text"
                class="form-control"
                placeholder="Username"
                v-model="form.username"
                required
              />
            </div>
            <div class="form-group mb-3">
              <label class="label" for="password">Password</label>
              <input
                id="password"
                type="password"
                class="form-control"
                placeholder="Password"
                v-model="form.password"
                required
              />
            </div>
            <div class="form-group mb-3">
              <label class="label" for="password-confirm">
                Confirm Password
              </label>
              <input
                v-model="form.password2"
                id="password-confirm"
                type="password"
                class="form-control"
                placeholder="Password"
                required
              />
            </div>

            <div class="form-group">
              <button
                @click="signup()"
                class="form-control btn btn-primary submit px-3 mt-3"
              >
                Sign Up
              </button>
            </div>

            <p class="text-center mt-2">
              Already Singed up?
              <router-link to="/login" data-toggle="tab"> Sign In </router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpView',

  data () {
    return {
      form: {
        username: null,
        password: null,
        password2: null,
        email: null
      }
    }
  },

  beforeCreate () {
    if (localStorage.getItem('accessToken')) {
      this.$router.push('/')
    }
  },

  methods: {
    async signup () {
      if (this.form.password === this.form.password2 && this.form.password !== null) {
        try {
          const response = await axios.post(
            'http://localhost:3000/signup',
            {
              email: this.form.email,
              password: this.form.password,
              username: this.form.username
            })

          if (response.status === 201) {
            this.$router.push('/login')
          }
        } catch (e) {
          alert(e.response.data)
        }
      } else {
        alert('Пароли не совпадают')
      }
    }
  }
}
</script>

<style scoped></style>
```

#### ProfileView.vue
```
<template>
  <div class="container-fluid">
    <NavbarMinimal></NavbarMinimal>
    <div class="container">
      <div class="row">
        <div class="col-6">
          <section class="settings mt-4">
            <h4 class="mb-4">Profile</h4>
            <div class="form-group row mb-3">
              <div class="col-6">
                <label class="label" for="first-name">First Name</label>
                <input id="first-name" type="text" class="form-control" placeholder="First Name" required>
              </div>
              <div class="col-6">
                <label class="label" for="last-name">Last Name</label>
                <input id="last-name" type="text" class="form-control" placeholder="Last Name" required>
              </div>
            </div>
            <div class="form-group mb-3">
              <label class="label" for="name">Username</label>
              <input id="name" type="text" class="form-control" placeholder="Username" required>
            </div>
            <div class="form-group mb-3">
              <label class="label" for="email">Email</label>
              <input id="email" type="text" class="form-control" placeholder="Email" required="">
            </div>
            <div class="form-group mb-3">
              <label class="label" for="description">Bio</label>
              <textarea id="description" type="text" class="form-control" placeholder="Enter a Bio"></textarea>
            </div>
            <div class="form-group d-flex justify-content-end">
              <button type="submit" class="btn btn-secondary px-3 mx-2">Cancel</button>
              <button type="submit" class="btn btn-primary px-3">Save</button>
            </div>
          </section>
        </div>
        <div class="col-6">
          <h4 class="mt-4">Liked pictures</h4>
          <div class="pinterest-grid-profile">
            <img v-for="photo in likedPhotos" :key="photo.photo" class="main-image" :src="photo.url"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarMinimal from '@/components/NavbarMinimal'

export default {
  name: 'ProfileView',

  computed: {
    likedPhotos () {
      return this.$store.getters.likedPhotos
    }
  },

  beforeMount () {
    if (!localStorage.getItem('accessToken')) {
      this.$router.push('/login')
    }

    this.$store.dispatch('getLikedPhotos', { accessToken: localStorage.accessToken, userId: JSON.parse(localStorage.user).id })
  },

  components: {
    NavbarMinimal
  }
}
</script>

<style scoped></style>
```

### Components

#### NavbarMinimal.vue
```
<template>
  <div class="container-fluid my-navbar sticky-top">
    <nav class="navbar navbar-light">
      <router-link to="/" class="navbar-brand">
        <img
          src="@/assets/logo.png"
          width="30"
          height="30"
          class="d-inline-block align-top"
          alt=""
        />
        Picterest
      </router-link>
      <ProfileBlock></ProfileBlock>
    </nav>
  </div>
</template>

<script>
import ProfileBlock from '@/components/ProfileBlock'

export default {
  name: 'TheNavbarMinimal',

  components: {
    ProfileBlock
  }
}
</script>

<style scoped></style>
```

#### NavbarWithFilters.vue
```
<template>
  <div class="container-fluid my-navbar sticky-top">
    <nav class="navbar navbar-light">
      <router-link to="/" class="navbar-brand">
        <img
          src="@/assets/logo.png"
          width="30"
          height="30"
          class="d-inline-block align-top"
          alt=""
        />
        Picterest
      </router-link>
      <ProfileBlock></ProfileBlock>
    </nav>
  </div>
</template>

<script>
import ProfileBlock from '@/components/ProfileBlock'

export default {
  name: 'TheNavbarMinimal',

  components: {
    ProfileBlock
  }
}
</script>

<style scoped></style>

```

#### ProfileBlock.vue
```
<template>
  <div class="d-flex align-items-center">
    <router-link to="/profile" class="mx-2">
      <img src="@/assets/img/avatar.png" alt="profile" width="30" height="30"/>
    </router-link>
    <svg v-if="isLoggedIn" @click="logout" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="black" class="bi bi-box-arrow-right ml-3" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
      <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'ProfileBlock',

  data () {
    return {
      isLoggedIn: false
    }
  },

  mounted () {
    if (localStorage.getItem('accessToken')) {
      this.isLoggedIn = true
    }
  },

  methods: {
    logout () {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('user')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>

</style>
```

### Store

#### index.js
```
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const accessKey = '4WtZzqzkj1jpOdx3igqSGJuGBWg2gheh_QvIARzn40M'

export default new Vuex.Store({
  state: {
    photos: null,
    postPhoto: null,
    likedPhotos: null
  },

  getters: {
    photos (state) {
      return state.photos
    },

    postPhoto (state) {
      return state.postPhoto
    },

    likedPhotos (state) {
      return state.likedPhotos
    }
  },

  mutations: {
    setPhotos (state, payload) {
      state.photos = payload
    },

    setPostPhoto (state, payload) {
      state.postPhoto = payload
    },

    setLikedPhotos (state, payload) {
      state.likedPhotos = payload
    }
  },

  actions: {
    async searchPhotos (context, { query, filters }) {
      if (query == null) {
        return
      }

      if (filters.color === null) {
        delete filters.color
      }

      try {
        const response = await axios.get('https://api.unsplash.com/search/photos', {
          params: {
            client_id: accessKey,
            per_page: 20,
            query,
            ...filters
          }
        })

        if (response.status === 200) {
          context.commit('setPhotos', response.data.results)
        }
      } catch (e) {
        console.log(e)
      }
    },

    async getPhotos (context) {
      try {
        const response = await axios.get('https://api.unsplash.com/photos', {
          params: {
            client_id: accessKey,
            order_by: 'popular',
            per_page: 20
          }
        })

        if (response.status === 200) {
          context.commit('setPhotos', response.data)
        }
      } catch (e) {
        console.log(e)
      }
    },

    async loadPhoto (context, id) {
      try {
        const response = await axios.get('https://api.unsplash.com/photos/' + id, {
          params: {
            client_id: accessKey
          }
        })

        if (response.status === 200) {
          context.commit('setPostPhoto', response.data)
        }
      } catch (e) {
        console.log(e)
      }
    },

    async getLikedPhotos (context, { accessToken, userId }) {
      try {
        const response = await axios.get('http://localhost:3000/600/likedPhotos?userId=' + userId, {
          headers: {
            Authorization: 'Bearer ' + accessToken
          }
        })

        if (response.status === 200) {
          context.commit('setLikedPhotos', response.data)
        }
      } catch (e) {
        console.log(e)
      }
    }
  }
})
```

### Router

#### index.js
```
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: DashboardView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/post/:id',
    name: 'Post',
    component: PostView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```