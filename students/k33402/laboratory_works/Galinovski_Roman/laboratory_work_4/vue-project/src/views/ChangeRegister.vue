<template>
    <section class="page-content text-center">
      <app-header />
      <register-change-form v-bind:dog_id="dog_id"/>
    </section>
  </template>
  <script>
  import AppHeader from "../components/AppHeader"
  import RegisterChangeForm from "../components/RegisterChangeForm.vue"
  export default {
    name: "ChangeRegister",
    components: {
      AppHeader,
      RegisterChangeForm,
    },
    data() {
    return {
      dog: [],
      dog_id: this.$route.params.id,
    }
  }
  }
  </script>
  
  <style>
  html,
  body {
    height: 100%;
  }
  body {
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 40px;
  }
  #app {
    width: 100%;
    height: 100%;
  }
  .page-content {
    width: 100%;
  }
  header {
    top: 0;
    position: absolute;
    width: 100%;
  }
  </style>