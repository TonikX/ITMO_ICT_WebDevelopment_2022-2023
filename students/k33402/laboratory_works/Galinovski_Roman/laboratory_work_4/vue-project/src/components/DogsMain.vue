<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <div class="object" v-for="object in dog" :key="object.id">
      <dog-card 
      v-bind:id="object.id"
      v-bind:name="object.name"
      v-bind:breed="object.breed"
      v-bind:full_age="object.full_age"
      v-bind:month_age="object.month_age"
      v-bind:document="object.document"
      v-bind:last_vaccination="object.last_vaccination"
      v-bind:ownerID ="object.owner.id"
      v-bind:ownerSurname = "object.owner.surname"
      v-bind:ownerName = "object.owner.name"
      v-bind:ownerPatronymic = "object.owner.patronymic"
      v-bind:clubID = "object.club.id"
      v-bind:clubName = "object.club.name"
      />
      </div>
    </main>
  </template>
  
  <script>
  import $ from "jquery"
  import DogCard from "./DogCard.vue"
  export default {
    name: "DogsMain",
    components: {
      DogCard
    },
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
  
  <style>
  </style>