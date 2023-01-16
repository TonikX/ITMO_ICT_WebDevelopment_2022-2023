<template>
  <div class="edit">
    <h2>Личный кабинет</h2>
    <h3>Добро пожаловать, {{login ()}} </h3>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <div class="text--primary">
          Имя: <b>{{ this.first_name }}</b> <br>
          Фамилия: <b>{{ this.last_name }} </b><br>
          Телефон: <b>{{ this.tel }} </b><br>
        </div><br><br>
        <a @click.prevent="goRegister" style="text-decoration: none; color: #4E342E">Зарегистрировать собаку</a> <br>
        <a @click.prevent="goGrade" style="text-decoration: none; color: #4E342E">Оценить собаку</a> <br>
        <a @click.prevent="goEdit" style="text-decoration: none; color: #4E342E">Редактировать профиль</a> <br>
        <a @click.prevent="goHome" style="text-decoration: none; color: #4E342E">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
import $ from "jquery";
export default {
  name: 'Profile',
  data () {
    return {
      userme: Object,
      first_name: '',
      last_name: '',
      tel: '',
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
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
      this.first_name = response.data.first_name
      this.last_name = response.data.last_name
      this.tel = response.data.tel
    },

    goHome () {
      this.$router.push({ name: 'home' })
    },

    goRegister () {
      this.$router.push({ name: 'regdog' })
    },

    goEdit () {
      this.$router.push({ name: 'profile_edit' })
    },

    goGrade () {
      this.$router.push({ name: 'grading' })
    },

    login () {
      return (sessionStorage.getItem('username'))
}
  }
}
</script>

<style>

</style>
