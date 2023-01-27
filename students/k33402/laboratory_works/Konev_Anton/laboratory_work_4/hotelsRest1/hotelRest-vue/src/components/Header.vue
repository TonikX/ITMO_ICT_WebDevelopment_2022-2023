<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="mynavbar">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">Комнаты</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/guests">Гости</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/report">Отчет</RouterLink>
          </li>
        </ul>
        <button class="btn btn-warning" type="button" @click="showModal=true" v-if="!token">Войти</button>
        <div class="logged d-flex align-items-center" v-if="token">
          <p class="username me-4 p-2 m-0">{{ user.username }}</p>
          <button class="btn btn-danger" @click="logout">Выйти</button>
        </div>
      </div>
    </div>
  </nav>
  <Login v-show="showModal" @close-modal="showModal = false" @show-register="[showModal=false, showRegister=true]"/>
  <Register v-show="showRegister" @close-register="showRegister=false"
            @show-modal="[showRegister=false, showModal=true]"/>
</template>

<script>
import Login from "@/components/modal/Login.vue";
import Register from "@/components/modal/Register.vue";
import {mapActions, mapState} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  name: 'Header',
  components: {
    Login,
    Register
  },
  data() {
    return {
      showModal: false,
      showRegister: false,
    }
  },
  methods: {
    ...mapActions(useUsersStore, ["onLogout"]),

    async logout() {
      if (confirm("Вы действительно хотите выйти?")) {
        await this.onLogout()
        window.location.reload()
      }
    }

  },
  computed: {
    ...mapState(useUsersStore, ["user"]),
    ...mapState(useUsersStore, ['token'])
  }
}
</script>

<style>
.username {
  color: white;
}
</style>