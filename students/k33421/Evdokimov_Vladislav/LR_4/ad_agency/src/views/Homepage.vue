<template>
  <div>
    <v-card>
       <h1 class="headline"> Агентство  "Луч"</h1>
      <v-card-text>
          <template v-if="isLogged">
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goCreateRequest">Создать заявку</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goAddStuff()">Добавить сущность</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goClients">Клиенты</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goServices">Услуги</v-btn></div><br>
           <div class="d-flex align-center flex-column flex-md-row">
             <v-btn variant="outlined" color="outline" rounded="lg" @click="goMaterials">Материалы</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goStaff">Сотрудники</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goRequests">Заявки</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="goLogout()">Выйти</v-btn></div>
          </template>
          <template v-else>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="primary" rounded="lg" @click="goLogin">Войти</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="primary" rounded="lg" @click="goRegistration()">Зарегистрироваться</v-btn></div>
          </template>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data: () => ({}),
  computed: {
    // eslint-disable-next-line vue/return-in-computed-property
    isLogged() {
       return localStorage.getItem('token')
    }
  },
  methods: {
    goStaff () {
      this.$router.push({ name: 'staffList' })
    },
    goServices () {
      this.$router.push({ name: 'services' })
    },
    goLogout () {
      localStorage.removeItem('token')
      window.location = '/'
    },
    goLogin () {
      this.$router.push({ name: 'signin' })
    },
    goRegistration () {
      this.$router.push({ name: 'signup' })
    },
    goMaterials () {
      this.$router.push({ name: 'materials' })
    },
    goAddClient () {
      this.$router.push({ name: 'addclient' })
    },
    goClients () {
      this.$router.push({ name: 'clients' })
    },
    goCreateRequest () {
      this.$router.push({ name: 'requestcreation' })
    },
    goRequests () {
      this.$router.push({ name: 'requests' })
    },
    goAddStuff () {
      this.$router.push({ name: 'addstuff' })
    },

  }
}
</script>
