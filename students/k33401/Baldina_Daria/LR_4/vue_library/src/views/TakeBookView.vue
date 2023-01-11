<template>
    <v-app>
        <bar-layout> 
            <TakeBook />
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
          <v-text-field
            label="Дата выдачи"
            v-model="submitForm.issue_date"
            name="issue_date"
            type="date"/>
          <v-text-field
            label="Дата возврата"
            v-model="submitForm.due_date"
            name="due_date"
            type="date"/>
        </div>
      </v-card-text>
    </v-card>
    <v-btn color="primary" light @click="takeBook">Оформить</v-btn>
  </v-col>
  </v-row>
  </v-main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import TakeBook from '@/components/TakeBook.vue'
import axios from 'axios'
export default {
  name: 'TakeBookView',
  components:{ BarLayout, TakeBook},
  data: () => ({
    book: Object,
    reader: Object,
    submitForm: {
      book: '',
      reader: '',
      issue_date: '',
      due_date: ''
    }
  }),
  created () {
    this.loadReaderData()
    this.loadBook()
  },
  
  methods: {
    async loadBook () {
      this.book_url = 'http://127.0.0.1:8000/library/books/' + this.$route.params.id
      const response = await axios.get(this.book_url)
      this.book = response.data
    },
    async takeBook () {
      this.submitForm.book = this.book.id
      this.submitForm.reader = this.reader.id
      await axios.post('http://127.0.0.1:8000/library/take_out/', this.submitForm)
      await this.$router.push({ name: 'Book', params: { id: this.book.id } })
    },
    async loadReaderData () {
      const response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.auth_token}`
          }
        })
      this.reader = response.data
    },
}}

</script>