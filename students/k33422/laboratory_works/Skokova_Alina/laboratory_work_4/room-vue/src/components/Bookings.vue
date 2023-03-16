<template>
  <div>
    <br><br>
    <b-table striped hover :items="bookings" :fields="fields" caption-top>
      <template #table-caption>Все бронирования</template>
    </b-table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Bookings',
  data () {
    return {
      fields: [
        { key: 'id_booking', label: '' }, 
        { key: 'id_client.passport', label: 'Клиент' }, 
        { key: 'id_room.id_room', label: 'Комната' }, 
        { key: 'date_start', label: 'Дата заселения' }, 
        { key: 'date_end', label: 'Дата выселения' },
      ],
      bookings: '',
    }
  },
  created() {
    $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
    this.loadBookings()
  },
  methods: {
            loadBookings() {
                $.ajax({
                  url: 'http://127.0.0.1:8000/bookings/',
                  type: "GET",
                  success: (response) => {
                    this.bookings = response.data.data
                  },
                })
            },
        },
}
</script>


<style scoped>

</style>