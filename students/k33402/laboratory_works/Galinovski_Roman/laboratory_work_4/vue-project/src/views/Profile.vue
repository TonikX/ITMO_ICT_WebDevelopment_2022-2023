<template>
    <section class="page-content">
      <app-header />
      <hr class="opacity-100 m-0 hr-jopa"/>
      <profile-card 
      v-bind:surname = "this.organizer.surname"
      v-bind:name = "this.organizer.name"
      v-bind:patronymic = "this.organizer.patronymic"
      v-bind:phone = "this.organizer.phone_number"
      v-bind:passport = "this.organizer.passport"
      v-bind:email = "this.organizer.mail"/>
    </section>
  </template>

<script>
import AppHeader from "../components/AppHeader"
import ProfileCard from "../components/ProfileCard.vue"
import axios from "axios";
  export default {
    name: 'Profile',
    components: {
      AppHeader,
      ProfileCard,
    },
    data () {
      return {
        organizer: Object
      }
    },
    methods: {
      async loadOrganizerData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
            headers: {
              Authorization: `Token ${sessionStorage.getItem('auth_token')}`
            }
          })
          console.log(response.data)
          this.organizer = response.data
        } catch (e) {
          alert('Error')
        }
      },
      goBack() {
        this.$router.push({ name: 'home'})
      }
    },
    mounted() {
      this.loadOrganizerData()
    }
  }
  </script>