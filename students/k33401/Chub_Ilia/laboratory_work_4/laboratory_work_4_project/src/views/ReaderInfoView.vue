<template>
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
              class="my-2"
            >
              <br>
              <v-card-title><h2>Профиль</h2></v-card-title>

              <v-card-text>
                <div class="text--primary">
                  <b>Имя:</b> {{ this.user.first_name }} <br>
                  <b>Фамилия:</b> {{ this.user.last_name }} <br>
                  <b>Логин:</b> {{ this.user.username }} <br>
                  <b>Номер билета:</b> {{ this.reader.ticket }} <br>
                  <b>Дата рождения:</b> {{ this.reader.birth_date }} <br>
                  <b>Образование:</b> {{ this.reader.education }} <br>
                  <b>Ученая степень:</b> {{ this.reader.is_has_academic_degree ? 'да' : 'нет' }} <br>
                  <b>Паспортные данные:</b> {{ this.reader.passport_number }} <br>
                  <b>Адрес:</b> {{ this.reader.address }} <br>
                  <b>Телефон:</b> {{ this.reader.phone_number }} <br>
                  <b>Дата регистрации:</b> {{ this.reader.registration_date }} <br>
                </div>
              </v-card-text>
            </v-card>

            <v-col cols="7" class="mx-auto">
              <v-btn block color="blue" light @click.prevent="goEditReaderInfo">Редактировать профиль</v-btn>
            </v-col>

            <v-card
              elevation="2"
              outlined
              class="my-2"
            >
              <br>
              <v-card-title>
                <h2>
                  {{ reader_book_instances.length > 0 ? "Вы сейчас читаете:" : "У вас на руках нет книг" }}
                </h2>
              </v-card-title>

              <v-flex d-flex flex-column md-6>
                <v-flex v-for="book_instance in reader_book_instances" :key="book_instance.id">
                  <v-card-text
                    elevation="2"
                    outlined
                    class="my-2"
                  >
                    <p>Название: {{ book_instance.book_instance.book.title }} </p>
                    <p>Автор: {{ book_instance.book_instance.book.author }} </p>
                    <p>Дата начала бронирования: {{ book_instance.start_date }} </p>
                    <p>Дата конца бронирования: {{ book_instance.end_date }} </p>

                    <v-col cols="3">
                      <v-btn
                        variant="text"
                        color="blue"
                        light @click.prevent="returnBook(book_instance.book_instance.id)"
                      >
                        Сдать
                      </v-btn>
                    </v-col>

                  </v-card-text>
                </v-flex>
              </v-flex>
            </v-card>
          </div>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'ReaderInfoView',
  components: {BarLayout, DefaultNavigationBar},
  data() {
    return {
      reader_book_instances: Object,
      reader: Object,
      user: Object
    }
  },
  created() {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData() {
      const get_user_response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {Authorization: `Token ${localStorage.auth_token}`}
        })
      const user = get_user_response.data
      const get_user_reader_request_url = 'http://127.0.0.1:8000/library/userreaders/' + user.id
      const get_user_reader_response = await axios.get(get_user_reader_request_url)
      const user_reader = get_user_reader_response.data
      const reader_id = user_reader.reader
      const get_reader_request_url = 'http://127.0.0.1:8000/library/readers/' + reader_id
      const get_reader_response = await axios.get(get_reader_request_url)
      const reader = get_reader_response.data
      const get_reader_books_request_url = 'http://127.0.0.1:8000/library/readerbooks/by_reader/' + reader_id
      const get_reader_books_response = await axios.get(get_reader_books_request_url)
      const reader_book_instances = get_reader_books_response.data

      this.reader_book_instances = reader_book_instances
      this.reader = reader
      this.user = user
    },

    async returnBook(book_instance_id) {
      const delete_reader_book_request_url = "http://127.0.0.1:8000/library/readerbooks/by_instance/" + book_instance_id

      await axios.delete(delete_reader_book_request_url)

      this.$router.push({name: 'Books'})
    },
    goEditReaderInfo() {
      this.$router.push({name: 'EditReader'})
    }
  }
}
</script>
