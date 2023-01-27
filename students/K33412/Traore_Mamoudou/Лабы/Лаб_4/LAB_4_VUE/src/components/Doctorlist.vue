<template>
    <div>
      <div>
        <v-app-bar color="#653d19" dense dark>
          <v-btn icon @click="goHome">
            <v-icon>mdi-home</v-icon>
          </v-btn>
          <v-toolbar-title>Clinic</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon @click="goProfile">
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-btn icon @click="logout">
            <v-icon>mdi-exit-to-app</v-icon>
          </v-btn>
        </v-app-bar>
      </div>
      <div class="block-content">
        <v-simple-table class="v-data-table">
          <template v-slot:default class="theme--light">
            <thead>
            <tr>
              <th class="text-center">
                <h2>Врачи</h2>
              </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="doctor in doctors" v-bind:key="doctor.id">
              <router-link :to="{name:'Doctor', params:{id: doctor.id}}">
                <td>{{ doctor.last_name }} {{doctor.first_name}} {{doctor.middle_name}}</td>
              </router-link>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
</template>
  
<script>
  import $ from 'jquery'
  export default {
    name: 'Doctorlist',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        doctors: ''
      }
    },
    created () {
      $.ajaxSetup({
        headers: { authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.loadDoctors()
    },
    methods: {
      loadDoctors () {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/doctors/',
          type: 'GET',
          success: (response) => {
            this.doctors = response
          },
          error: (response) => {
            alert(response)
          }
        })
      },
      goHome () {
        this.$router.push({ name: 'Home' })
      },
      goProfile () {
        this.$router.push({ name: 'Profile' })
      },
      logout () {
        sessionStorage.removeItem('auth_token')
        window.location = '/'
      }
    }
  }
</script>
  
<style scoped>
  .block-content {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #FFFFFF; /* Цвет фона */
    padding: 10px; /* Поля вокруг текста */
  }
  .v-data-table {
    line-height: 5;
    width: 700px;
    max-width: 100%;
  }
  .theme--light.v-data-table{
    background-color: #FFD7A7;
  }
</style>