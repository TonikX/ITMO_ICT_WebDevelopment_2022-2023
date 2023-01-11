<template>
  <header-block/>
  <full-calendar
      :options="{
    events: userEvents,
  }"
  />
  <footer-block/>
</template>

<script>
import HeaderBlock from "@/components/Header.vue";
import FullCalendar from "@/components/FullCalendar.vue";
import FooterBlock from "@/components/Footer.vue";
import useUsersStore from "@/stores/users";
import {mapActions, mapState} from "pinia";

export default {
  name: "CalendarPage",
  components: {FooterBlock, FullCalendar, HeaderBlock},
  computed: {
    ...mapState(useUsersStore, ['userEvents'])
  },
  methods: {
    ...mapActions(useUsersStore, ['getUserEvents'])
  },
  mounted() {
    this.getUserEvents()
  }
}
</script>

<style scoped>

</style>