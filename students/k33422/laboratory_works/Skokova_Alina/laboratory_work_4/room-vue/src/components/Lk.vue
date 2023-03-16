<template>
  <div>
    <h1>Личный кабинет</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <p>Здравствуйте, <b>{{me.username}}</b>! Для изменения личных данных скорректируйте значения полей и нажмите "Редактировать".</p>
    <b-container fluid>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Имя:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="me.first_name"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Фамилия:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="me.last_name"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Телефон:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="tel"  v-model="me.tel"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Почта:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="email"  v-model="me.email"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="updateLk">Редактировать</b-button>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Lk',
  data () {
    return {
      me: '',
    }
  },
  created() {
    $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
    this.loadMe()
  },
  methods: {
            loadMe() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/me/",
                    type: "GET",
                    success: (response) => {
                        this.me = response.data.attributes
                    }
                })
            },
            updateLk() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/me/",
                    type: "PATCH",
                    data: {
                        first_name: this.me.first_name,
                        last_name: this.me.last_name,
                        email: this.me.email,
                        tel: this.me.tel,
                    },
                    success: (response) => {
                        alert("Данные обновлены!")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные некорректны")
                        }
                    }
                })
            },
            goHome() {
                this.$router.push({name: 'home'})
            },
        },
        
}
</script>


<style scoped>

</style>