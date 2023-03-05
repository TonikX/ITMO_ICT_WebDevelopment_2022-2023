<template>
      <v-form @submit.prevent class="my-0">
        <h1>Edit registered dog (with ID {{ $route.params.id }})</h1>
          <v-row>
          <v-col class="mx-auto">
            <v-text-field
                v-model="dog_registered.show_dog_number"
                label="Number of dog"
                class="input"
                type="number"
                placeholder="Number of dog"/>
            <v-select
                v-model="dog_registered.status"
                label="Dog status"
                :items="status_choices"
                placeholder="Status"/>
            <v-text-field
                v-model="dog_registered.dateof_reg_dog"
                label="Date of dog registration"
                class="input"
                type="date"
                placeholder="Date of registration"/>
            <v-select
                v-model="dog_registered.bill"
                label="Bill date"
                :items="bill_choices"
                placeholder="Bill"/>
            <v-select
                v-model="dog_registered.checkup"
                label="Checkup status"
                :items="checkup_choices"
                placeholder="Status"/>
            <v-text-field
                v-model="dog_registered.dateof_checkup"
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
                label="Exhibition ID"
                class="input"
                type="number"
                placeholder="Exhibition"/>
            <v-select
                v-model="dog_registered.show_medal"
                clearable
                label="Medal"
                :items="medals"/>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="tonal" rounded="pill" @click="changeDogRegistered">Edit</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn vvariant="tonal" color="error" rounded="pill" @click="goBack">Back</v-btn></div>
          </v-col>
        </v-row>
      </v-form>
    </template>
    
    <script>
    import axios from "axios"
    export default {
      name: "DogRegisteredChangeForm",
      props: {
        dog_id: {
          type: Number,
          required: true
        }
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
          status_choices: ["Participated",
                  "Suspended",
                  "Not allowed",
                  "Absence"],
          bill_choices: ["Paid",
                  "Not paid"],
          checkup_choices: ["Passed",
                  "Not passed"],
          medals: ["Gold",
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
        async getDogRegistered() {
          const response = await axios.get(`http://127.0.0.1:8000/dog_reg/${this.dog_id}/`)
           console.log(response.data)
           this.dog_registered.show_dog_number = response.data.show_dog_number
           this.dog_registered.status = response.data.status
           this.dog_registered.dateof_reg_dog = response.data.dateof_reg_dog
           this.dog_registered.bill = response.data.bill
           this.dog_registered.checkup = response.data.checkup
           this.dog_registered.dateof_checkup = response.data.dateof_checkup
           this.dog_registered.participant_dog = response.data.participant_dog
           this.dog_registered.show_dog = response.data.show_dog
           this.dog_registered.show_medal = response.data.show_medal
        },
        changeDogRegistered() {
          axios.patch(`http://127.0.0.1:8000/dog_reg/${this.dog_id}/`, {
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
          this.$router.push({ name: 'dog_registered'})
        }
      },
      mounted() {
        this.getDogRegistered()
      }
    }
    </script>
    
    <style scoped>
    </style>
    