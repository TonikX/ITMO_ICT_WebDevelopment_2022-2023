<template>
    <header>
      <b-navbar>
        <div class="container">
          <header-nav-brand />
          <b-navbar-nav class="justify-content-end">
            <template v-if="auth">
            <header-nav-item navLink="profile" navText="Профиль" />
            <header-nav-item navLink="dog" navText="Список собак" />
            <header-nav-item navLink="dog/create" navText="Добавить собак" />
            <header-nav-item navLink="dog_reg" navText="Список участников" />
            <header-nav-item navLink="dog_reg/create" navText="Добавить участников" />
            <b-nav-form @submit="goLogout">
          <b-button size="sm" class="my-2 my-sm-0 this-btn" type="submit">Выйти</b-button>
        </b-nav-form>           
       </template>
            <template v-else>
            <header-nav-item navLink="login" navText="Вход" />
            <header-nav-item navLink="register" navText="Регистрация" />
            </template>
          </b-navbar-nav>
        </div>
      </b-navbar>
    </header>
  </template>
<script>
  import HeaderNavItem from "../components/HeaderNavItem.vue"
  import HeaderNavBrand from "../components/HeaderBrand.vue"
  export default {
    name: "AppHeader",
    components: { HeaderNavItem, HeaderNavBrand },
    data: () => ({
      authorized: false
    }),
    computed: {
      auth() {
         if (sessionStorage.getItem('auth_token')) {
           return true
         }
      }
    },
    methods: {
      goLogout () {
        sessionStorage.removeItem("auth_token")
        alert("You are logged out")
        window.location = '/'
      },
    }
  }
</script>
  <style>
  header {
    background-color: var(--accent-color);
    height: 70px;
  }
  .nav-link:hover {
    color: var(--nav-link-on-hover) !important;
  }
  </style>
