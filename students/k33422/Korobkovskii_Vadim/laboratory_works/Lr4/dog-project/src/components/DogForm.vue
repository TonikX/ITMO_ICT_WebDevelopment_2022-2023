<template>
<!--  <v-form @submit.prevent>-->
<!--    <h1>Создание собаки</h1>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Кличка: </strong>-->
<!--        <input-->
<!--            v-model="dog.dog_name"-->
<!--            class="input"-->
<!--            type="text"-->
<!--            placeholder="Кличка"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Порода: </strong>-->
<!--        <select v-model="selected" label="Standard">-->
<!--          <option disabled value="">Выберите один из вариантов</option>-->
<!--          <option v-for="one_dog in breed_selector">{{ one_dog }}</option>-->
<!--        </select>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Полный возраст: </strong>-->
<!--        <input-->
<!--            v-model="dog.full_age"-->
<!--            class="input"-->
<!--            type="number"-->
<!--            placeholder="Полный возраст"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Возраст в месяцах: </strong>-->
<!--        <input-->
<!--            v-model="dog.month_age"-->
<!--            class="input"-->
<!--            type="number"-->
<!--            placeholder="Возраст в месяцах"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Номер документа: </strong>-->
<!--        <input-->
<!--            v-model="dog.document"-->
<!--            class="input"-->
<!--            type="number"-->
<!--            placeholder="Документ"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Кличка отца: </strong>-->
<!--        <input-->
<!--            v-model="dog.dad_name"-->
<!--            class="input"-->
<!--            type="text"-->
<!--            placeholder="Отец"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Кличка матери: </strong>-->
<!--        <input-->
<!--            v-model="dog.mom_name"-->
<!--            class="input"-->
<!--            type="text"-->
<!--            placeholder="Мать"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Дата последней вакцинации: </strong>-->
<!--        <input-->
<!--            v-model="dog.last_vaccination"-->
<!--            class="input"-->
<!--            type="date"-->
<!--            placeholder="Последняя вакцинация"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Информация о собаке: </strong>-->
<!--        <input-->
<!--            v-model="dog.dog_info"-->
<!--            class="input"-->
<!--            type="text"-->
<!--            placeholder="Информация о собаке"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Хозяин: </strong>-->
<!--        <input-->
<!--            v-model="dog.dog_owner"-->
<!--            class="input"-->
<!--            type="number"-->
<!--            placeholder="Идентификатор хозяина"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div style="font-size: 20px; color: royalblue">-->
<!--      <div class="t"><strong>Клуб: </strong>-->
<!--        <input-->
<!--            v-model="dog.dog_club"-->
<!--            class="input"-->
<!--            type="number"-->
<!--            placeholder="Идентификатор клуба"/>-->
<!--      </div>-->
<!--    </div>-->
<!--    <button class="btn" v-on:click="createDog">Создать</button> <br><br>-->
<!--    <button class="btn" v-on:click="goBack">Назад</button>-->
<!--  </v-form>-->
  <h1>Создание собаки</h1>
  <v-form @submit.prevent class="my-0">
    <v-row>
      <v-col class="mx-auto">
        <v-text-field
            v-model="dog.dog_name"
            label="Имя собаки"
            class="input"
            type="text"
            placeholder="Имя"/>
        <v-select
            v-model="dog.breed"
            label="Порода собаки"
            :items="breed_selector"
            placeholder="Порода"/>
        <v-text-field
            v-model="dog.full_age"
            label="Полный возраст собаки"
            class="input"
            type="number"
            placeholder="Полный возраст"/>
        <v-text-field
            v-model="dog.month_age"
            label="Возраст собаки в месяцах"
            class="input"
            type="number"
            placeholder="Возраст в месяцах"/>
        <v-text-field
            v-model="dog.document"
            label="Документ"
            class="input"
            type="number"
            placeholder="Документ"/>
        <v-text-field
            v-model="dog.dad_name"
            label="Кличка отца"
            class="input"
            type="text"
            placeholder="Отец"/>
        <v-text-field
            v-model="dog.mom_name"
            label="Кличка матери"
            class="input"
            type="text"
            placeholder="Мать"/>
        <v-text-field
            v-model="dog.last_vaccination"
            label="Дата последней вакцинации"
            class="input"
            type="date"
            placeholder="Дата"/>
        <v-text-field
            v-model="dog.dog_info"
            label="Информация о собаке"
            class="input"
            type="text"
            placeholder="Информация"/>
        <v-text-field
            v-model="dog.dog_owner"
            label="Идентификатор владельца"
            class="input"
            type="number"
            placeholder="Владелец"/>
        <v-text-field
            v-model="dog.dog_club"
            label="Идентификатор клуба"
            class="input"
            type="number"
            placeholder="Клуб"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="success" rounded="lg" @click="createDog">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="warning" rounded="lg" @click="goBack">Назад</v-btn></div>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from "axios"
export default {
  name: "DogForm",
  data () {
    return {
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
      breed_selector: ['Корги/Corgi',
      'Немецкая овчарка/German shepherd',
      'Бигль/Beagle',
      'Пудель/Poodle',
      'Ретривер/Retriever',
      'Самоед/Samoyed',
      'Доберман/Doberman']
    }
  },
  methods: {
    createDog() {
      axios.post('http://127.0.0.1:8000/dog/create/', {
        dog_name: this.dog.dog_name,
        breed: this.selected,
        full_age: this.dog.full_age,
        month_age: this.dog.month_age,
        document: this.dog.document,
        dad_name: this.dog.dad_name,
        mom_name: this.dog.mom_name,
        last_vaccination: this.dog.last_vaccination,
        dog_info: this.dog.dog_info,
        dog_owner: this.dog.dog_owner,
        dog_club: this.dog.dog_club
      })
    },
    goBack() {
      this.$router.push({ name: 'home'})
    }
  }
}
</script>

<style scoped>

</style>
