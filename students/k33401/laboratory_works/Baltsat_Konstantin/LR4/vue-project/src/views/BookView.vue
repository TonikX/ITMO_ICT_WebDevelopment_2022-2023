<template>
    <section>
    <v-app>
        <bar-layout> 
            <OneBook />
      </bar-layout>
      <v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
    <v-row class="mx-3.5">
     <v-col cols="5" class="mx-auto">
<br><br>
<div>
    <v-card
      elevation="2"
      outlined
      class="my-5"
    >
      <v-card-title>
        <h2>{{ this.book.title }}</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
            <b>Авторы:</b>  {{ this.book.authors }}<br>
            <b>Жанр:</b>  {{ this.book.genre }} <br>
            <b>Год издания:</b>  {{ this.book.publication_year }} <br>
            <b>Издательство:</b>  {{ this.book.publisher }} <br>
            <b>Библиотечный номер:</b>  {{ this.book.book_cypher }} <br>
          <br>
          <b>Залы:</b> 
          <ul>
            <li v-for="hall in this.book.book_hall" v-bind:key="hall" v-bind:hall="hall">
              {{ hall.title }}
            </li>
          </ul>
        </div>
      </v-card-text>
    </v-card>

    <v-btn v-if="!this.bookOnHold" color="primary" light @click="takeBook">Взять книгу</v-btn>

    <v-card
      elevation="2"
      outlined
      class="my-2"
      v-else>
      <v-card-text>
        <div class="text--primary">Вы сейчас читаете эту книгу</div>
      </v-card-text>
      <v-spacer></v-spacer>
      <v-btn block color="red" light @click="returnBook">Вернуть книгу в библиотеку</v-btn>
    </v-card>
  </div>
</v-col>
</v-row>
</v-main>
</v-app>
</section>
</template>


<script>
import BarLayout from '@/layouts/BarLayout.vue'
import OneBook from '@/components/OneBook.vue'
import axios from 'axios'
export default {
  name: 'BookView',
  data () {
    return {
      book: Object,
      reader: Object,
      bookOnHold: false,
      bookReaderID: ''
    }
  },
  created () {
    this.loadBook()
    this.loadReaderData()
  },
    components:{ BarLayout, OneBook},
    
  methods: {    
    async loadBook () {
      this.book_url = 'http://127.0.0.1:8000/library/books/' + this.$route.params.id
      const response = await axios.get(this.book_url)
      this.book = response.data
    }, 
    async loadReaderData() {
        const response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.auth_token}`
          }
        })
      this.reader = response.data
      await this.checkOnHold()
    },
    async checkOnHold () {
      this.reader_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await axios.get(this.reader_url)
      // console.log(response.data)
      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data.reader_book)) {
        if (value.id === this.book.id) {
          this.bookOnHold = true
          break
        }
      }
    },
    takeBook () {
      this.$router.push({ name: 'TakeBook', params: { id: this.book.id } })
    },
    async returnBook () {
      const response = await axios.get('http://127.0.0.1:8000/library/readers-book/')

      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data)) {
        if (value.reader === this.reader.id && value.book === this.book.id) {
          this.bookReaderID = value.id_rb
          break
        }
      }
      await this.$router.push({ name: 'ReturnBook', params: { id: this.bookReaderID } })
    },

  }}
</script>