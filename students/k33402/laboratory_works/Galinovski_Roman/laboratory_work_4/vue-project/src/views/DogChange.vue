<template>
    <div class="app">
      <dog-change-form v-bind:dog_id="id"/>
    </div>
  </template>
  <script>
  import DogChangeForm from "@/components/DogChangeForm.vue";
  import axios from "axios";
  export default {
    components: {
      DogChangeForm
    },
    data() {
      return {
        dog: [],
        id: this.$route.params.id,
      }
    }
  }
  </script>