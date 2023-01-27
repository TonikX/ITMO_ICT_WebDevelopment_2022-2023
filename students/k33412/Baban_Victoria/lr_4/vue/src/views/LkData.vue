<template>
  <Header/>
  <main class="p-5 container-fluid d-flex flex-row vh-100">
    <aside  class="col-lg-3   d-flex flex-column justify-content-start">
      <img src="https://e7.pngegg.com/pngimages/398/54/png-clipart-silhouette-graphics-male-silhouette-animals-hand.png" height="auto" alt="Фото профиля" class="img-fluid img-thumbnail">
      <ul class="list-group col-12">
        <li class="list-group-item list-group-item-secondary">
          <a class="text-decoration-none link-dark active" aria-current="true" href="#">Мои данные</a>
        </li>
        <li class="list-group-item">
          <a class="text-decoration-none link-dark "  href="#" @click="$router.push('/lk/')">Мои мероприятия</a>
        </li>
        <li class="list-group-item">
          <a class="text-danger text-decoration-none link-dark" href="#" @click="Logout">Выйти</a>
        </li>
      </ul>
    </aside>
    <section class="col-lg-6   px-5">
      <h2>Мои данные</h2>
      <div class="row mt-4 ">
          <ul class="list-group">
            <li class="list-group-item">Имя: {{ user.first_name }}</li>
            <li class="list-group-item">Фамилия: {{ user.last_name }}</li>
            <li class="list-group-item">ID: {{ user.id }}</li>
            <li class="list-group-item">Email: {{ user.email }}</li>
            <li class="list-group-item">Username: {{ user.username }}</li>
          </ul>
      </div>
    </section>
  </main>
  <Footer/>
</template>

<script>
import { mapState, mapActions } from 'pinia'
import useUserStore from '@/stores/user'
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";


export default {
  name: "LkData",
  components: {Footer, Header},
  computed: {
    ...mapState(useUserStore, ['user', 'token']),
  },
  mounted() {
    this.currentUserInfo().then(result => {
      if (!result?.email) {
        this.$router.replace({ path:'/' })
      }
    })
  },
  methods: {
    ...mapActions(useUserStore, ['currentUserInfo', 'logout']),
    async Logout() {
      await this.logout()
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>