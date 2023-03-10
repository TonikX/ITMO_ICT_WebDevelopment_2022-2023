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
