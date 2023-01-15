<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.gif')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>
      <v-col>
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            Bienvenue à l'hotel<br>
             «Harmony»
          </h1>
            Для продолжения войдите или зарегистрируйтесь.
        </v-col>
        <v-col>
            <v-btn color=primary @click='$router.push("/sign-in/")'>Войти</v-btn>
        </v-col>
        <v-col>
            <v-btn color=secondary @click='$router.push("/sign-up/")'>Зарегистрироваться</v-btn>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    console.log(this.isAuth, localStorage.getItem('token'), this.axios.defaults.headers.common.Authorization)
  }
}
</script>
