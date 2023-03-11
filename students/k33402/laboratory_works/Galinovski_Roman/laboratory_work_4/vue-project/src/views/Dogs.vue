<template>
    <section class="page-content">
      <app-header />
      <dogs-main :dog = "dog"/>
    </section>
  </template>
  <script>
  import AppHeader from "../components/AppHeader"
  import DogsMain from "../components/DogsMain.vue"
  import axios from "axios";
  export default {
    name: "Dogs",
    components: {
      AppHeader,
      DogsMain
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
      }
    },
    mounted() {
      this.fetchDogs()
    }
  }
  
  </script>
  
  <style>
  </style>