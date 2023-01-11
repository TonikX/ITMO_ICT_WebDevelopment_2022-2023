<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>{{ this.instance.book.book_name }}</h2>
<!--        <h3>{{ this.instance.id }}</h3>-->
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
          Автор: <b>{{ this.instance.book.author }}</b> <br>
          Раздел: {{ this.instance.book.section }} <br>
          Год издания: {{ this.instance.year_published }} <br>
          Издательство: {{ this.instance.publisher }} <br>
          Библиотечный номер: {{ this.instance.cypher }} <br>
          Зал: {{ this.instance.instance_hall.name }} <br>
<!--          <ul>-->
<!--            <li v-for="hall in this.book.book_hall" v-bind:key="hall" v-bind:hall="hall">-->
<!--              {{ hall.title }}-->
<!--            </li>-->
<!--          </ul>-->
<!--          <br>-->
<!--          Сейчас читают: <span v-if="!this.book.book_reader.length">-</span>-->
<!--          <ul v-else>-->
<!--            <li v-for="reader in this.book.book_reader" v-bind:key="reader" v-bind:reader="reader">-->
<!--              {{ reader.first_name }} {{ reader.last_name }}-->
<!--            </li>-->
<!--          </ul>-->
        </div>
      </v-card-text>
    </v-card>
    <v-btn v-if="!this.bookOnHold && !this.booksOnHoldOthers" color="primary" light @click="takeOutBook(instance.id)">Хочу прочитать</v-btn>

    <v-card
      elevation="2"
      outlined
      class="my-2"
      v-else-if="this.booksOnHoldOthers">
      <v-card-text>
        <div class="text--primary">К сожалению, эту книгу уже читает {{ this.WhoReads }}. Подождите немного.</div>
      </v-card-text>
    </v-card>

    <v-card
      elevation="2"
      outlined
      class="my-2"
      v-else>
      <v-card-text>
        <div class="text--primary">Вы сейчас читаете эту книгу</div>
        <a @click="returnBook(instance.id)">Вернуть книгу в библиотеку</a>
      </v-card-text>
    </v-card>

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
  name: 'Instance',
  data () {
    return {
      instance: Object,
      reader: Object,
      bookOnHold: false,
      booksOnHoldOthers: false,
      whoReads: '',
      bookReaderID: ''
    }
  },
  created () {
    this.loadBook()
    this.loadReaderData()
  },

  methods: {
    async loadBook () {
      this.instance_url = 'http://127.0.0.1:8000/lib/instances/' + this.$route.params.id
      const response = await this.axios.get(this.instance_url)
      this.instance = response.data
    },

    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
      await this.checkOnHold()
    },

    async checkOnHold () {
      this.reader_url = 'http://127.0.0.1:8000/lib/readers/' + this.reader.id
      const response = await this.axios.get(this.reader_url)
      console.log(response.data)
      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data.instances_on_hands)) {
        if (value.id === this.instance.id) {
          this.bookOnHold = true
          // this.bookReaderID = value.
          break
        }
      }
      this.book_url = 'http://127.0.0.1:8000/lib/instances/' + this.instance.id
      const response2 = await this.axios.get(this.book_url)
      console.log('Читаeт ' + response2.data.who_reads[0].name + ' человек')
      if (response2.data.who_reads.length > 0 &&
        response2.data.who_reads[0].id !== this.reader.id) {
        this.booksOnHoldOthers = true
        this.WhoReads = response2.data.who_reads[0].name
      }
    },

    takeOutBook (InstanceId) {
      this.$router.push({ name: 'take_out', params: { id: InstanceId } })
    },

    // async returnBook () {
    //   const response = await this.axios.get('http://127.0.0.1:8000/lib/reader_books/list/')
    //   // eslint-disable-next-line no-unused-vars
    //   for (const [key, value] of Object.entries(response.data)) {
    //     if (value.reader.id === this.reader.id && value.instance.id === this.instance.id) {
    //       this.bookReaderID = value.id
    //       break
    //     }
    //   }
    //   alert(this.bookReaderID)
    //   await this.$router.push({ name: 'return', params: { id: this.bookReaderID } })
    // },
    async returnBook (InstanceId) {
      // alert(InstanceId)
      const response = await this.axios.get('http://127.0.0.1:8000/lib/reader_books/list/')
      console.log('returning ' + response.data)
      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data)) {
        if (value.reader.id === this.reader.id && value.instance.id === this.instance.id) {
          this.bookReaderID = value.id
          break
        }
      }
      // alert(this.bookReaderID)
      await this.$router.push({ name: 'return', params: { id: this.bookReaderID } })
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
