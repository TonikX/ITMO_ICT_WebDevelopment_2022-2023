<template>
  <div>
    <br>
    <slider :width="300" format="push" direction="right"
            :opacity="0.15"
            :links="[{'id': 1, 'text': 'Главная', 'url': '/main'&rbrace;,
                     {'id': 2, 'text': 'Комнаты', 'url': '/rooms/'},
                     {'id': 3, 'text': 'Гости', 'url': '/clients/'},
                     {'id': 4, 'text': 'Бронь', 'url': '/bookings/create/'},
                     {'id': 5, 'text': 'Наши сотрудники', 'url': '/employees/'},
                     {'id': 6, 'text': 'Выйти', 'url': '/logout/'}]"
    >
    </slider>
    <div align="center">
      <b-table>
        <h2 class="display-1 font-weight-bold mb-3">Список бронирований 📃</h2>
        <br>
        <tr>
          <td><strong>Комната</strong></td>
          <td><strong>Гость</strong></td>
          <td><strong>Дата заселения</strong></td>
          <td><strong>Дата выселения</strong></td>
        </tr>
        <tr v-for="elem in bookings" :key="elem.id">
          <td>{{ elem.room }}</td>
          <td>{{ elem.client }}</td>
          <td>{{ elem.check_in }}</td>
          <td>{{ elem.check_out }}</td>
        </tr>
      </b-table>
      <br>
      <v-col>
        <v-btn color="primary" @click='$router.push("/bookings/create/")'>Добавить бронь</v-btn>
      </v-col>
    </div>
  </div>
</template>

<script>
import Slider from '@jeremyhamm/vue-slider'
export default {
  name: 'Bookings',
  components: {
    slider: Slider
  },
  data: () => ({
    bookings: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/hotels/bookings/')
      .then((res) => {
        this.bookings = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>
  td {
    text-align: left;
    padding: 0.8rem;
  }
</style>