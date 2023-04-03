<template>
  <div>
    <h1>Вход</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <b-container fluid>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Имя пользователя:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="username"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Пароль:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="password"  v-model="password"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="setLogin">Войти</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'Login',
    data() {
            return {
                username: '',
                password: '',
            }
        },
    methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Добро пожаловать!")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: 'home'})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Имя пользователя или пароль не верны")
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