<template>
  <div class="app">
<!--    <h1>Идентификатор записи: {{ $route.params.id }} </h1>-->
    <dog-change-form v-bind:dog_id="dog_id"/>
  </div>
</template>
<script>
import DogChangeForm from "@/components/DogChangeForm.vue";
import axios from "axios";
export default {
  components: {
    DogChangeForm
  },

  data() {
    return {
      dog: [],
      dog_id: this.$route.params.id,
    }
  }
}
</script>

