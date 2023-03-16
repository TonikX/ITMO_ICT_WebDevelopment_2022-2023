<template>
  <div>
    <h1>Система для администратора отеля</h1>
    <b-button v-if="!auth" @click="goLogin">Вход</b-button>
    <b-button v-if="!auth" @click="goRegister">Регистрация</b-button>
    <b-button v-if="auth" @click="goClientAdd">Добавить клиента</b-button>
    <b-button v-if="auth" @click="goBook">Заселить гостя</b-button>
    <b-button v-if="auth" @click="goBookUpdate">Выселить гостя</b-button>
    <b-button v-if="auth" @click="goSched">Добавить расписание</b-button>
    <b-button v-if="auth" @click="goSchedDel">Удалить расписание</b-button>
    <b-button v-if="auth" @click="goLk">Личный кабинет</b-button>
    <b-button v-if="auth" @click="logout">Выход</b-button>
    <vacant v-if="auth"></vacant>
    <bookings v-if="auth"></bookings>
    <clients v-if="auth"></clients>
    <schedules v-if="auth"></schedules>
    <cleaners v-if="auth"></cleaners>
  </div>
</template>

<script>

import Vacant from '@/components/Vacant'
import Bookings from '@/components/Bookings'
import Schedules from '@/components/Schedules'
import Cleaners from '@/components/Cleaners'
import Clients from '@/components/Clients'

export default {
  name: 'Home',
  components: {
    Vacant,
    Bookings,
    Schedules,
    Cleaners,
    Clients
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("auth_token")) {
        return true
      }
    }
  },
  methods: {
            goLogin() {
                this.$router.push({name: 'login'})
            },
            goRegister() {
                this.$router.push({name: 'register'})
            },
            goBook() {
                this.$router.push({name: 'book'})
            },
            goBookUpdate() {
                this.$router.push({name: 'bookupdate'})
            },
            goSched() {
                this.$router.push({name: 'sched'})
            },
            goLk() {
                this.$router.push({name: 'lk'})
            },
            goClientAdd() {
                this.$router.push({name: 'clientadd'})
            },
            goSchedDel() {
                this.$router.push({name: 'scheddel'})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
        },
}
</script>


<style scoped>

</style>
