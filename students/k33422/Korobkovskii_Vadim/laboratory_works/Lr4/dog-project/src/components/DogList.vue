<template>
  <div class="object" v-for="object in dog" :key="object.id">
    <h1>Собака с ID {{ object.id }}</h1>
    <div><strong>Кличка: </strong> {{ object.dog_name }}</div>
    <div><strong>Порода: </strong> {{ object.breed }}</div>
    <div><strong>Полный возраст: </strong> {{ object.full_age }}</div>
    <div><strong>Возраст в месяцах: </strong> {{ object.month_age }}</div>
    <div><strong>Номер документа: </strong> {{ object.document }}</div>
    <div><strong>Кличка отца: </strong> {{ object.dad_name }}</div>
    <div><strong>Кличка матери: </strong> {{ object.mom_name }}</div>
    <div><strong>Дата последней вакцинации: </strong> {{ object.last_vaccination }}</div>
    <div><strong>Информация о собаке: </strong> {{ object.dog_info }}</div>
    <div><strong>Идентификатор хозяина: </strong> {{ object.dog_owner.id }}</div>
    <div><strong>ФИО хозяина: </strong> {{object.dog_owner.owner_surname}} {{object.dog_owner.owner_name}} {{object.dog_owner.owner_patronymic}}</div>
    <div><strong>Идентификатор клуба: </strong> {{ object.dog_club.id }}</div>
    <div><strong>Название клуба: </strong> {{ object.dog_club.name }}</div>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/dog/${object.id}/`)">Изменить</v-btn></div>
    <div><strong>------------------------------------------------------------------------</strong></div>
  </div>
</template>

<script>
import $ from "jquery"
export default {
  name: "DogList",
  props: {
    dog: {
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
