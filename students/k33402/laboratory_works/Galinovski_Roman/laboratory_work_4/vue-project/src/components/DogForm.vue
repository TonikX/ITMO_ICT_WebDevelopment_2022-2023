<template>
      <h1>Add dog</h1>
      <v-form @submit.prevent class="my-0">
        <v-row>
          <v-col class="mx-auto">
            <v-text-field
                v-model="dog.name"
                label="Dog name"
                class="input"
                type="text"
                placeholder="Name"/>
            <v-select
                v-model="dog.breed"
                label="Dog breed"
                :items="breeds"
                placeholder="Breed"/>
            <v-text-field
                v-model="dog.full_age"
                label="Full age"
                class="input"
                type="number"
                placeholder="Full age"/>
            <v-text-field
                v-model="dog.month_age"
                label="Age in month"
                class="input"
                type="number"
                placeholder="Age in month"/>
            <v-text-field
                v-model="dog.document"
                label="Document"
                class="input"
                type="number"
                placeholder="Document"/>
            <v-text-field
                v-model="dog.last_vaccination"
                label="Vaccination date"
                class="input"
                type="date"
                placeholder="Date"/>
            <v-text-field
                v-model="dog.owner"
                label="Owner ID"
                class="input"
                type="number"
                placeholder="Owner"/>
            <v-text-field
                v-model="dog.club"
                label="Club ID"
                class="input"
                type="number"
                placeholder="Club"/>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" rounded="pill" @click="createDog">Add</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
          </v-col>
        </v-row>
      </v-form>
    </template>
    
    <script>
    import axios from "axios"
    export default {
      name: "DogForm",
      data () {
        return {
          dog: {
            name: '',
            breed: '',
            full_age: '',
            month_age: '',
            document: '',
            last_vaccination: '',
            owner: '',
            club: ''
          },
          breeds: ['Achihuahua',
          'Apchihuahua',
          'Pudel',
          'Sobaka',
          'Dobel',
          'Ovcharka',
          'Doberman']
        }
      },
      methods: {
        createDog() {
          axios.post('http://127.0.0.1:8000/dog/create/', {
            name: this.dog.name,
            breed: this.selected,
            full_age: this.dog.full_age,
            month_age: this.dog.month_age,
            document: this.dog.document,
            last_vaccination: this.dog.last_vaccination,
            owner: this.dog.owner,
            club: this.dog.club
          })
        },
        goBack() {
          this.$router.push({ name: 'home'})
        }
      }
    }
    </script>
    
    <style scoped>
    </style>