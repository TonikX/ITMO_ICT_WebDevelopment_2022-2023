<template>
  <report v-if="this.token"/>
  <unlogged v-if="!this.token"/>
</template>

<script>
import Report from "@/components/Report.vue";
import Unlogged from "@/components/Unlogged.vue";
import {mapState} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  components: {
    Report,
    Unlogged
  },
  computed:{
    ...mapState(useUsersStore, ["token"])
  }
}
</script>

<style scoped>

</style>