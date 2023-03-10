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
