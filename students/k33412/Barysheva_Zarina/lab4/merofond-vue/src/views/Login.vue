<template>
  <span>
    <Navbar></Navbar>
    <div class="container-fluid">
      <br />
      <div class="row d-flex justify-content-center">
        <div class="col-xs-2 col-md-6 col-sm-6 col-lg-4 align-self-center">
          <div class="p-3 border bg-white text-center">
            <p class="fs-2">Вход</p>
          </div>
          <div class="p-3 border bg-white">
            <LoginComp />
          </div>
        </div>
      </div>
    </div>
  </span>
</template>
  
  <script>
  import LoginComp from "../components/LoginComp.vue";
  import Navbar from "../components/Navbar.vue";
  
  export default {
    components: { LoginComp, Navbar },
  };
  </script>
  
  <style scoped>
  /* .col-custom {
    min-width: inherit;
  } */
  </style>