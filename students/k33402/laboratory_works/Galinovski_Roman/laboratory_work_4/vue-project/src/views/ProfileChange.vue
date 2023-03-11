<template>
<main>
    <section class="page-content">
    <app-header />
      <hr class="opacity-100 m-0 hr-jopa"/>
<section class="form-signin">
    <b-form  @submit.prevent @submit="changeProfile" class="my-2">
      <centered-heading text="Изменить Организатора" />

      <b-form-input
        v-model="profileChangeForm.surname"
        labelText="Surname"
        class="input"
        type="text"
        placeholder="Surname"/>
      <b-form-input
      v-model="profileChangeForm.name"
      labelText="Name"
      class="input"
      type="text"
      placeholder="Name"/>
      <b-form-input
      v-model="profileChangeForm.patronymic"
      labelText="Patronymic"
      class="input"
      type="text"
      placeholder="Patronymic"/>
      <b-form-input
      v-model="profileChangeForm.phone_number"
      labelText="Phone"
      class="input"
      type="text"
      placeholder="Phone"/>
      <b-form-input
      v-model="profileChangeForm.passport"
      labelText="Passport"
      class="input"
      type="number"
      placeholder="Passport"/>
      <b-form-input
      v-model="profileChangeForm.mail"
      labelText="E-mail"
      class="input"
      type="email"
      placeholder="E-mail"/>

      <big-button text="Добавить участника" />
    </b-form>
    </section>
</section>
</main>
</template>

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
  .form-signin {
    max-width: 330px;
    padding: 15px;
    margin: auto;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  </style>

  <script>
    import axios from "axios";
    import AppHeader from "../components/AppHeader"
    import BigButton from "../components/BigButton.vue"
  export default {
    name: 'ProfileChange',
    components: {
      AppHeader,
      BigButton,
    },
    data: () => ({
      profileChangeForm: {
        surname: '',
        name: '',
        patronymic: '',
        phone_number: '',
        passport: '',
        mail: ''
      }
    }),
    methods: {
      async loadOrganizerData() {
        const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
        console.log(response.data)
        this.profileChangeForm.surname = response.data.surname
        this.profileChangeForm.name = response.data.name
        this.profileChangeForm.patronymic = response.data.patronymic
        this.profileChangeForm.phone_number = response.data.phone_number
        this.profileChangeForm.passport = response.data.passport
        this.profileChangeForm.mail = response.data.mail
      },
      changeProfile() {
        axios.patch(`http://127.0.0.1:8000/auth/users/me/`, {
          surname: this.profileChangeForm.surname,
          name: this.profileChangeForm.name,
          patronymic: this.profileChangeForm.patronymic,
          phone_number: this.profileChangeForm.phone_number,
          passport: this.profileChangeForm.passport,
          mail: this.profileChangeForm.mail,
        }, {
          headers: {
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
        this.$router.push({ name: 'profile' })
      },
    },
    mounted() {
      this.loadOrganizerData()
    }
  }
</script>