<template>
  <rooms v-if="this.token"/>
  <unlogged v-if="!this.token"/>
</template>

<script>
import Rooms from '@/components/Rooms.vue'
import Unlogged from "@/components/Unlogged.vue";
import {mapState} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  components: {
    Rooms,
    Unlogged
  },
  computed: {
    ...mapState(useUsersStore, ["token"])
  }
}
</script>