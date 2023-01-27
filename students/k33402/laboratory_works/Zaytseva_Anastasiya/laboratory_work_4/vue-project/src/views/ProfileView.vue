<script>
import { mapState, mapActions } from 'pinia'
import useUsersStore from '@/stores/users'
import useOrdersStore from '@/stores/orders'
import { COLORS } from '@/const/lang'

export default {
  name: 'ProfileView',
  data() {
    return {
      COLORS
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user', 'token']),
    ...mapState(useOrdersStore, ['orders']),
  },
  mounted() {
    this.fetchCurrentUser().then(result => {
      if (!result?.email) {
        this.$router.replace({ path:'/' })
      }
    })
    this.fetchOrders(this.token)
  },
  methods: {
    ...mapActions(useUsersStore, ['fetchCurrentUser', 'logout']),
    ...mapActions(useOrdersStore, ['fetchOrders', 'token']),
    async onLogout() {
      await this.logout()
      this.$router.push('/')
    }
  }
}
</script>

<template>
<main class="container">
  <nav class="mt-4" aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><RouterLink to="/" class="link-dark">Главная</RouterLink></li>
      <li class="breadcrumb-item active" aria-current="page">Личный кабинет</li>
    </ol>
  </nav>
  <div v-if="user.email" class="row mt-4">
    <div class="col-4">
      <ul class="list-group">
        <li class="list-group-item">ID: {{ user.id }}</li>
        <li class="list-group-item">Email: {{ user.email }}</li>
        <li class="list-group-item">Username: {{ user.username }}</li>
        <li class="list-group-item">Token: {{ token }}</li>
      </ul>
      <button
        class="btn btn-danger btn-lg mt-3"
        @click="onLogout"
      >Выйти</button>
    </div>
    <div class="col-1">

    </div>
    <div class="col">
      <h1>Заказы</h1>
      <div
        v-for="order in orders"
        :key="'order-' + order.id"
        class="border py-3 px-4"
      >
        <h3 class="mb-4">Заказ #{{ order.id }}</h3>
        <RouterLink
          v-for="item in order.cart"
          :key="'item' + item.id"
          :to="`/products/${item.product.id}`"
          class="row justify-content-between align-items-stretch"
          style="text-decoration:none"
        >
          <div class="col-auto">
            <img
              :src="item.product.photo"
              :alt="item.product.name"
              width="64"
              height="64"
            >
          </div>
          <div class="col d-flex align-items-center">
            <h5>{{ item.product.name + (item.quantity > 1 ? (' * ' + item.quantity) : '') }}</h5>
          </div>
          <div class="col-auto">
            <div class="d-flex justify-content-between align-items-end flex-column" style="height:100%">
              <small>{{ item.product.price }}</small>
            </div>
          </div>
          <hr class="mt-3">
        </RouterLink>
      </div>
    </div>
  </div>
</main>
</template>

<style scoped>
main.container {
  min-height: 60vh;
}
</style>
