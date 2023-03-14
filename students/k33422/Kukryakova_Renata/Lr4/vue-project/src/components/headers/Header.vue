<template>
  <header class="d-flex justify-content-center py-3">
    <ul class="nav nav-pills">
      <li class="nav-item">
        <div class="nav-link pt-1">
          <svg class="nav-logo" style=" height: 27px">
            <use xlink:href="#logo">
            </use>
          </svg>
        </div>
      </li>
      <li class="nav-item"><a href="/main" class="nav-link">Купить криптовалюту</a></li>
      <li class="nav-item"><a href="#" @click="checkAuth" class="nav-link">Мой портфель</a></li>
<!--      <li class="nav-item"><a href="/charts" class="nav-link">Графики</a></li>-->
      <li class="nav-item" id="logout" :style="[this.isLogged ? {'display' : 'block'} : {'display' : 'none'}]">
        <button class="logout-button" @click="logout"
                style="border: none; background-color: white; padding-top:5px">
          <svg class="logout-img" style="width: 27px; height: 27px">
            <use xlink:href="#logout">
            </use>
          </svg>
        </button>
      </li>
    </ul>
  </header>
</template>

<script>
import router from "@/router";

export default {
  name: 'Header',
  data() {
    return {
      isLogged: false
    }
  },
  methods: {
    logout() {
      if (confirm('Вы действительно хотите выйти?')) {
        localStorage.clear()
        if (this.$route.path === '/personal') {
          router.push('/')
        } else {
          window.location.reload()
        }
      }
    },
    checkAuth() {
      if (!this.isLogged) {
        router.push('/login')
      } else {
        router.push('/personal')
      }
    }
  },
  mounted() {
    localStorage.getItem('pinia_users') ? this.isLogged = true : this.isLogged = false
  }
}
</script>

<style>
.nav-logo {
  width: 40%;
}

.nav-link {
  font-family: Tahoma, sans-serif;
  font-weight: bold;
  color: var(--link-color) !important;
}

.nav-link:hover {
  color: var(--link-hover) !important;
}
</style>
