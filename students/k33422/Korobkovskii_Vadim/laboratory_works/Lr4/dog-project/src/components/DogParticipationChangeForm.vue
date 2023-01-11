<template>
<!--  <form @submit.prevent>-->
<!--    <h1>Изменение участия собаки (запись с ID {{ $route.params.id }})</h1>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Порядковый номер: </strong>-->
<!--        <input-->
<!--            v-model="dog_participation.show_dog_number"-->
<!--            class="input"-->
<!--            type="number"-->
<!--            placeholder="Порядковый номер"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Статус участия: </strong>-->
<!--        <select v-model="dog_participation.dog_status">-->
<!--          <option disabled value="">Выберите один из вариантов</option>-->
<!--          <option v-for="one_dog in status_selector">{{ one_dog }}</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Дата регистрации собаки: </strong>-->
<!--        <input-->
<!--            v-model="dog_participation.reg_dog_date"-->
<!--            class="input"-->
<!--            type="date"-->
<!--            placeholder="Дата регистрации собаки"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Статус счета: </strong>-->
<!--        <select v-model="this.dog_participation.bill">-->
<!--          <option disabled value="">Выберите один из вариантов</option>-->
<!--          <option v-for="one_dog in bill_selector">{{ one_dog }}</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Статус медосмотра: </strong>-->
<!--        <select v-model="dog_participation.checkup">-->
<!--          <option disabled value="">Выберите один из вариантов</option>-->
<!--          <option v-for="one_dog in checkup_selector">{{ one_dog }}</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Дата прохождения медосмотра: </strong>-->
<!--        <input-->
<!--            v-model="dog_participation.checkup_date"-->
<!--            class="input"-->
<!--            type="date"-->
<!--            placeholder="Дата прохождения медосмотра"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Собака: </strong>-->
<!--        <input-->
<!--            v-model="dog_participation.participant_dog"-->
<!--            class="input"-->
<!--            type="text"-->
<!--            placeholder="Выставка"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Выставка: </strong>-->
<!--        <input-->
<!--            v-model="dog_participation.show_dog"-->
<!--            class="input"-->
<!--            type="text"-->
<!--            placeholder="Выставка"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Медаль: </strong>-->
<!--        <select v-model="this.dog_participation.show_medal">-->
<!--          <option disabled value="">Выберите один из вариантов</option>-->
<!--          <option v-for="one_dog in medal_selector">{{ one_dog }}</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    <br><br/>-->
<!--    <button class="btn" v-on:click="changeDogParticipation">Изменить</button> <br><br>-->
<!--    <button class="btn" v-on:click="goBack">Назад</button>-->
<!--  </form>-->
  <v-form @submit.prevent class="my-0">
    <h1>Изменение участия собаки (запись с ID {{ $route.params.id }})</h1>
      <v-row>
      <v-col class="mx-auto">
        <v-text-field
            v-model="dog_participation.show_dog_number"
            label="Порядковый номер собаки на выставке"
            class="input"
            type="number"
            placeholder="Прядковый номер"/>
        <v-select
            v-model="dog_participation.dog_status"
            label="Статус собаки"
            :items="status_selector"
            placeholder="Статус"/>
        <v-text-field
            v-model="dog_participation.reg_dog_date"
            label="Дата регистрации собаки"
            class="input"
            type="date"
            placeholder="Дата регистрации"/>
        <v-select
            v-model="dog_participation.bill"
            label="Статус счета"
            :items="bill_selector"
            placeholder="Статус"/>
        <v-select
            v-model="dog_participation.checkup"
            label="Статус медосмотра"
            :items="checkup_selector"
            placeholder="Статус"/>
        <v-text-field
            v-model="dog_participation.checkup_date"
            label="Дата прохождения медосмотра"
            class="input"
            type="date"
            placeholder="Дата медосмотра"/>
        <v-text-field
            v-model="dog_participation.participant_dog"
            label="Идентификатор собаки"
            class="input"
            type="number"
            placeholder="Собака"/>
        <v-text-field
            v-model="dog_participation.show_dog"
            label="Идентификатор выставки"
            class="input"
            type="number"
            placeholder="Выставка"/>
        <v-select
            v-model="dog_participation.show_medal"
            clearable
            label="Медаль за выступление"
            :items="medal_selector"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="success" rounded="lg" @click="changeDogParticipation">Изменить</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="warning" rounded="lg" @click="goBack">Назад</v-btn></div>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from "axios"
export default {
  name: "DogParticipationChangeForm",
  props: {
    dog_id: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      dog_participation: {
        show_dog_number: '',
        dog_status: '',
        reg_dog_date: '',
        bill: '',
        checkup: '',
        checkup_date: '',
        participant_dog: '',
        show_dog: '',
        show_medal: null,
      },
      status_selector: ["Участвовал/Participated",
              "Снят/Suspended",
              "Не допущен/Not allowed",
              "Неявка/Absence"],
      bill_selector: ["Оплачен/Paid",
              "Не оплачен/Not paid"],
      checkup_selector: ["Пройден/Passed",
              "Не пройден/Not passed"],
      medal_selector: ["Золото/Gold",
              "Серебро/Silver",
              "Бронза/Bronze",
              "Медаль от зрителей/Audience award"],
      dog: {
        dog_name: '',
        breed: '',
        full_age: '',
        month_age: '',
        document: '',
        dad_name: '',
        mom_name: '',
        last_vaccination: '',
        dog_info: '',
        dog_owner: '',
        dog_club: ''
      },
    }
  },
  methods: {
    async getDogParticipation() {
      const response = await axios.get(`http://127.0.0.1:8000/dog_reg/${this.dog_id}/`)
       console.log(response.data)
       this.dog_participation.show_dog_number = response.data.show_dog_number
       this.dog_participation.dog_status = response.data.dog_status
       this.dog_participation.reg_dog_date = response.data.reg_dog_date
       this.dog_participation.bill = response.data.bill
       this.dog_participation.checkup = response.data.checkup
       this.dog_participation.checkup_date = response.data.checkup_date
       this.dog_participation.participant_dog = response.data.participant_dog
       this.dog_participation.show_dog = response.data.show_dog
       this.dog_participation.show_medal = response.data.show_medal
    },
    changeDogParticipation() {
      axios.patch(`http://127.0.0.1:8000/dog_reg/${this.dog_id}/`, {
        show_dog_number: this.dog_participation.show_dog_number,
        dog_status: this.dog_participation.dog_status,
        reg_dog_date: this.dog_participation.reg_dog_date,
        bill: this.dog_participation.bill,
        checkup: this.dog_participation.checkup,
        checkup_date: this.dog_participation.checkup_date,
        participant_dog: this.dog_participation.participant_dog,
        show_dog: this.dog_participation.show_dog,
        show_medal: this.dog_participation.show_medal,
      })
    },
    goBack() {
      this.$router.push({ name: 'dog_participation'})
    }
  },
  mounted() {
    this.getDogParticipation()
  }
}
</script>

<style scoped>

</style>

