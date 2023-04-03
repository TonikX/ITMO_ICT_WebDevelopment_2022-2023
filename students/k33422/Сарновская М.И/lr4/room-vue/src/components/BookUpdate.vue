<template>
  <div>
    <h1>Выселить гостя</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <b-container fluid>
    <b-row class="my-1">
            <b-col sm="2">
                <label>Номер бронирования:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="id_booking"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Дата выселения:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="date"  v-model="date_end"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="updateBook">Готово</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'BookUpdate',
    data() {
            return {
                id_booking: '',
                date_end: '',
            }
        },
    methods: {
            updateBook() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/bookings/'+this.id_booking+'',
                    type: "PATCH",
                    data: {
                        date_end: this.date_end,
                    },
                    success: (response) => {
                        alert("Клиент выселен!")
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