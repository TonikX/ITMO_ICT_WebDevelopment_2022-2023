<template>
<v-app>
    <bar-layout> 
        <ReturnBook />
  </bar-layout>
  <v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
<v-row class="mx-3.5">
 <v-col cols="5" class="mx-auto">
<br><br>
<v-card>
<v-card-title>
    <h2>{{ this.book.title }}</h2>
  </v-card-title>

  <v-card-text>
    <div class="text--primary">
        <b>Автор(-ы):</b>  {{ this.book.authors }}<br>
        <b>Жанр:</b>  {{ this.book.genre }} <br>
        <b>Год издания:</b>  {{ this.book.publication_year }} <br>
        <b>Издательство:</b>  {{ this.book.publisher }} <br>
        <b>Библиотечный номер:</b>  {{ this.book.book_cypher }} <br>
      <br>
      </div>
    </v-card-text>
    </v-card>

      <v-card>
      <v-card-text >
        <div class="text--primary">
          Дата выдачи: {{ this.issue_date }} <br>
          Дата возврата: {{ this.due_date }}
        </div>
      </v-card-text>
    </v-card>

<v-btn style="margin-top:0.5cm" color="red" light @click="returnBook">Вернуть</v-btn>
</v-col>
</v-row>
</v-main>
</v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import ReturnBook from '@/components/ReturnBook.vue'
import axios from 'axios'
export default {
name: 'ReturnBookView',
components:{ BarLayout, ReturnBook},    
data: () => ({
  book: '',
  reader: '',
  issue_date: '',
  due_date: ''
}),

created () {
this.loadReaderData()
},

methods: {
async loadReaderData () {
    this.book_url = 'http://127.0.0.1:8000/library/readers-book/edit/' + this.$route.params.id
    const response = await axios.get(this.book_url)
    this.book = response.data.book
    this.reader = response.data.reader
    this.issue_date = response.data.issue_date
    this.due_date = response.data.due_date
    console.log('response.data is', response.data)
},
async returnBook () {
      this.return_url = 'http://127.0.0.1:8000/library/readers-book/edit/' + this.$route.params.id
      await axios.delete(this.return_url)
      alert('Вы вернули книгу в библиотеку')
      await this.$router.push({ name: 'Books' })
    },
}}

</script>