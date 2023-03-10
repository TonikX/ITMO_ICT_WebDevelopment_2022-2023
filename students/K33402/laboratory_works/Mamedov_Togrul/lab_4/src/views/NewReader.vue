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
