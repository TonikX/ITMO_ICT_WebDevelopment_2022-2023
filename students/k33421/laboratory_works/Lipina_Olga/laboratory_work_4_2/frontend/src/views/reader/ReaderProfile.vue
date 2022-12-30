<template>
<div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Личный кабинет</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
          ФИО: <b>{{ this.reader.name }}</b> <br>
          Логин: {{ this.reader.username }} <br>
          Номер билета: {{ this.reader.library_pass }} <br>
          Дата рождения: {{ this.reader.birth_date }} <br>
          Образование: {{ this.reader.education_level }} <br>
          Ученая степень: {{ this.reader.degree ? 'есть' : 'нет' }} <br>
          Адрес: {{ this.reader.address }} <br>
          Телефон: {{ this.reader.phone_number }} <br>
        </div>
      </v-card-text>
    </v-card>

  <v-card
    elevation="2"
    outlined
    class="my-2">
    <v-card-text class="text--primary">
      Вы сейчас читаете:
      <ul>
          <li v-for="instance in reader.instances_on_hands" v-bind:key="instance" v-bind:instance="instance">
            <a @click.prevent="goBook(instance.id)">{{ instance.book.book_name }}</a>, {{ instance.book.author }}
          </li>
        </ul>
    </v-card-text>
  </v-card>

  <v-card>
    <v-card-text  style="margin-top:1cm">
      <a @click.prevent="goEdit">Редактировать профиль</a><br>
    </v-card-text>
  </v-card>

    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goCatalogue">Каталог</a><br>
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'ReaderProfile',

  data () {
    return {
      reader: Object
    }
  },

  created () {
    this.loadReaderData()
  },

  methods: {
    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
      await this.loadCurrentlyReading()
    },

    async loadCurrentlyReading () {
      this.cur_read_url = 'http://127.0.0.1:8000/lib/readers/' + this.reader.id
      const response = await this.axios.get(this.cur_read_url)
      this.reader = response.data
      console.log('hehe ' + this.reader.phone_number)
    },

    goBook (bookID) {
      this.$router.push({ name: 'instance', params: { id: bookID } })
    },

    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },

    goHome () {
      this.$router.push({ name: 'home' })
    },

    goEdit () {
      this.$router.push({ name: 'reader_profile_edit' })
    }
  }
}
</script>

<style>

</style>
