<template>
    <div class="block-content">
      <v-simple-table class="v-data-table">
        <template v-slot:default class="theme--light">
          <thead>
          <tr>
            <th class="text-center">
              <h2>Кабинеты</h2>
            </th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="cabinet in doctors" v-bind:key="cabinet.id">
            <router-link :to="{name:'Doctor', params:{id: cabinet.id}}">
              <td>{{ cabinet.number }}</td>
            </router-link>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
    </div>
</template>
  
<script>
  import $ from 'jquery'
  export default {
    name: 'Creationlist',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        data_: ''
      }
    },
    created () {
      $.ajaxSetup({
        headers: { authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.loadCabinets()
    },
    methods: {
      loadCreations () {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/cabinets/',
          type: 'GET',
          success: (response) => {
            this.data_ = response
          },
          error: (response) => {
            alert(response)
          }
        })
      },
      goReview (creationId) {
        this.$router.push({ name: 'Review', params: { creationId: creationId } })
      },
      goNewCreation () {
        this.$router.push({ name: 'NewCreation' })
      }
    }
  }
</script>
  
<style scoped>
  .v-data-table {
    line-height: 5;
    width: 1200px;
    max-width: 100%;
  }
  .theme--light.v-data-table{
    background-color: #FFFFFF;
  }
</style>