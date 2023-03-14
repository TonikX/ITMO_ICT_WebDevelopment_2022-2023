<template>
  <v-app>
    <bar-layout>
      <DefaultNavigationBar/>
    </bar-layout>
    <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
      <v-col cols="8" class="mx-auto">
        <br><br><br><br>

        <h1>Домашняя страница</h1>

        <br>

        <span>Возможности сайта:</span>

        <p>
          <br> 1. Редактирование личной информации
          <br> 2. Просмотр всех книг
          <br> 3. Бронирвоание/возврат книги
        </p>
      </v-col>
    </v-main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'

export default {
  name: 'HomeView',
  components: {BarLayout, DefaultNavigationBar}
}
</script>
