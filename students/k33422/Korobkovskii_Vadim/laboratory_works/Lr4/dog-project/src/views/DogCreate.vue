<template>
  <div class="app">
    <dog-form/>
  </div>
</template>
<script>
import DogForm from "@/components/DogForm.vue";
import axios from "axios";
export default {
  components: {
    DogForm
  },

  data() {
    return {
      dog: [],
    }
  }
}
</script>



