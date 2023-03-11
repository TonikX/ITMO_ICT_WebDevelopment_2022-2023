<template>
    <div class="container-md booking-item">
      <h3>{{ id }}</h3>
      <p>№ Выступления: {{ showNum }}</p>
      <p>Статус: {{ status }}</p>
      <p>Дата регистрации: {{ redDate }}</p>
      <p>Оплата: {{ bill }}</p>
      <p>Медосмотр: {{ checkup }}</p>
      <p>Дата медосмотра: {{ checkupDate }}</p>
      <p>ID собаки: {{ dogID }}</p>
      <p>Имя собаки: {{ dogName }}</p>
      <p>Клуб собаки: {{ clubID }}</p>
      <p>Название клуба: {{ clubName }}</p>
      <p>ID выступления: {{ showID }}</p>
      <p>Название выступления: {{ showName }}</p>
      <p>Начало: {{ beginDate }}</p>
      <p>Медаль: {{ medal }}</p>
      <b-form  @submit="$router.push(`/dog_reg/${id}/`)">
        <big-button text="Изменить" />
        </b-form>
      </div>
  </template>
  <script>
  import BigButton from "./BigButton.vue"
  export default {
    name: "RegisterCard",
    props: {
      id: String,
      showNum: String,
      status: String,
      redDate: Number,
      bill: Number,
      checkup: String,
      checkupDate: String,
      dogID: String,
      dogName: String,
      clubID: String,
      clubName: String,
      showID: String,
      showName: String,
      beginDate: String,
      medal: String,
    },
    components: {
      BigButton
    },
  }
  </script>
  <style>
  .booking-item {
    padding: 20px;
    border: 2px solid var(--accent-color);
    margin: 30px auto 0px;
    border-radius: 7px;
  }
  .booking-img {
    width: 50%;
    padding: 25px 0px;
  }
  </style>