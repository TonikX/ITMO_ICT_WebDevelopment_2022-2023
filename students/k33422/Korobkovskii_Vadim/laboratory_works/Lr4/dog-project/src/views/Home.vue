<template>
  <div>
    <v-card
      class="mx-auto"
      width="600"
      variant="outlined"
    >
      <template v-slot:title>
        <h1>Выставки собак</h1>
      </template>
      <v-card-text>
          <template v-if="auth">
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="secondary" rounded="lg" @click="myProfile">Мой профиль</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="secondary" rounded="lg" @click="goDog">Список собак</v-btn></div><br>
           <div class="d-flex align-center flex-column flex-md-row">
             <v-btn variant="outlined" color="secondary" rounded="lg" @click="goDogCreate">Добавление новой собаки</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="secondary" rounded="lg" @click="goParticipant">Список участников выставок</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="secondary" rounded="lg" @click="goParticipantCreate">Добавление новой собаки-участника выставки</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="error" rounded="lg" @click="goLogout">Выйти</v-btn></div>
          </template>
          <template v-else>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="success" rounded="lg" @click="goLogin">Войти</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="primary" rounded="lg" @click="goRegistration">Зарегистрироваться</v-btn></div>
          </template>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data: () => ({
    authorized: false
  }),
  // created () {
  //   // const response = this.axios.get('http://127.0.0.1:8000/lib/readers/list/')
  //   // console.log('hehe' + ' ' + localStorage.getItem('auth_token'))
  //   if (sessionStorage.getItem('auth_token')) {
  //     if (sessionStorage.getItem('auth_token') !== '-1') {
  //       this.authorized = true
  //     }
  //   }
  // },
  computed: {
    auth() {
       if (sessionStorage.getItem('auth_token')) {
         return true
       }
    }
  },
  methods: {
    myProfile () {
      this.$router.push({ name: 'profile'})
    },
    goDog () {
      this.$router.push({ name: 'dogs' })
    },
    goParticipant () {
      this.$router.push({ name: 'dog_participation' })
    },
    goLogout () {
      sessionStorage.removeItem("auth_token")
      alert("Вы вышли из аккаунта")
      window.location = '/'
    },
    goLogin () {
      this.$router.push({ name: 'login' })
    },
    goRegistration () {
      this.$router.push({ name: 'registration' })
    },
    goDogCreate () {
      this.$router.push({ name: 'dogs_create' })
    },
    goParticipantCreate () {
      this.$router.push({ name: 'dog_participation_create'})
    }
  }
}
</script>
