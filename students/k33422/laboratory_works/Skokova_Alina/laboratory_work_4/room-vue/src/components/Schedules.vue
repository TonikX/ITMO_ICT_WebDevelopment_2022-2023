<template>
  <div>
    <br><br>
    <b-table striped hover :items="schedules" :fields="fields" caption-top>
      <template #table-caption>Расписание уборки</template>
    </b-table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Schedules',
  data () {
    return {
      fields: [
        { key: 'id_schedule', label: '' }, 
        { key: 'id_cleaner.id_cleaner', label: 'Служащий' }, 
        { key: 'id_floor', label: 'Этаж' }, 
        { key: 'day', label: 'День недели' }, 
      ],
      schedules: '',
    }
  },
  created() {
    $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
    this.loadSchedule()
  },
  methods: {
            loadSchedule() {
                $.ajax({
                  url: 'http://127.0.0.1:8000/schedules/',
                  type: "GET",
                  success: (response) => {
                    this.schedules = response.data.data
                  },
                })
            },
        },
}
</script>


<style scoped>

</style>