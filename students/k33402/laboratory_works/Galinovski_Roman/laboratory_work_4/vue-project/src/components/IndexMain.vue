<template>
    <main>
      <template v-if="auth">
        <hr class="opacity-100 m-0 hr-jopa"/>
        <section class="px-4 py-5 my-5 text-center">
      <img class="d-block mx-auto mb-4" src="../assets/greetings.png" alt="" width="200" />
      <h1 class="display-5 fw-bold"> Поздравляю, вы вошли</h1>
      <p class="lead mb-4">Наверное, круто быть организатором такой крутой выставки.</p>
        </section>
        </template>
        <template v-else>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <section class="px-4 py-5 my-5 text-center">
      <img class="d-block mx-auto mb-4" src="../assets/sad_boy.png" alt="" width="200" />
      <h1 class="display-5 fw-bold"> Нет учетной записи?</h1>
      <p class="lead mb-4">Заведите её, чтобы начать наше сотрудничество!</p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <section class="form-signin">
          <b-form @submit="onClickListener">
      <big-button text="Зарегистрироваться"/>
    </b-form>
    </section>
    </div>
    </section>
  </template>
    </main>
  </template>
  
  <script>
  import BigButton from "./BigButton.vue"
  import Heading from "./Heading.vue"
  export default {
    name: "IndexMain",
    components: {
      Heading,
      BigButton
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        this.$router.push({
          name: "SearchResults",
          query: {
            country: document.getElementById("country").value,
            arrivalDatetime: document.getElementById("arrivalDatetime").value,
          }
        })
      },
      onClickListener() {
      this.$router.push({ name: 'Registration' })
    }
    },
    computed: {
      auth() {
         if (sessionStorage.getItem('auth_token')) {
           return true
         }
      }
    }
  }
  </script>
  
  <style>
  main {
    height: 100%;
  }
  .index-search-form {
    height: 100%;
  }
  .hr-jopa {
    border: none;
    height: 33px;
    background-color: black;
    color: black;
  }
  .hr-a{
    border: none;
    height: 2px;
    background-color: black;
    color: black;    
  }
  </style>