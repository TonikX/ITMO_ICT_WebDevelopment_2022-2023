<template>
      <h1>Edit dog data with ID {{ $route.params.id }}</h1>
      <v-form @submit.prevent class="my-0">
        <v-row>
          <v-col class="mx-auto">
            <v-text-field
                v-model="dog.dog_name"
                label="Dog name"
                class="input"
                type="text"
                placeholder="Name"/>
            <v-select
                v-model="dog.breed"
                label="Dog breed"
                :items="breed_selector"
                placeholder="Breed"/>
            <v-text-field
                v-model="dog.full_age"
                label="Full age"
                class="input"
                type="number"
                placeholder="Full age"/>
            <v-text-field
                v-model="dog.month_age"
                label="Age in Month"
                class="input"
                type="number"
                placeholder="Age in Month"/>
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
                v-model="dog.dog_owner"
                label="ID Owner"
                class="input"
                type="number"
                placeholder="Owner"/>
            <v-text-field
                v-model="dog.dog_club"
                label="Club ID"
                class="input"
                type="number"
                placeholder="Club"/>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" rounded="pill" @click="changeDog">Edit</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
          </v-col>
        </v-row>
      </v-form>
    </template>
    
    <script>
    import axios from "axios"
    export default {
      name: "DogChangeForm",
      props: {
        dog_id: {
          type: Number,
          required: true
        }
      },
      data () {
        return {
          dog: {
            dog_name: '',
            breed: '',
            full_age: '',
            month_age: '',
            document: '',
            dad_name: '',
            mom_name: '',
            last_vaccination: '',
            dog_info: null,
            dog_owner: '',
            dog_club: ''
          },
          breed_selector: ['Achihuahua',
          'Apchihuahua',
          'Pudel',
          'Sobaka',
          'Dobel',
          'Ovcharka',
          'Doberman']
        }
      },
      methods: {
        async getDog() {
          const response = await axios.get(`http://127.0.0.1:8000/dog/${this.dog_id}/`)
          console.log(response.data)
          this.dog.dog_name = response.data.dog_name
          this.dog.breed = response.data.breed
          this.dog.full_age = response.data.full_age
          this.dog.month_age = response.data.month_age
          this.dog.document = response.data.document
          this.dog.dad_name = response.data.dad_name
          this.dog.mom_name = response.data.mom_name
          this.dog.last_vaccination = response.data.last_vaccination
          this.dog.dog_info = response.data.dog_info
          this.dog.dog_owner = response.data.dog_owner
          this.dog.dog_club = response.data.dog_club
        },
        changeDog() {
          axios.patch(`http://127.0.0.1:8000/dog/${this.dog_id}/`, {
            dog_name: this.dog.dog_name,
            breed: this.dog.breed,
            full_age: this.dog.full_age,
            month_age: this.dog.month_age,
            document: this.dog.document,
            dad_name: this.dog.dad_name,
            mom_name: this.dog.mom_name,
            last_vaccination: this.dog.last_vaccination,
            dog_info: this.dog.dog_info,
            dog_owner: this.dog.dog_owner,
            dog_club: this.dog.dog_club,
          })
        },
        goBack() {
          this.$router.push({ name: 'dogs'})
        }
      },
      mounted() {
        this.getDog()
      }
    }
    </script>
    
    <style scoped>
    </style>