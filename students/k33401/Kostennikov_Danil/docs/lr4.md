# Lab 3

Реализация клиентской части приложения средствами vue.js.

# API

### Авторизация

```javascript
class UserApi {
  constructor(instance) {
    this.API = instance;
  }

  register = async (data) => {
    return this.API({
      method: "POST",
      url: "/auth/users/",
      data,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  login = async (data) => {
    return this.API({
      method: "POST",
      url: "/auth/token/login/",
      data,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  logout = async (token) => {
    return this.API({
      method: "POST",
      url: "/auth/token/logout/",
      headers: {
        Authorization: `Token ${token}`,
      },
    });
  };
}

export default UserApi;
```

### Количество свободных комнат

```javascript
class RoomsApi {
  constructor(instance) {
    this.API = instance;
  }

  freeRooms = async (date) => {
    return this.API({
      url: `/free_rooms/${date}`,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };
}

export default RoomsApi;
```

### Количество клиентов из заданного города

```javascript
class ClientApi {
  constructor(instance) {
    this.API = instance;
  }

  clientCityCount = async (data) => {
    return this.API({
      url: `/client/${data}`,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };
}

export default ClientApi;
```

# Stores

### user store

```javascript
import { defineStore } from "pinia";
import { userApi } from "@/api";

const usersStore = defineStore("users", {
  state: () => ({
    user: null,
    token: null,
  }),

  actions: {
    async register(user) {
      console.log("in store", user);
      const response = await userApi.register(user);
      console.log("in store response", response);
      return response.data;
    },

    async login(credentials) {
      const response = await userApi.login(credentials);
      this.user = {
        username: credentials.username,
        password: credentials.password,
      };
      this.token = response.data.auth_token;
      return response;
    },

    async logout() {
      if (this.token) {
        this.token = null;
        this.user = null;
        this.$router.push("Navbar");
        return true;
      }
    },
  },
});

export default usersStore;
```

### rooms store

```javascript
import { defineStore } from "pinia";
// импортируем API
import { roomsApi } from "@/api";

const userRoomsStore = defineStore("rooms", {
  state: () => ({
    date: "",
    rooms: "",
  }),

  actions: {
    async loadFreeRooms(date) {
      const response = await roomsApi.freeRooms(date);
      this.date = date;
      this.rooms = JSON.stringify(response.data.count);
      return response;
    },
  },
});

export default userRoomsStore;
```

### client store

```javascript
import { defineStore } from "pinia";
// импортируем API
import { clientApi } from "@/api";

const clientStore = defineStore("rooms", {
  state: () => ({
    city: "",
    count: "",
  }),

  actions: {
    async loadClientCityCount(data) {
      const response = await clientApi.clientCityCount(data);
      this.city = data;
      this.count = JSON.stringify(response.data.count);
      return response;
    },
  },
});

export default clientStore;
```

# Components

### Navbar

```vue
<template>
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
      <a class="navbar-brand">Hotel app</a>
      <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
          <li v-if="user" class="nav-item">
            <router-link class="nav-link active" to="/freeRooms"
              ><a>Free rooms</a></router-link
            >
          </li>
          <li v-if="user" class="nav-item">
            <router-link class="nav-link active" to="/clientCity"
              ><a>Client city count</a></router-link
            >
          </li>
        </ul>
      </div>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li v-if="!user" class="nav-item auth_link">
            <router-link class="nav-link active" to="/login">
              <a class="nav-link">Login</a></router-link
            >
          </li>
          <li v-if="!user" class="nav-item auth_link">
            <router-link class="nav-link active" to="/register">
              <a class="nav-link">Register</a></router-link
            >
          </li>
          <li v-if="user" class="nav-item profile_link">
            <router-link class="nav-link active" to="/navbar">
              <a class="nav-link" @click="logout" href="#">LogOut</a>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";

export default {
  name: "Navbar",
  computed: {
    ...mapState(usersStore, ["user", "token"]),
  },

  methods: {
    ...mapActions(usersStore, ["logout", "login"]),
  },
};
</script>
```

### Login

```vue
<template>
  <form ref="registerForm" @submit.prevent="loginForm">
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />
    </div>
    <div>
      <button type="submit" class="btn btn-primary">Login</button>
    </div>
  </form>
</template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(usersStore, ["login"]),
    async loginForm() {
      try {
        const response = await this.login({
          username: this.username,
          password: this.password,
        });
        this.$refs.registerForm.reset();
        this.$router.push("Navbar");
      } catch (error) {
        alert("wrong username or password");
      }
    },
  },
};
</script>
```

### Register

```vue
<template>
  <form ref="registerForm" @submit.prevent="registerForm">
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />
    </div>
    <div>
      <label for="email">Email:</label>
      <input type="text" id="email" v-model="email" required />
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />
    </div>
    <div>
      <button type="submit" class="btn btn-primary">Register</button>
    </div>
  </form>
</template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";
export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      email: "",
    };
  },
  methods: {
    ...mapActions(usersStore, ["register", "login"]),
    async registerForm() {
      try {
        const response = await this.register({
          username: this.username,
          email: this.email,
          password: this.password,
        });
        this.$refs.registerForm.reset();

        await this.login({
          username: this.username,
          password: this.password,
        });
        this.$router.push("Navbar");
      } catch (error) {
        alert("something went wrong");
      }
    },
  },
};
</script>
```

