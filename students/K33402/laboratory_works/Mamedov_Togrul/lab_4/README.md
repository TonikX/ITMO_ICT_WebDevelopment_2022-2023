# Лабораторная работа №3 Мамедов Тогрул К33402

# Описание

Лабораторная работа №4 является совмещенной с 3ей лабоаторной работой и представляет собой фронт часть 
для приложения которое мы писали

#AllUsers

<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">All Users</h1>
    <router-link to="/new-reader" class="btn btn-primary mt-3">Add new user</router-link>
    <table class="table">
      <thead>
      <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Email</th>
        <th>Age</th>
        <th>Profile</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.age }}</td>
        <td><router-link :to="'users/' + user.id">Profile</router-link></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    }
  },
  async mounted() {
    try {
      const response = await axios.get('http://localhost:8001/readers/', {
        headers: {
          'accept': 'application/json',
          'X-CSRFToken': 'qLPcRBcn40VgMGedRMMMybZTJCicmmuv4wvbh3o60LBo4uhSiirKpoPYY1KAlNpQ',
        },
      });
      this.users = response.data;
    } catch (error) {
      console.log(error);
    }
  },
}
</script>


#Aut

<template>
  <div class="container">
    <h1 class="mt-5">Login</h1>
    <div v-if="isLoggedIn">You're already logged in!</div>
    <div v-else>
      <form class="mt-4" @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label" for="username">Username:</label>
          <input id="username" v-model="username" class="form-control" required type="text">
        </div>
        <div class="mb-3">
          <label class="form-label" for="password">Password:</label>
          <input id="password" v-model="password" class="form-control" required type="password">
        </div>
        <button class="btn btn-primary" type="submit">Login</button>
      </form>
  </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  computed: {
    isLoggedIn() {
      return localStorage.getItem('accessToken');
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8001/jwt/create/', {
              username: this.username,
              password: this.password,
            },
            {
              headers: {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': 'qLPcRBcn40VgMGedRMMMybZTJCicmmuv4wvbh3o60LBo4uhSiirKpoPYY1KAlNpQ'
              }
            });
        const accessToken = response.data.access;
        localStorage.setItem('accessToken', accessToken);
        location.reload(); // Reload the page
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>

#CreateLibrarian

<template>
  <div class="container my-5">
    <h1>Create Librarian</h1>
    <form @submit.prevent="createLibrarian">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" v-model="username" required>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="password" required>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" v-model="email" required>
      </div>
      <div class="mb-3">
        <label for="firstName" class="form-label">First Name</label>
        <input type="text" class="form-control" id="firstName" v-model="firstName" required>
      </div>
      <div class="mb-3">
        <label for="lastName" class="form-label">Last Name</label>
        <input type="text" class="form-control" id="lastName" v-model="lastName" required>
      </div>
      <div class="mb-3">
        <label for="age" class="form-label">Age</label>
        <input type="number" class="form-control" id="age" v-model="age" required>
      </div>
      <div class="mb-3">
        <label for="library" class="form-label">Library</label>
        <input type="number" class="form-control" id="library" v-model="library" required>
      </div>
      <button type="submit" class="btn btn-primary">Create</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateLibrarian',
  data() {
    return {
      username: '',
      password: '',
      email: '',
      firstName: '',
      lastName: '',
      age: null,
      library: null
    }
  },
  methods: {
    createLibrarian() {
      axios.post('http://localhost:8001/librarians/', {
        username: this.username,
        password: this.password,
        email: this.email,
        is_active: true,
        first_name: this.firstName,
        last_name: this.lastName,
        age: this.age,
        library: this.library
      }, {
        headers: {
          'X-CSRFToken': localStorage.getItem('accessToken'),
          'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
        }
      })
          .then(() => {
            this.$router.push('/librarians');
          })
          .catch(error => {
            console.log(error);
          });
    }
  }
}
</script>

#LibrarianList

<template>
  <div class="container py-4">
    <h2 class="mb-4">Librarians List</h2>
    <router-link to="/add-librarian" class="btn btn-primary mt-3">Add new librarian</router-link>

    <table class="table table-striped">
      <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Username</th>
        <th scope="col">Email</th>
        <th scope="col">Library</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(librarian, index) in librarians" :key="librarian.id">
        <th scope="row">{{ index + 1 }}</th>
        <td>{{ librarian.username }}</td>
        <td>{{ librarian.email }}</td>
        <td>{{ librarian.library }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LibrarianList',
  data() {
    return {
      librarians: [],
    }
  },
  mounted() {
    this.loadLibrarians()
  },
  methods: {
    loadLibrarians() {
      axios.get('http://localhost:8001/librarians/')
          .then(response => {
            this.librarians = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
}
</script>

#NewReader

<template>
  <div class="container mt-5">
    <h1 class="mb-4">Add New User</h1>
    <form @submit.prevent="submitForm">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" class="form-control" id="username" v-model="formData.username" required>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="formData.password" required>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" v-model="formData.email" required>
      </div>
      <div class="mb-3">
        <label for="firstName" class="form-label">First Name</label>
        <input type="text" class="form-control" id="firstName" v-model="formData.first_name" required>
      </div>
      <div class="mb-3">
        <label for="lastName" class="form-label">Last Name</label>
        <input type="text" class="form-control" id="lastName" v-model="formData.last_name" required>
      </div>
      <div class="mb-3">
        <label for="age" class="form-label">Age</label>
        <input type="number" class="form-control" id="age" v-model="formData.age" required>
      </div>
      <button type="submit" class="btn btn-primary">Add User</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        username: '',
        password: '',
        email: '',
        first_name: '',
        last_name: '',
        age: null,
      }
    }
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8001/readers/', this.formData, {
          headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': 'qLPcRBcn40VgMGedRMMMybZTJCicmmuv4wvbh3o60LBo4uhSiirKpoPYY1KAlNpQ',
            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
          }
        });
        console.log(response.data);
        // Redirect to the users list page
        this.$router.push('/users');
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>

#User

<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">User ID: {{ user.id }}</h1>
    <table class="table">
      <tr>
        <th>Username:</th>
        <td>{{ user.username }}</td>
      </tr>
      <tr>
        <th>Email:</th>
        <td>{{ user.email }}</td>
      </tr>
      <tr>
        <th>Age:</th>
        <td>{{ user.age }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {},
    }
  },
  async mounted() {
    try {
      const userId = this.$route.params.id;
      const response = await axios.get(`http://localhost:8001/readers/${userId}/`, {
        headers: {
          'accept': 'application/json',
          'X-CSRFToken': 'qLPcRBcn40VgMGedRMMMybZTJCicmmuv4wvbh3o60LBo4uhSiirKpoPYY1KAlNpQ',
        },
      });
      this.user = response.data;
    } catch (error) {
      console.log(error);
    }
  },
}
</script>

#index.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD" crossorigin="anonymous"></script>
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>

#App

<template>
  <div id="app">
    <header>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand">Home</router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                  aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
              </li>
              <li v-if="isLoggedIn" class="nav-item">
                <button class="nav-link btn btn-link" @click="logout">Logout</button>
              </li>
              <li v-else class="nav-item">
                <router-link to="/login" class="nav-link">Login</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>

    <main class="container my-3">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return localStorage.getItem('accessToken');
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('accessToken');
      location.reload();
      // Redirect to the login page
    }
  }
}
</script>


