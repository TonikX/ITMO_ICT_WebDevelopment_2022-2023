<template>
    <div class="object" v-for="object in dog" :key="object.id">
      <h1>Dog with ID {{ object.id }}</h1>
      <div><strong>Name: </strong> {{ object.name }}</div>
      <div><strong>Breed: </strong> {{ object.breed }}</div>
      <div><strong>Age: </strong> {{ object.full_age }}</div>
      <div><strong>Months: </strong> {{ object.month_age }}</div>
      <div><strong>Document: </strong> {{ object.document }}</div>
      <div><strong>Vaccination data: </strong> {{ object.last_vaccination }}</div>
      <div><strong>Owner Id: </strong> {{ object.owner.id }}</div>
      <div><strong>Owner: </strong> {{object.owner.surname}} {{object.owner.name}} {{object.owner.patronymic}}</div>
      <div><strong>Club ID: </strong> {{ object.club.id }}</div>
      <div><strong>Club name: </strong> {{ object.club.name }}</div>
      <div class="d-flex align-center flex-column flex-md-row">
        <v-btn variant="tonal" rounded="pill" @click="$router.push(`/dog/${object.id}/`)">Edit</v-btn></div>
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