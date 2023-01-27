
<script>
import { mapState, mapActions } from 'pinia';
import useUsersStore from '@/stores/users'
import useOrdersStore from '@/stores/orders'

export default {
  name: 'TheHeader',
  computed: {
    ...mapState(useUsersStore, ['token'])
  },
  mounted() {
    this.setToken(window.localStorage.getItem('fabiana-user'))
  },
  methods: {
    ...mapActions(useUsersStore, ['setToken']),
    ...mapActions(useOrdersStore, ['fetchCartItems']),
    openCart() {
      this.fetchCartItems(this.token)
    }
  }
}
</script>

<template>
  <div class="container">
    <header class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-4">
      <RouterLink
        to="/"
        class="d-flex align-items-center col-md-auto mb-2 mb-md-0 text-decoration-none"
      >
        <img
          src="/img/logo.png"
          width="288"
          height="33"
          alt="Fabiana Filippi"
          class="logo"
        >
        <!-- <h1 class="text-uppercase">Fabiana Filippi</h1> -->
      </RouterLink>
      <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
        <li><a href="#" class="nav-link active px-2 link-dark text-decoration-underline">Все товары</a></li>
        <li><a href="#" class="nav-link px-2 link-dark">Одежда</a></li>
        <li><a href="#" class="nav-link px-2 link-dark">Верхняя одежда</a></li>
        <li><a href="#" class="nav-link px-2 link-dark">Обувь и аксессуары</a></li>
        <li><a href="#" class="nav-link px-2 link-dark">О бренде</a></li>
      </ul>
      <div class="col-md-3 text-end">
        <button type="button" class="btn btn-link py-0 px-1" aria-label="Поиск">
          <svg width="18" height="18" viewBox="0 0 18 18" aria-label="Поиск" fill="none" xmlns="http://www.w3.org/2000/svg">
            <use xlink:href="#icon-search"></use>
          </svg>
        </button>
        <RouterLink v-if="token" to="/profile" type="button" class="login-icon-button btn btn-link py-0 px-1" aria-label="Личный кабинет">
          <svg width="16" height="19" viewBox="0 0 16 19" aria-label="Личный кабинет" fill="none" xmlns="http://www.w3.org/2000/svg">
            <use xlink:href="#icon-member"></use>
          </svg>
        </RouterLink>
        <button v-else type="button" class="login-icon-button btn btn-link py-0 px-1" aria-label="Вход в систему" data-bs-toggle="modal" data-bs-target="#auth">
          <svg width="16" height="19" viewBox="0 0 16 19" aria-label="Вход в систему" fill="none" xmlns="http://www.w3.org/2000/svg">
            <use xlink:href="#icon-member"></use>
          </svg>
        </button>
        <button v-if="token" type="button" class="btn btn-link py-0 px-1" aria-label="Избранное">
          <svg width="20" height="19" viewBox="0 0 20 19" aria-label="Избранное" fill="none" xmlns="http://www.w3.org/2000/svg">
            <use xlink:href="#icon-favorite"></use>
          </svg>
        </button>
        <button
          type="button"
          class="cart-icon-button btn btn-link py-0 px-1"
          aria-label="Корзина"
          data-bs-toggle="modal"
          data-bs-target="#cart"
          @click="openCart"
        >
          <svg width="17" height="22" viewBox="0 0 17 22" aria-label="Корзина" fill="none" xmlns="http://www.w3.org/2000/svg">
            <use xlink:href="#icon-cart"></use>
          </svg>
        </button>
      </div>
    </header>
  </div>
</template>
