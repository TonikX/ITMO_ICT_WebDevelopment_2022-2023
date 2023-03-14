<template>
  <section>
    <v-app>
      <bar-layout>
        <DefaultNavigationBar/>
      </bar-layout>

      <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
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
                    <b>Автор:</b> {{ this.book.author }}<br>
                    <b>Год издания:</b> {{ this.book.year_of_publishing }} <br>
                    <b>Издательство:</b> {{ this.book.publisher }} <br>
                    <ul>
                      <li v-for="hall in this.book.book_hall" v-bind:key="hall" v-bind:hall="hall">
                        {{ hall.title }}
                      </li>
                    </ul>
                  </div>
                </v-card-text>
              </v-card>

              <v-btn
                v-if="(!this.is_book_on_hold && this.book_instances.length > 0)"
                color="primary"
                light @click="takeBook">Взять книгу
              </v-btn>

              <a v-if="!this.is_book_on_hold && this.book_instances.length == 0">
                К сожалению, свободных экземпляров книги нет
              </a>

              <v-card
                v-if="this.is_book_on_hold"
                elevation="2"
                outlined
                class="my-2"
              >
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
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'BookView',
  data() {
    return {
      book: Object,
      user_book_instance: Object,
      book_instances: Object,
      reader: Object,
      is_book_on_hold: false,
      bookReaderID: ''
    }
  },
  created() {
    this.loadBook()
    this.loadReader()
  },
  components: {BarLayout, DefaultNavigationBar},

  methods: {
    async loadBook() {
      this.book_url = 'http://127.0.0.1:8000/library/books/' + this.$route.params.id
      const response = await axios.get(this.book_url)
      this.book = response.data

      this.loadBookInstances()
    },

    async loadBookInstances() {
      const get_book_instances_request_url = 'http://127.0.0.1:8000/library/book_instances/free/by_book_id/' + this.book.id
      const get_book_instances_response = await axios.get(get_book_instances_request_url)

      this.book_instances = get_book_instances_response.data
    },

    async loadReader() {
      const get_user_response_response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: { Authorization: `Token ${localStorage.auth_token}` }
        })
      const user = get_user_response_response.data
      const get_userreader_request_url = "http://127.0.0.1:8000/library/userreaders/" + user.id
      const get_userreader_response = await axios.get(get_userreader_request_url)
      const userreader = get_userreader_response.data
      const get_reader_request_url = "http://127.0.0.1:8000/library/readers/" + userreader.reader
      const get_reader_response = await axios.get(get_reader_request_url)
      const reader = get_reader_response.data

      this.reader = reader

      await this.checkIsOnHold()
    },

    async checkIsOnHold() {
      const get_reader_books_url = 'http://127.0.0.1:8000/library/readerbooks/by_reader/' + this.reader.ticket
      const get_reader_books_response = await axios.get(get_reader_books_url)
      const readers_book = get_reader_books_response.data

      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(readers_book)) {
        if (value.book_instance.book.id === this.book.id) {
          this.is_book_on_hold = true
          this.user_book_instance = value.book_instance
          break
        }
      }
    },

    async takeBook() {
      const free_book_instance = this.book_instances[Math.floor(Math.random()*this.book_instances.length)]
      await axios.post(
        'http://127.0.0.1:8000/library/readerbooks/create/',
        {
          reader: this.reader.ticket,
          book_instance: free_book_instance.id
        }
      )

      this.$router.push({name: 'Reader'})
    },

    async returnBook() {
      const delete_reader_book_request_url = "http://127.0.0.1:8000/library/readerbooks/by_instance/" + this.user_book_instance.id

      await axios.delete(delete_reader_book_request_url)

      this.$router.push({name: 'Books'})
    },
  }
}
</script>
