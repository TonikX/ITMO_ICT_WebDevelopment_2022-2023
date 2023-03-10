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
