<template>
  <div class="app">
    <h1>Информация о собаках</h1>
    <div class="d-flex align-center flex-column flex-md-row">
      <v-btn variant="outlined" color="warning" rounded="lg" @click="goBack">Назад</v-btn></div>
<!--    <dog-form/>-->
    <dog-list v-bind:dog="dog"/>
  </div>

</template>
<script>
// import DogForm from "@/components/DogForm.vue";
import DogList from "@/components/DogList.vue";
import axios from "axios";
export default {
  components: {
    DogList,
    // DogForm
  },

  data() {
    return {
      dog: [],
    }
  },
  methods: {
    async fetchDogs() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/dog/')
        console.log(response.data)
        this.dog = response.data
      } catch (e) {
        alert('Error')
      }
    },
    goBack() {
      this.$router.push({ name: 'home'})
    }
  },
  mounted() {
    this.fetchDogs()
  }
}
</script>
