<template>
    <section class="page-content">
      <app-header />
      <register-main :dog_registered = "dog_registered"/>
    </section>
  </template>
  <script>
  import AppHeader from "../components/AppHeader"
  import RegisterMain from "../components/RegisterMain.vue"
  import axios from "axios";
  export default {
    name: "Dogs",
    components: {
      AppHeader,
      RegisterMain
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
  
  <style>
  </style>