### ClientCity

```vue
<template>
  <div class="free-rooms-count">
    <h5 class="free-rooms-title">For the city of {{ city }}</h5>
    <h5 class="free-rooms-count">Amount of clients: {{ count }}</h5>
  </div>
</template>

<script>
export default {
  name: "ClientCity",
  props: {
    city: {
      type: String,
      required: true,
    },
    count: {
      type: String,
      required: true,
    },
  },
};
</script>
```

### FreeRooms

```vue
<template>
  <div class="free-rooms-count">
    <h5 class="free-rooms-title">For the date {{ date }}</h5>
    <h5 class="free-rooms-count">Amount of free rooms: {{ text }}</h5>
  </div>
</template>

<script>
export default {
  name: "FreeRooms",
  props: {
    text: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },
};
</script>
```

# Views

### ClientCityPage

```vue
<template>
  <HeaderComponent> </HeaderComponent>
  <a></a>
  <h1>Amount of client from current city</h1>

  <form
    ref="noteForm"
    @submit.prevent="createCard"
    class="d-flex flex-column my-5"
  >
    <input type="text" v-model="form.cityForm" class="my-1" />

    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>

  <div class="row row-cols-1 row-cols-md-2 g-4 mt-5" id="notes">
    <div>
      <client-city :city="this.city" :count="this.count" />
    </div>
  </div>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import ClientCity from "@/components/ClientCity.vue";
import HeaderComponent from "@/components/Navbar.vue";
import { mapActions, mapState } from "pinia";

import clientStore from "@/stores/client";

export default {
  name: "ClientCityPage",

  components: { BaseLayout, ClientCity, HeaderComponent },

  computed: {
    ...mapState(clientStore, ["city", "count"]),
  },

  methods: {
    ...mapActions(clientStore, ["loadClientCityCount"]),

    async createCard() {
      console.log(this.form);
      console.log(this.form.cityForm);
      console.log(this.form.cityForm);
      await this.loadClientCityCount(this.form.cityForm);

      this.$refs.noteForm.reset();
      console.log(this.city);
      console.log(this.count);
    },
  },

  data() {
    return {
      form: {
        cityForm: "",
      },
    };
  },

  mounted() {
    if (localStorage.getItem("reloaded")) {
      // The page was just reloaded. Clear the value from local storage
      // so that it will reload the next time this page is visited.
      localStorage.removeItem("reloaded");
    } else {
      // Set a flag so that we know not to reload the page twice.
      localStorage.setItem("reloaded", "1");
      location.reload();
    }
  },
};
</script>
```

### FreeRoomsPage

```vue
<template>
  <HeaderComponent> </HeaderComponent>
  <a></a>
  <h1>Amount of free rooms on current date</h1>

  <form
    ref="noteForm"
    @submit.prevent="createCard"
    class="d-flex flex-column my-5"
  >
    <input type="text" v-model="form.date" class="my-1" />

    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>

  <div class="row row-cols-1 row-cols-md-2 g-4 mt-5" id="notes">
    <div>
      <free-rooms :date="date" :text="rooms" />
    </div>
  </div>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import FreeRooms from "@/components/FreeRooms.vue";
import HeaderComponent from "@/components/Navbar.vue";
import { mapActions, mapState } from "pinia";

import userRoomsStore from "@/stores/rooms";

export default {
  name: "FreeRoomsPage",

  components: { BaseLayout, FreeRooms, HeaderComponent },

  computed: {
    ...mapState(userRoomsStore, ["rooms", "date"]),
  },

  methods: {
    ...mapActions(userRoomsStore, ["loadFreeRooms"]),

    async createCard() {
      console.log(this.form);
      console.log(this.form.date);
      await this.loadFreeRooms(this.form.date);

      this.$refs.noteForm.reset();
      console.log(this.rooms);
    },
  },

  data() {
    return {
      form: {
        date: "",
      },
    };
  },

  mounted() {
    if (localStorage.getItem("reloaded")) {
      // The page was just reloaded. Clear the value from local storage
      // so that it will reload the next time this page is visited.
      localStorage.removeItem("reloaded");
    } else {
      // Set a flag so that we know not to reload the page twice.
      localStorage.setItem("reloaded", "1");
      location.reload();
    }
  },
};
</script>
```

# Router

```javascript
import FreeRoomsPage from "@/views/FreeRoomsPage.vue";
import clientCityPage from "@/views/clientCityPage.vue";
import RegisterComponent from "@/components/Register.vue";
import LoginComponent from "@/components/Login.vue";
import Navbar from "@/components/Navbar.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  // массив с роутами
  // отдельный роут:
  { path: "/freeRooms", component: FreeRoomsPage },
  { path: "/register", component: RegisterComponent },
  { path: "/login", component: LoginComponent },
  { path: "/navbar", component: Navbar },
  { path: "/clientCity", component: clientCityPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```
