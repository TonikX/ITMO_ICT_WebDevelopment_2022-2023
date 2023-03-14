<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>{{ this.book.book.book_name }}</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
          Авторы: <b>{{ this.book.book.author }}</b> <br>
          Жанр: {{ this.book.book.section }} <br>
          Год издания: {{ this.book.year_published }} <br>
          Издательство: {{ this.book.publisher }} <br>
          Библиотечный номер: {{ this.book.cypher }} <br>
          <br>
          <u>Дата выдачи:</u> <b>{{ new Date().getDate() }}-{{ new Date().getMonth() }}-{{ new Date().getFullYear() }}</b>
<!--          <v-text-field-->
<!--            label="Дата выдачи"-->
<!--            v-model="submitForm.issue_date"-->
<!--            name="issue_date"-->
<!--            type="date"/>-->
<!--          <v-text-field-->
<!--            label="Срок возврата"-->
<!--            v-model="submitForm.due_date"-->
<!--            name="due_date"-->
<!--            type="date"/>-->
        </div>
      </v-card-text>
    </v-card>

    <v-btn color="primary" light @click="takeOutBook">Оформить</v-btn>

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
  name: 'InstanceTake',

  data: () => ({
    book: Object,
    reader: Object,
    submitForm: {
      instance: '',
      reader: ''
      // issue_date: '',
      // due_date: ''
    }
  }),

  created () {
    this.loadReaderData()
    this.loadBook()
  },

  methods: {
    async loadBook () {
      this.book_url = 'http://127.0.0.1:8000/lib/instances/' + this.$route.params.id
      const response = await this.axios.get(this.book_url)
      this.book = response.data
    },

    async takeOutBook () {
      this.submitForm.instance = this.book.id
      this.submitForm.reader = this.reader.id
      // this.submitForm.date_register = ''

      await this.axios.post('http://127.0.0.1:8000/lib/reader_books/create/', this.submitForm)
      await this.$router.push({ name: 'instance', params: { id: this.book.id } })
    },

    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
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
