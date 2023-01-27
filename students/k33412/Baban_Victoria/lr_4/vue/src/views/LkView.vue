<template>
  <Header/>
  <main class="p-5 container-fluid d-flex flex-row vh-100">
    <aside  class="col-lg-3   d-flex flex-column justify-content-start">
        <img src="https://e7.pngegg.com/pngimages/398/54/png-clipart-silhouette-graphics-male-silhouette-animals-hand.png" height="auto" alt="Фото профиля" class="img-fluid img-thumbnail">
        <ul class="list-group col-12">
            <li class="list-group-item">
                <a class="text-decoration-none link-dark" href="#" @click="$router.push('/lk/data')">Мои данные</a>
            </li>
            <li class="list-group-item list-group-item-secondary">
                <a class="text-decoration-none link-dark active" aria-current="true" href="#">Мои мероприятия</a>
            </li>
            <li class="list-group-item">
                <a class="text-danger text-decoration-none link-dark" href="#" @click="Logout">Выйти</a>
            </li>
        </ul>
    </aside>
    <section class="col-lg-9   px-5">
        <h2>Мои мероприятия</h2>
        <MyEvents/>
    </section>
</main>
  <Footer/>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import MyEvents from "../components/MyEvents.vue";
import {mapActions, mapState} from "pinia";
import useUserStore from '@/stores/user'

export default {
name: "LkView",
  components: {MyEvents, Footer, Header},
  computed: {
    ...mapState(useUserStore, ['token'])
  },
   mounted() {
    this.setToken(window.localStorage.getItem('token'))
  },
  methods: {
    ...mapActions(useUserStore, ['setToken', 'logout']),
    async Logout() {
      await this.logout()
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>