<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <section class="form-signin">
      <b-form  @submit.prevent @submit="createRegister" class="my-2">
        <centered-heading text="Добавить собаку" />
  
        <b-form-input
          v-model="dog_registered.show_dog_number"
          labelText="Number of dog"
          class="input"
          type="number"
          placeholder="Number of dog"/>
        <b-form-select 
          v-model="dog_registered.dog_status" :options="status_selector"
          labelText="Dog status"
          placeholder="Dog status"/>
        <b-form-input
        v-model="dog_registered.dateof_reg_dog"
        labelText="Date of dog registration"
        class="input"
        type="date"
        placeholder="Date of dog registration"/>
        <b-form-select
        v-model="dog_registered.bill" :options="bill_selector"
        labelText="Bill status"
        placeholder="Bill status"/>
        <b-form-select 
          v-model="dog_registered.checkup" :options="checkup_selector"
          labelText="Checkup"
          placeholder="Checkup"/>
        <b-form-input
        v-model="dog_registered.dateof_checkup"
        labelText="Date of checkup"
        class="input"
        type="date"
        placeholder="Date of checkup"/>
        <b-form-input
        v-model="dog_registered.participant_dog"
        labelText="Dog ID"
        class="input"
        type="number"
        placeholder="Dog ID"/>
        <b-form-input
        v-model="dog_registered.show_dog"
        labelText="ID Exhibition"
        class="input"
        type="number"
        placeholder="ID Exhibition"/>
        <b-form-select 
          v-model="dog_registered.show_medal" :options="medal_selector"
          labelText="Medal"
          placeholder="Medal"/>
        <big-button text="Добавить участника" />
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
    name: "RegisteredForm",
    components: {
      CenteredHeading,
      CenteredFormInput,
      Checkbox,
      BigButton
    },
    data () {
        return {
          dog_registered: {
            show_dog_number: '',
            status: '',
            dateof_reg_dog: '',
            bill: '',
            checkup: '',
            dateof_checkup: '',
            participant_dog: '',
            show_dog: '',
            show_medal: null,
          },
          status_selector: ["Participated",
                  "Suspended",
                  "Not allowed",
                  "Absence"],
          bill_selector: ["Paid",
                  "Not paid"],
          checkup_selector: ["Passed",
                  "Not passed"],
          medal_selector: ["Gold",
                  "Silver",
                  "Bronze",
                  "Audience award"],
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
        }
      },
      methods: {
        createRegister() {
            axios.post('http://127.0.0.1:8000/dog_reg/create/', {
            show_dog_number: this.dog_registered.show_dog_number,
            status: this.dog_registered.status,
            dateof_reg_dog: this.dog_registered.dateof_reg_dog,
            bill: this.dog_registered.bill,
            checkup: this.dog_registered.checkup,
            dateof_checkup: this.dog_registered.dateof_checkup,
            participant_dog: this.dog_registered.participant_dog,
            show_dog: this.dog_registered.show_dog,
            show_medal: this.dog_registered.show_medal,
          })
        }
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
  