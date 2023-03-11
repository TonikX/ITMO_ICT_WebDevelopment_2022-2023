<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <section class="form-signin">
      <b-form  @submit.prevent @submit="changeDog" class="my-2">
        <centered-heading text="Редактирование собаки" />
  
        <b-form-input
          v-model="dog.name"
          labelText="Dog name"
          class="input"
          type="text"
          placeholder="Dog name"/>
        <b-form-select 
          v-model="dog.breed" :options="breeds"
          labelText="Breed"/>
        <b-form-input
        v-model="dog.full_age"
        labelText="Full age"
        class="input"
        type="text"
        placeholder="Full age"/>
        <b-form-input
        v-model="dog.month_age"
        labelText="Age in month"
        class="input"
        type="text"
        placeholder="Age in month"/>
        <b-form-input
        v-model="dog.document"
        labelText="Document"
        class="input"
        type="text"
        placeholder="Document"/>
        <b-form-input
        v-model="dog.last_vaccination"
        labelText="Vaccination date"
        class="input"
        type="date"
        placeholder="Vaccination date"/>
        <b-form-input
        v-model="dog.owner"
        labelText="Owner ID"
        class="input"
        type="number"
        placeholder="Owner ID"/>
        <b-form-input
        v-model="dog.club"
        labelText="Club ID"
        class="input"
        type="number"
        placeholder="Club ID"/>
        <big-button text="Добавить собаку" />
      </b-form>
      </section>
    </main>
  </template>
  
  <script>
  import axios from "axios"
  import CenteredHeading from "./CenteredHeading.vue"
  import CenteredFormInput from "./CenteredFormInput.vue"
  import Checkbox from "./Checkbox.vue"
  import BigButton from "./BigButton.vue"
  export default {
    name: "DogChangeForm",
    components: {
      CenteredHeading,
      CenteredFormInput,
      Checkbox,
      BigButton
    },
      props: {
        dog_id: {
          type: Number,
          required: true
        }
      },
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
        async getDog() {
          const response = await axios.get(`http://127.0.0.1:8000/dog/${this.dog_id}/`)
          console.log(response.data)
          this.dog.name = response.data.name
          this.dog.breed = response.data.breed
          this.dog.full_age = response.data.full_age
          this.dog.month_age = response.data.month_age
          this.dog.document = response.data.document
          this.dog.last_vaccination = response.data.last_vaccination
          this.dog.owner = response.data.owner
          this.dog.club = response.data.club
        },
        changeDog() {
          axios.patch(`http://127.0.0.1:8000/dog/${this.dog_id}/`, {
            name: this.dog.name,
            breed: this.dog.breed,
            full_age: this.dog.full_age,
            month_age: this.dog.month_age,
            document: this.dog.document,
            last_vaccination: this.dog.last_vaccination,
            owner: this.dog.owner,
            club: this.dog.club,
          })
        }
      },
      mounted() {
        this.getDog()
      }
    }
  </script>
  
  <style>
  .form-signin {
    max-width: 400px;
    padding: 15px;
    margin: auto;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  #registerPasswordInput {
    margin-bottom: -1px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  #rePasswordInput {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  </style>
  