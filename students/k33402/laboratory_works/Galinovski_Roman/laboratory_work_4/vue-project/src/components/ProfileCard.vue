<template>
    <div class="container-md booking-item">
      <p>Фамилия: {{ surname }}</p>
      <p>Имя: {{ name }}</p>
      <p>Отчество: {{ patronymic }}</p>
      <p>Телефон: {{ phone }}</p>
      <p>Пасспорт: {{ passport }}</p>
      <p>E-mail: {{ email }}</p>
      <b-form  @submit="$router.push(`/profile/change/`)">
        <big-button text="Изменить" />
      </b-form>
      </div>
  </template>
  <script>
  import BigButton from "./BigButton.vue"
  export default {
    name: "ProfileCard",
    props: {
      surname: String,
      name: String,
      patronymic: String,
      phone: Number,
      passport: Number,
      email: String,
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