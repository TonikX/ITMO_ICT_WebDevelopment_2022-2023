<template>
    <div class="dogp" v-for="dogp in dog_registered" :key="dogp.id">
      <h1>ID {{ dogp.id }}</h1>
      <div><strong>Number of exhibition: </strong> {{ dogp.show_dog_number }}</div>
      <div><strong>Status of participation: </strong> {{ dogp.status }}</div>
      <div><strong>Date of registration: </strong> {{ dogp.dateof_reg_dog }}</div>
      <div><strong>Bill status: </strong> {{ dogp.bill }}</div>
      <div><strong>Checkup status: </strong> {{ dogp.checkup }}</div>
      <div><strong>Checkup date: </strong> {{ dogp.dateof_checkup }}</div>
      <div><strong>ID Dog: </strong> {{ dogp.participant_dog.id }}</div>
      <div><strong>Name of Dog: </strong> {{ dogp.participant_dog.name }}</div>
      <div><strong>Club of Dog: </strong> {{ dogp.participant_dog.club.id }}</div>
      <div><strong>Club name: </strong> {{ dogp.participant_dog.club.name }}</div>
      <div><strong>ID Show: </strong> {{ dogp.show_dog.id }}</div>
      <div><strong>Exhibition name: </strong> {{ dogp.show_dog.name }}</div>
      <div><strong>Date of begin: </strong> {{ dogp.show_dog.dateof_begin }}</div>
      <div><strong>Medal: </strong> {{ dogp.show_medal }}</div>
      <div class="d-flex align-center flex-column flex-md-row">
        <v-btn variant="tonal" rounded="pill" @click="$router.push(`/dog_reg/${dogp.id}/`)">Edit</v-btn></div>
      <div><strong>------------------------------------------------------------------------</strong></div>
    </div>
  </template>
  
  <script>
  import $ from "jquery"
  export default {
    name: "DogRegisteredList",
    props: {
      dog_registered: {
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