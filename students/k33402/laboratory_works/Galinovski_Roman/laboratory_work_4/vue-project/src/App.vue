
<template>
  <div class="app">
    <router-view/>
  </div>
</template>

<script>
  import $ from "jquery"
  export default {
    name: "App",
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, "Arial Black", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing:  grayscale;
    /*text-align: center;*/
    /*color: #2c3e50;*/
    margin-top: 60px;
  }
</style>