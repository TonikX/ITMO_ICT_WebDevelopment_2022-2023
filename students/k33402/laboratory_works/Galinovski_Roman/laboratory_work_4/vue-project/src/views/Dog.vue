<template>
    <div class="app">
      <h1>About dog's</h1>
      <div class="d-flex align-center flex-column flex-md-row">
        <v-btn variant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
      <dog-list v-bind:dog="dog"/>
    </div>
  
  </template>
  <script>
  import DogList from "@/components/DogList.vue";
  import axios from "axios";
  export default {
    components: {
      DogList,
    },
    data() {
      return {
        dog: [],
      }
    },
    methods: {
      async fetchDogs() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/dog/')
          console.log(response.data)
          this.dog = response.data
        } catch (e) {
          alert('Error')
        }
      },
      goBack() {
        this.$router.push({ name: 'home'})
      }
    },
    mounted() {
      this.fetchDogs()
    }
  }
  </script>