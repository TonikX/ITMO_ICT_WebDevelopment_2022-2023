<template>
  <div>
    <br><br>
    <b-table striped hover :items="vacants" :fields="fields" caption-top>
      <template #table-caption>Свободные комнаты</template>
    </b-table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Vacant',
  data () {
    return {
      fields: [
        { key: 'id_room', label: '' }, 
        { key: 'room_type.room_type', label: 'Тип' }, 
        { key: 'id_floor', label: 'Этаж' }, 
        { key: 'room_type.price_daily', label: 'Цена за сутки' }, 
      ],
      vacants: '',
    }
  },
  created() {
    $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
    this.loadVacant()
  },
  methods: {
            loadVacant() {
                $.ajax({
                  url: 'http://127.0.0.1:8000/vacant/',
                  type: "GET",
                  success: (response) => {
                    this.vacants = response.data.data
                  },
                })
            },
        },
}
</script>


<style scoped>

</style>