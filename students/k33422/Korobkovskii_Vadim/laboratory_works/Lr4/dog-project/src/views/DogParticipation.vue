<template>
  <div class="app">
    <h1>Информация об участии собак</h1>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="outlined" color="warning" rounded="lg" @click="goBack">Назад</v-btn></div>
    <dog-participation-list v-bind:dog_participation="dog_participation"/>
<!--    <dog-participation-form/>-->
  </div>
</template>
<script>
// import DogParticipationForm from "@/components/DogParticipationForm.vue";
import DogParticipationList from "@/components/DogParticipationList.vue";
import DogList from "@/components/DogList.vue"
import axios from "axios";
export default {
  components: {
    DogParticipationList,
    // DogParticipationForm,
    DogList
  },

  data() {
    return {
      dog_participation: [],
    }
  },
  methods: {
    async fetchRegDogs() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/dog_reg/')
        console.log(response.data)
        this.dog_participation = response.data
      } catch (e) {
        alert('Error')
      }
    },
    goBack() {
      this.$router.push({name: 'home'})
    }
  },
  mounted() {
    this.fetchRegDogs()
  }
}
</script>

