<template>
  <div class="report-wrapper d-flex justify-content-start mt-4 p-4">
    <div class="report-header">
      <h3>Выберите квартал</h3>
      <form type="submit" class="mt-4" @submit.prevent="generateReport">
        <input type="radio" name="quarter" :value="1" v-model="selectedValue">
        <label>1-й (Январь-Март)</label>
        <br>
        <input type="radio" name="quarter" :value="2" v-model="selectedValue">
        <label>2-й (Апрель-Июнь)</label>
        <br>
        <input type="radio" name="quarter" :value="3" v-model="selectedValue">
        <label>3-й (Июль-Сентябрь)</label>
        <br>
        <input type="radio" name="quarter" :value="4" v-model="selectedValue">
        <label>4-й (Октрябрь-Декабрь)</label>
        <br>
        <button class="btn btn-success mt-3" type="submit">Сгенерировать</button>
      </form>
    </div>
    <div class="report-body" v-if="report">
      <h3>Отчет за {{ selectedValue }}-й квартал</h3>
      <h4>Комнаты:</h4>
      <table>
        <tr class="">
          <th scope="col" width="25%">Номер</th>
          <th scope="col" width="50%">Бронирования</th>
          <th scope="col" width="25%">Профит</th>
        </tr>
        <tr v-for="room in report.rooms">
          <td>{{ room.number }}</td>
          <td>{{ room.count }}</td>
          <td>₽ {{ room.profit }}</td>
        </tr>
      </table>
      <h4>Этажи:</h4>
      <table>
        <tr class="">
          <th scope="col" width="50%">Этаж</th>
          <th scope="col" width="50%">Кол-во комнат</th>
        </tr>
        <tr v-for="floor in report.floors">
          <td>{{ floor.floor }}</td>
          <td>{{ floor.count }}</td>
        </tr>
      </table>
      <h4>
        Общий профит:
      </h4>
      <h5>₽ {{ report.profit }}</h5>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'report',
  data() {
    return {
      selectedValue: null,
      report: null
    }
  },
  methods: {
    async generateReport() {
      if (this.selectedValue < 2) {
        this.report = (await axios.get(`http://localhost:8000/hotels/report/${this.selectedValue}`)).data
      } else {
        this.report = null
        alert('Пока отчет не доступен')
      }
    }
  },
}
</script>

<style scoped>
.report-header {
  margin-right: 300px;
}

input {
  margin-bottom: 20px;
  margin-right: 10px;
}

h4 {
  margin-top: 30px;
}
</style>