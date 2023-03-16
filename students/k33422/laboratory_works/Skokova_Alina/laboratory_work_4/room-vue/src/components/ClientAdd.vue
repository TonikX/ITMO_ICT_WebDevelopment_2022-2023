<template>
  <div>
    <h1>Добавить клиента</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <b-container fluid>
    <b-row class="my-1">
            <b-col sm="2">
                <label>Номер паспорта:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="passport"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Фамилия:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="last_name_client"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Имя:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="first_name_client"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Отчество:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="patronymic_client"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Город проживания:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="city"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="createClient">Готово</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'ClientAdd',
    data() {
            return {
                passport: '',
                last_name_client: '',
                first_name_client: '',
                patronymic_client: '',
                city: '',
            }
        },
    methods: {
            createClient() {
                $.ajax({
                    url: "http://127.0.0.1:8000/clients/",
                    type: "POST",
                    data: {
                        passport: this.passport,
                        last_name_client: this.last_name_client,
                        first_name_client: this.first_name_client,
                        patronymic_client: this.patronymic_client,
                        city: this.city,
                    },
                    success: (response) => {
                        alert("Клиент добавлен!")
                        this.$router.push({name: 'home'})
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