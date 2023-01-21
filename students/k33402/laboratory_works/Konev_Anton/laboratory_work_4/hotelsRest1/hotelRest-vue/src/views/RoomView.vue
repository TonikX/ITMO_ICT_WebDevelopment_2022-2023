<template>
  <room :id="id"/>
</template>

<script>
import Room from "@/components/Room.vue";

export default {
  props: {
    id: String
  },
  components: {
    Room
  }
}
</script>

<style scoped>

</style>