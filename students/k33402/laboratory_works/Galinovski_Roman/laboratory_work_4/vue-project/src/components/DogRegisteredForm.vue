<template>
      <h1>Create refistered dog</h1>
      <v-form @submit.prevent class="my-0">
        <v-row>
          <v-col class="mx-auto">
            <v-text-field
                v-model="dog_registered.show_dog_number"
                label="Number of dog"
                class="input"
                type="number"
                placeholder="Number of dog"/>
            <v-select
                v-model="dog_registered.dog_status"
                label="Dog status"
                :items="status_selector"
                placeholder="Status"/>
            <v-text-field
                v-model="dog_registered.reg_dog_date"
                label="Date of dog registration"
                class="input"
                type="date"
                placeholder="Date of dog registration"/>
            <v-select
                v-model="dog_registered.bill"
                label="Bill status"
                :items="bill_selector"
                placeholder="Status"/>
            <v-select
                v-model="dog_registered.checkup"
                label="Checkup status"
                :items="checkup_selector"
                placeholder="Status"/>
            <v-text-field
                v-model="dog_registered.checkup_date"
                label="Date of checkup"
                class="input"
                type="date"
                placeholder="Date of checkup"/>
            <v-text-field
                v-model="dog_registered.participant_dog"
                label="Dog ID"
                class="input"
                type="number"
                placeholder="Dog"/>
            <v-text-field
                v-model="dog_registered.show_dog"
                label="ID Exhibition"
                class="input"
                type="number"
                placeholder="Exhibition"/>
            <v-select
                v-model="dog_registered.show_medal"
                clearable
                label="Medal"
                :items="medal_selector"/>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" rounded="pill" @click="createDogRegistered">Add</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
          </v-col>
        </v-row>
      </v-form>
    </template>
    
    <script>
    import axios from "axios"
    export default {
      name: "DogRegisteredForm",
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
        createDogRegistered() {
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
        },
        goBack() {
          this.$router.push({ name: 'home'})
        }
      }
    }
    </script>
    
    <style scoped>
    </style>