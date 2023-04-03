<template>
  <div>
    <h1>Удалить расписание</h1>
    <b-button @click="goHome">На главную</b-button>
    <br><br><br>
    <b-container fluid>
    <b-row class="my-1">
            <b-col sm="2">
                <label>Номер расписания:</label>
            </b-col>
            <b-col sm="9">
                <b-form-input type="text"  v-model="id_schedule"></b-form-input>
            </b-col>
        </b-row>
    </b-container>
    <br>
    <b-button @click="delSched">Удалить</b-button>
  </div>
</template>

<script>
    import $ from 'jquery'

export default {
    name: 'SchedDel',
    data() {
            return {
                id_schedule: '',
            }
        },
    methods: {
            delSched() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/schedules/'+this.id_schedule+'',
                    type: "DELETE",
                    success: (response) => {
                        alert("Расписание удалено!")
                        this.$router.push({name: 'home'})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Расписание не найдено")
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