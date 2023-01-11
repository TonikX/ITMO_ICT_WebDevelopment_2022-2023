<template>
  <div class="dogp" v-for="dogp in dog_participation" :key="dogp.id">
    <h1>Запись с ID {{ dogp.id }}</h1>
    <div><strong>Порядковый номер на выставке: </strong> {{ dogp.show_dog_number }}</div>
    <div><strong>Статус участия: </strong> {{ dogp.dog_status }}</div>
    <div><strong>Дата регистрации собаки: </strong> {{ dogp.reg_dog_date }}</div>
    <div><strong>Статус счёта: </strong> {{ dogp.bill }}</div>
    <div><strong>Статус медосмотра: </strong> {{ dogp.checkup }}</div>
    <div><strong>Дата прохождения медосмотра: </strong> {{ dogp.checkup_date }}</div>
    <div><strong>Идентификатор собаки: </strong> {{ dogp.participant_dog.id }}</div>
    <div><strong>Кличка собаки: </strong> {{ dogp.participant_dog.dog_name }}</div>
    <div><strong>Клуб собаки: </strong> {{ dogp.participant_dog.dog_club.id }}</div>
    <div><strong>Название клуба: </strong> {{ dogp.participant_dog.dog_club.name }}</div>
    <div><strong>Идентификатор выставки: </strong> {{ dogp.show_dog.id }}</div>
    <div><strong>Название выставки: </strong> {{ dogp.show_dog.name }}</div>
    <div><strong>Начало выставки: </strong> {{ dogp.show_dog.begin_date }}</div>
    <div><strong>Медаль: </strong> {{ dogp.show_medal }}</div>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/dog_reg/${dogp.id}/`)">Изменить</v-btn></div>
    <div><strong>------------------------------------------------------------------------</strong></div>
  </div>
</template>

<script>
import $ from "jquery"
export default {
  name: "DogPartiipationList",
  props: {
    dog_participation: {
      type: Array,
      required: true
    },
  },
  created() {
    $.ajaxSetup({
      headers: {'Authorization': "Token" + sessionStorage.getItem('auth_token')}
    })
  },
}
</script>

<style scoped>

</style>
