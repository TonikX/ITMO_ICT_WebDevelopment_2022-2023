<template>
  <div>
    <h1>Регистрация</h1>
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
                <b-form-input type="text"  v-model="password"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Фамилия:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="tel"  v-model="last_name"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Имя:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="email"  v-model="first_name"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Электронная почта:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="email"  v-model="email"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Телефон:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="email"  v-model="tel"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="setUser">Готово</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'Register',
    data() {
            return {
                username: '',
                password: '',
                first_name: '',
                last_name: '',
                tel: '',
                email: '',
            }
        },
    methods: {
            setUser() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password,
                        first_name: this.first_name,
                        last_name: this.last_name,
                        tel: this.tel,
                        email: this.email,
                    },
                    success: (response) => {
                        alert("Регистрация прошла успешно!")
                        this.$router.push({name: 'home'})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Данные введены некорректно")
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