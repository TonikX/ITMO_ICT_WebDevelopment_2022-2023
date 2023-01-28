<template>
  <header-block/>
  <user-block/>
  <footer-block/>
</template>

<script>
import HeaderBlock from "@/components/Header.vue";
import FooterBlock from "@/components/Footer.vue";
import UserBlock from "@/components/Profile.vue";
import useUsersStore from "@/stores/users";
import {mapActions, mapState} from "pinia";

export default {
  name: "ProfilePage",
  components: {FooterBlock, UserBlock, HeaderBlock},
  computed: {
   ...mapState(useUsersStore, ['user', 'token', 'userEvents']),
  },
  methods: {
    ...mapActions(useUsersStore, ['logout', 'CurrentUser']),
  }
}
</script>

<style scoped>

</style>