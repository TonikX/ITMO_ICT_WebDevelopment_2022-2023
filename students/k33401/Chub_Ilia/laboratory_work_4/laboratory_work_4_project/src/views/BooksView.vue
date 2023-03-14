<template>
  <section>
    <v-app>
      <bar-layout>
        <DefaultNavigationBar/>
      </bar-layout>

      <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
        <v-row class="mx-3.5">
          <v-col cols="4" class="mx-auto">
            <br><br>

            <div>
              <h2>Каталог библиотеки</h2>

              <v-flex d-flex flex-column md-6>
                <v-flex v-for="book in books" :key="book.id">
                  <v-card-text
                    elevation="2"
                    outlined
                    class="my-2"
                  >
                    <p>Название: {{ book.title }} </p>
                    <p>Автор: {{ book.author }} </p>
                    <p>Издательство: {{ book.publisher }}</p>
                    <p>Год издания: {{ book.year_of_publishing }}</p>

                    <v-col cols="3">
                      <v-btn variant="text" color="blue" light @click.prevent="goBook(book.id)">Подробнее</v-btn>
                    </v-col>
                  </v-card-text>
                </v-flex>
              </v-flex>
            </div>
          </v-col>
        </v-row>
      </v-main>
    </v-app>
  </section>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'BooksView',
  data() { return { books: Object } },
  created() { this.loadBooks() },
  components: {BarLayout, DefaultNavigationBar},
  methods: {
    async loadBooks() {
      const response = await axios.get('http://127.0.0.1:8000/library/books/all')
      this.books = response.data
    },
    goBook(bookID) {
      this.$router.push({name: 'Book', params: {id: bookID}})
    },
  }
}
</script>
