<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>Каталог библиотеки</h2>
      </v-card-title>
      <v-card-text>
        <ul>
          <li v-for="instance in instances" v-bind:key="instance" v-bind:instance="instance">
            <a @click.prevent="goBook(instance.id)">{{ instance.book.book_name }}, {{ instance.book.author }}, {{ instance.publisher }}</a>
          </li>
        </ul>
      </v-card-text>
    </v-card>
    <v-card>
      <v-card-text style="margin-top:2cm">
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Catalogue',
  data () {
    return {
      instances: ''
    }
  },

  created () {
    // $.ajaxSetup({ headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') } })
    this.loadBooks()
  },

  methods: {
    loadBooks () {
      $.ajax({
        url: 'http://127.0.0.1:8000/lib/instances/list/',
        type: 'GET',
        success: (response) => {
          this.instances = response
        }
      })
    },

    goBook (bookID) {
      this.$router.push({ name: 'instance', params: { id: bookID } })
    },

    goHome () {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style>
</style>
