<template>
  <div>
    <h1>Добавить расписание</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <b-container fluid>
    <b-row class="my-1">
            <b-col sm="2">
                <label>Номер служащего:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="id_cleaner"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>Этаж:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="id_floor"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="my-1">
            <b-col sm="2">
                <label>День недели:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="day"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="createSched">Готово</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'Sched',
    data() {
            return {
                id_cleaner: '',
                id_floor: '',
                day: '',
            }
        },
    methods: {
            createSched() {
                $.ajax({
                    url: "http://127.0.0.1:8000/schedules/",
                    type: "POST",
                    data: {
                        id_cleaner: this.id_cleaner,
                        id_floor: this.id_floor,
                        day: this.day,
                    },
                    success: (response) => {
                        alert("Расписание добавлено!")
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