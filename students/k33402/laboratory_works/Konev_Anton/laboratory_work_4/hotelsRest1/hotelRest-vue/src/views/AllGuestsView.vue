<template>
  <guests v-if="this.token"/>
  <unlogged v-if="!this.token"/>
</template>

<script>
import Guests from "@/components/Guests.vue";
import Unlogged from "@/components/Unlogged.vue";
import {mapState} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  components: {
    Guests,
    Unlogged
  },
  computed: {
    ...mapState(useUsersStore, ["token"])
  }
}
</script>