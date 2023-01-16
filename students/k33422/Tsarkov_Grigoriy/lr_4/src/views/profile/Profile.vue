<template>
  <div class="edit">
    <h2>Личный кабинет</h2>
    <h3>Вы авторизованы как: {{login ()}}</h3>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <div class="text--primary">
          Имя: <b>{{ this.first_name }}</b> <br>
          Фамилия: <b>{{ this.last_name }} </b><br>
          Телефон: <b>{{ this.tel }} </b><br>
        </div><br><br>
        <a @click.prevent="goRegister">Зарегистрировать участника</a> <br>
        <a @click.prevent="goScore">Оценить участника</a> <br>
        <a @click.prevent="goEdit">Редактировать профиль</a> <br>
        <a @click.prevent="goHome">На главную</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Profile',
  data () {
    return {
      first_name: '',
      last_name: '',
      tel: '',
    }
  },
  created () {
    this.loadInfo()
  },
  methods: {
    async loadInfo () {
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
      this.$router.push({ name: 'reg' })
    },

    goScore () {
      this.$router.push({ name: 'scoring' })
    },

    goEdit () {
      this.$router.push({ name: 'edit' })
    },

    login () {
      return (sessionStorage.getItem('username'))
    }
  }
}
</script>

<style>

</style>
