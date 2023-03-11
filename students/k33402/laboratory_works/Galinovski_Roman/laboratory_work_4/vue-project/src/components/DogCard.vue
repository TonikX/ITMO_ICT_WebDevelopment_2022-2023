<template>
    <div class="container-md booking-item">
      <h3>{{ id }}</h3>
      <p>Имя: {{ name }}</p>
      <p>Порода: {{ breed }}</p>
      <p>Лет: {{ full_age }}</p>
      <p>В месяцах: {{ month_age }}</p>
      <p>Документ: {{ document }}</p>
      <p>Последняя вакцинация: {{ last_vaccination }}</p>
      <p>ID владельца: {{ ownerID }}</p>
      <p>Имя владельца: {{ ownerSurname }} {{ ownerName }} {{ ownerPatronymic }}</p>
      <p>ID клуба: {{ clubID }}</p>
      <p>Название клуба: {{ clubName }}</p>
      <b-form  @submit="$router.push(`/dog/${id}/`)">
        <big-button text="Изменить" />
      </b-form>
      </div>
  </template>
  <script>
  import BigButton from "./BigButton.vue"
  export default {
    name: "DogCard",
    props: {
      id: String,
      name: String,
      breed: String,
      full_age: Number,
      month_age: Number,
      document: String,
      last_vaccination: String,
      ownerID: String,
      ownerName: String,
      ownerSurname: String,
      ownerPatronymic: String,
      clubID: String,
      clubName: String,
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