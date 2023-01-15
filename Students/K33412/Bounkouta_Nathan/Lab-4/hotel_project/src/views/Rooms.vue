<template>
  <div>
    <br>
    <slider :width="300" format="push" direction="right"
            :opacity="0.15"
            :links="[{'id': 1, 'text': 'Главная', 'url': '/main'},
                     {'id': 2, 'text': 'Бронь', 'url': '/bookings/create/'},
                     {'id': 3, 'text': 'Гости', 'url': '/clients/'},
                     {'id': 4, 'text': 'Список бронирований', 'url': '/bookings/'},
                     {'id': 5, 'text': 'Наши сотрудники', 'url': '/employees/'},
                     {'id': 6, 'text': 'Выйти', 'url': '/logout/'}]"
    >
    </slider>
    <div align="center">
      <b-table>
        <h2 class="display-1 font-weight-bold mb-3">Комнаты 🏨</h2>
        <br>
        <tr>
          <td><strong>Номер комнаты</strong></td>
          <td><strong>Тип</strong></td>
          <td><strong>Номер телефона</strong></td>
          <td><strong>Цена</strong></td>
          <td><strong>Гости</strong></td>
          <td><strong>Этаж</strong></td>
        </tr>
        <tr v-for="elem in rooms" :key="elem.id">
          <td>{{ elem.number }}</td>
          <td>{{ elem.type }}</td>
          <td>{{ elem.phone }}</td>
          <td>{{ elem.price }}</td>
          <td>{{ elem.client_in }}</td>
          <td>{{ elem.floor }}</td>
          <td>
            <v-btn color="secondary" @click='$router.push(`/rooms/update/${ elem.id }/`)'>Редактировать</v-btn>
          </td>
          <td>
            <v-btn color="accent" @click="deleteElem(elem.id)">Удалить</v-btn>
          </td>
        </tr>
      </b-table>
      <br>
      <v-col>
        <v-btn color="primary" @click='$router.push("/rooms/create/")'>Добавить комнату</v-btn>
      </v-col>
    </div>
  </div>
</template>

<script>
import Slider from '@jeremyhamm/vue-slider'
export default {
  name: 'Rooms',
  components: {
    slider: Slider
  },
  data: () => ({
    rooms: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/hotels/rooms/')
      .then((res) => {
        this.rooms = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/hotels/rooms/update/${elem}/`)
        .then((res) => {
          console.log(res)
          this.$router.go(0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
  td {
    text-align: left;
    padding: 0.8rem;
  }
</style>