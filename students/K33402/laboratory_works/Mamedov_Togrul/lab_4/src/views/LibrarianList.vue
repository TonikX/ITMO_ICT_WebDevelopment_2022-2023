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
