<template>
    <div class="app">
      <dog-registered-change-form v-bind:dog_id="id"/>
    </div>
  </template>
  <script>
  import DogRegisteredChangeForm from "@/components/DogRegisteredChangeForm.vue";
  import axios from "axios";
  export default {
    components: {
      DogRegisteredChangeForm
    },
    data() {
      return {
        dog_registered: [],
        id: this.$route.params.id,
      }
    }
  }
  </script>