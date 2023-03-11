<template>
    <main>
      <hr class="opacity-100 m-0 hr-jopa"/>
      <section class="form-signin">
      <b-form  @submit.prevent @submit="changeDogRegistered" class="my-2">
        <centered-heading text="Редактирование Участника" />
  
        <b-form-input
          v-model="dog_registered.show_dog_number"
          labelText="Number of dog"
          class="input"
          type="number"
          placeholder="Number of dog"/>
        <b-form-select 
          v-model="dog_registered.status" :options="status_choices"
          labelText="Dog status"
          placeholder="Dog status"/>
        <b-form-input
        v-model="dog_registered.dateof_reg_dog"
        labelText="Date of dog registration"
        class="input"
        type="date"
        placeholder="Date of dog registration"/>
        <b-form-select
        v-model="dog_registered.bill" :options="bill_choices"
        labelText="Bill status"
        placeholder="Bill status"/>
        <b-form-select 
          v-model="dog_registered.checkup" :options="checkup_choices"
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
          v-model="dog_registered.show_medal" :options="medals"
          labelText="Medal"
          placeholder="Medal"/>
        <big-button text="Изменить участника" />
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
    name: "RegisteredChangeForm",
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
        }
      },
      mounted() {
        this.getDogRegistered()
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
  