<template>
  <div>
    <br>
    <slider :width="300" format="push" direction="right"
            :opacity="0.15"
            :links="[{'id': 1, 'text': 'Главная', 'url': '/main'},
                     {'id': 2, 'text': 'Комнаты', 'url': '/rooms/'},
                     {'id': 3, 'text': 'Гости', 'url': '/clients/'},
                     {'id': 4, 'text': 'Бронь', 'url': '/bookings/create/'},
                     {'id': 5, 'text': 'Список бронирований', 'url': '/bookings/'},
                     {'id': 6, 'text': 'Выйти', 'url': '/logout/'}]"
    >
    </slider>
    <div align="center">
      <b-table>
        <h2 class="display-1 font-weight-bold mb-3">Сотрудники 👨‍🏭</h2>
        <br>
        <tr>
          <td><strong>Фамилия</strong></td>
          <td><strong>Имя</strong></td>
          <td><strong>Отчество</strong></td>
          <td><strong>Этаж</strong></td>
          <td><strong>День</strong></td>
        </tr>
        <tr v-for="elem in employees" :key="elem.id">
          <td>{{ elem.last_name }}</td>
          <td>{{ elem.first_name }}</td>
          <td>{{ elem.patronymic }}</td>
          <td>{{ elem.floor }}</td>
          <td>{{ elem.day }}</td>
          <td>
            <v-btn color="secondary" @click='$router.push(`/employees/update/${ elem.id }/`)'>Редактировать</v-btn>
          </td>
          <td>
            <v-btn color="accent" @click="deleteElem(elem.id)">Удалить</v-btn>
          </td>
        </tr>
      </b-table>
      <br>
      <v-col>
        <v-btn color="primary" @click='$router.push("/employees/create/")'>Добавить сотрудника</v-btn>
      </v-col>
    </div>
  </div>
</template>

<script>
import Slider from '@jeremyhamm/vue-slider'
export default {
  name: 'Employees',
  components: {
    slider: Slider
  },
  data: () => ({
    employees: []
  }),
  created () {
    this.axios
      .get('http://127.0.0.1:8000/hotels/employees/')
      .then((res) => {
        this.employees = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async deleteElem (elem) {
      await this.axios
        .delete(`http://127.0.0.1:8000/hotels/employees/update/${elem}/`)
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