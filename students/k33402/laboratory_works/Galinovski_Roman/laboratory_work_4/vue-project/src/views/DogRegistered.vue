<template>
    <div class="app">
      <h1>Info about Registered Dog</h1>
      <div class="d-flex align-center flex-column flex-md-row">
        <v-btn variant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
      <dog-registered-list v-bind:dog_registered="dog_registered"/>
    </div>
  </template>
  <script>
  import DogRegisteredList from "@/components/DogRegisteredList.vue";
  import DogList from "@/components/DogList.vue"
  import axios from "axios";
  export default {
    components: {
      DogRegisteredList,
      DogList
    },
    data() {
      return {
        dog_registered: [],
      }
    },
    methods: {
      async fetchRegDogs() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/dog_reg/')
          console.log(response.data)
          this.dog_registered = response.data
        } catch (e) {
          alert('Error')
        }
      },
      goBack() {
        this.$router.push({name: 'home'})
      }
    },
    mounted() {
      this.fetchRegDogs()
    }
  }
  </script>