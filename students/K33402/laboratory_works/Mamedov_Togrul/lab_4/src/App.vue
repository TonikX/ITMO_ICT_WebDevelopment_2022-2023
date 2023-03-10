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
