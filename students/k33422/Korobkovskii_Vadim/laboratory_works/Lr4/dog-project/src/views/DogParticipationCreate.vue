<template>
  <div class="app">
    <dog-participation-form/>
  </div>
</template>
<script>
import DogParticipationForm from "@/components/DogParticipationForm.vue";
import axios from "axios";
export default {
  components: {
    DogParticipationForm
  },

  data() {
    return {
      dog_participation: [],
    }
  }
}
</script>


