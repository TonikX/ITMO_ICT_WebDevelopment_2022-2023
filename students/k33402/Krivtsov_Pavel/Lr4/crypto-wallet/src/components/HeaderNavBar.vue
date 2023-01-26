<template>
  <header class="p-3 border-bottom bg-navbar">
    <div class="container">
      <div class="d-flex flex-wrap align-items-baseline justify-content-center">
        <router-link to="/" class="navbar-logo">
          <img class="filter-logo" src="@/assets/wallet2.svg" alt="Wallet" width="32" height="32">
          crypto wallet
        </router-link>

        <ul class="nav col-12 col-lg-auto me-lg-auto justify-content-center">
          <li>
            <router-link to="/market" class="nav-link px-3 link-main">Рынки</router-link>
          </li>
        </ul>

        <div v-if="isAuth" class="btn-group">
          <button @click="$router.push({name: 'profile'})" type="button" class="btn btn-main btn-md">
            Профиль
          </button>

          <button type="button" class="btn btn-md btn-main dropdown-toggle dropdown-toggle-split"
                  data-bs-toggle="dropdown" aria-expanded="false">
            <span class="visually-hidden">Toggle Dropdown</span>
          </button>

          <ul class="dropdown-menu dropdown-menu-dark">
            <li>
              <button @click="$router.push({name: 'profile'})" class="dropdown-item">Профиль</button>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li>
              <button @click="logout" class="dropdown-item">Выйти</button>
            </li>
          </ul>
        </div>

        <div v-else class="btn-group">
          <button @click="$router.push({name: 'register'})" type="button" class="btn btn-main btn-md">
            Профиль
          </button>

          <button type="button" class="btn btn-md btn-main dropdown-toggle dropdown-toggle-split"
                  data-bs-toggle="dropdown" aria-expanded="false">
            <span class="visually-hidden">Toggle Dropdown</span>
          </button>

          <ul class="dropdown-menu dropdown-menu-dark">
            <li><button @click="$router.push({name: 'login'})" class="dropdown-item">Войти</button></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><button @click="$router.push({name: 'register'})" class="dropdown-item">Зарегистрироваться</button></li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import $ from "jquery"

export default {
  name: "HeaderNavBar",
  data() {
    return {
      isAuth: false
    }
  },
  created() {
    this.isAuth = !!localStorage.getItem("auth_token")
  },
  watch: {
    $route() {
      this.isAuth = !!localStorage.getItem("auth_token")
    }
  },
  methods: {
    logout() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/logout",
        type: "POST",
        success: () => {
          localStorage.setItem("auth_token", "")
          delete $.ajaxSettings.headers['Authorization']
          this.isAuth = false,
          this.$router.push({name: "welcome"})
        },
        error: (response) => {
          alert(Object.values(response.responseJSON)[0])
        }
      })
    }
  }
}
</script>

<style scoped>

</style>