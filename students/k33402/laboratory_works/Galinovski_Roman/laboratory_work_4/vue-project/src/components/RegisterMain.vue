<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <div class="dogp" v-for="dogp in dog_registered" :key="dogp.id">
      <register-card 
      v-bind:id="dogp.id"
      v-bind:showNum="dogp.show_dog_number"
      v-bind:status="dogp.status"
      v-bind:redDate="dogp.dateof_reg_dog"
      v-bind:bill="dogp.bill"
      v-bind:checkup="dogp.checkup"
      v-bind:checkupDate="dogp.dateof_checkup"
      v-bind:dogID ="dogp.participant_dog.id"
      v-bind:dogName = "dogp.participant_dog.name"
      v-bind:clubID = "dogp.participant_dog.club.id"
      v-bind:clubName = "dogp.participant_dog.club.name"
      v-bind:showID = "dogp.show_dog.id"
      v-bind:showName = "dogp.show_dog.name"
      v-bind:beginDate = "dogp.show_dog.dateof_begin"
      v-bind:medal = "dogp.show_medal"
      />
      </div>
    </main>
  </template>
  
  <script>
  import $ from "jquery"
  import RegisterCard from "./RegisterCard.vue"
  export default {
    name: "RegisterMain",
    components: {
      RegisterCard
    },
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
  
  <style>
  </style>