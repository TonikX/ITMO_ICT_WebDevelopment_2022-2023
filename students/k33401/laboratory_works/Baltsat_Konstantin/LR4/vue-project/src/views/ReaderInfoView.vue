<template>
    <v-app>
        <bar-layout> 
            <ReaderInfo />
      </bar-layout>
<v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
    <v-row class="mx-3.5">
     <v-col cols="4" class="mx-auto">
<br><br>
<div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Личный кабинет</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
            <b>Имя:</b> {{ this.reader.first_name }} <br>
            <b>Фамилия:</b> {{ this.reader.last_name }} <br>
            <b>Логин:</b> {{ this.reader.username }} <br>
            <b>Номер билета:</b> {{ this.reader.card_number }} <br>
            <b>Дата рождения:</b> {{ this.reader.date_of_birth }} <br>
            <b>Образование:</b> {{ this.reader.education }} <br>
            <b>Ученая степень:</b> {{ this.reader.degree ? 'есть' : 'нет' }} <br>
            <b>Паспортные данные:</b> {{ this.reader.passport }} <br>
            <b>Адрес:</b> {{ this.reader.address }} <br>
            <b>Телефон:</b> {{ this.reader.phone }} <br>
        </div>
      </v-card-text>
    </v-card>


    <h3  v-if= " arrLegth > 0">Вы сейчас читаете:</h3>
    <h3 v-else> Сейчас на книжной полке пусто.</h3>
      <v-card  elevation="5"
        outlined
        class="my-2"
         v-for="book in reader.reader_book" v-bind:key="book" v-bind:book="book">
            <a @click.prevent="goBook(book.id)">{{ book.title }}</a>
          </v-card>
    
  

  <v-btn block color="green" light @click.prevent="goEdit">Редактировать профиль</v-btn>


</div>
</v-col>
</v-row>
</v-main>
</v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import ReaderInfo from '@/components/ReaderInfo.vue'
import axios from 'axios'
export default {
name: 'ReaderLK',
components:{ BarLayout, ReaderInfo},  
data () {
    return {
      arrLegth: Number,
      reader: Object
    }
  },
  created () {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData () {
      const response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.auth_token}`
          }
        })
      this.reader = response.data
      await this.loadCurrentlyReading()
    },
    async loadCurrentlyReading () {
      this.cur_read_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await axios.get(this.cur_read_url)
      this.reader = response.data
      this.arrLegth = this.reader.reader_book.length
    },
    goBook (bookID) {
      this.$router.push({ name: 'Book', params: { id: bookID } })
    },
    goEdit () {
      this.$router.push({ name: 'EditReader' })
    }
  }
}  
</script>