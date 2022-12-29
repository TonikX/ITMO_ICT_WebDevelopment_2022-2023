<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>{{ this.book.id }}</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
          Авторы: <b>{{ this.book.authors }}</b> <br>
          Жанр: {{ this.book.genre }} <br>
          Год издания: {{ this.book.publication_year }} <br>
          Издательство: {{ this.book.publisher }} <br>
          Библиотечный номер: {{ this.book.book_cypher }} <br>
        </div>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text style="margin-top:2cm">
        <div class="text--primary">
          Дата выдачи: {{ this.issue_date }} <br>
          Срок возврата: {{ this.due_date }}
        </div>
      </v-card-text>
    </v-card>

    <v-btn style="margin-top:0.5cm" color="primary" light @click="returnBook">Вернуть</v-btn>

    <v-card>
      <v-card-text style="margin-top:2cm">
        <a @click.prevent="goCatalogue">Каталог</a><br>
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'BookReturn',

  data: () => ({
    book: Object,
    reader: Object,
    issue_date: '',
    due_date: ''
  }),

  created () {
    this.loadReaderBookData()
  },

  methods: {
    async loadReaderBookData () {
      this.book_url = 'http://127.0.0.1:8000/lib/reader_books/' + this.$route.params.id
      const response = await this.axios.get(this.book_url)
      this.book = response.data.book
      this.reader = response.data.reader
      this.issue_date = response.data.issue_date
      this.due_date = response.data.due_date
    },

    async returnBook () {
      this.return_url = 'http://127.0.0.1:8000/library/return/' + this.$route.params.id
      await this.axios.delete(this.return_url)
      alert('Вы вернули книгу в библиотеку')
      await this.$router.push({ name: 'catalogue' })
    },

    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goHome () {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style>
</style>
