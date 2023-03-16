<template>
  <div>
    <h1>Заселить гостя</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <b-container fluid>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Номер клиента:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="id_client"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Номер комнаты:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="id_room"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Дата заселения:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="date"  v-model="date_start"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="createBook">Готово</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'Book',
    data() {
            return {
                id_client: '',
                id_room: '',
                date_start: '',
            }
        },
    methods: {
            createBook() {
                $.ajax({
                    url: "http://127.0.0.1:8000/bookings/",
                    type: "POST",
                    data: {
                        id_client: this.id_client,
                        id_room: this.id_room,
                        date_start: this.date_start,
                    },
                    success: (response) => {
                        alert("Клиент заселен!")
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