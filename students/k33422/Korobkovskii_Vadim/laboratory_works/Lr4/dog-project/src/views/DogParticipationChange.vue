<template>
  <div class="app">
<!--    <h1>Идентификатор записи: {{ $route.params.id }} </h1>-->
    <dog-participation-change-form v-bind:dog_id="dog_id"/>
  </div>
</template>
<script>
import DogParticipationChangeForm from "@/components/DogParticipationChangeForm.vue";
import axios from "axios";
export default {
  components: {
    DogParticipationChangeForm
  },

  data() {
    return {
      dog_participation: [],
      dog_id: this.$route.params.id,
    }
  }
}
</script>
