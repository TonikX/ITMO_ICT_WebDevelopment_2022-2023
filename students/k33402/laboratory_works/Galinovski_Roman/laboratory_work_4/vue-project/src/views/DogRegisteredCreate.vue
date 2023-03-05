<template>
    <div class="app">
      <dog-registered-form/>
    </div>
  </template>
  <script>
  import DogRegisteredForm from "@/components/DogRegisteredForm.vue";
  import axios from "axios";
  export default {
    components: {
      DogRegisteredForm
    },
    data() {
      return {
        dog_registered: [],
      }
    }
  }
  </script>