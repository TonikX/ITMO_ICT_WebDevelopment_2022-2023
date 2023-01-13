<template>
    <section>
    <v-app>
        <bar-layout> 
            <AllBooks />
      </bar-layout>
<v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
    <v-row class="mx-3.5">
     <v-col cols="4" class="mx-auto">
<br><br>
<div>
    <h2>Каталог библиотеки</h2>
          <v-card  elevation="5"
        outlined
        class="my-2"
         v-for="book in books" v-bind:key="book" v-bind:book="book">
            <a @click.prevent="goBook(book.id)">{{ book.title }}</a>
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
import AllBooks from '@/components/AllBooks.vue'
import axios from 'axios'
export default {
    name: 'BookList',
    data () {
    return {
      books: ''
    }
    },
    created () {
      this.loadBooks()
    },
    components:{ BarLayout, AllBooks},
    
  methods: {
    async loadBooks () {
        const response = await axios.get('http://127.0.0.1:8000/library/books/')
        this.books = response.data
    },
    goBook (bookID) {
    
      this.$router.push({ name: 'Book', params: { id: bookID } })
    },
  }}
</script>