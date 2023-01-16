<template>
  <header-block/>
  <signup-block/>
  <footer-block/>
</template>

<script>
import HeaderBlock from "@/components/Header.vue";
import FooterBlock from "@/components/Footer.vue";
import SignupBlock from "@/components/Signup.vue";
import {mapActions, mapState} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  name: "SignUpPage",
  components: {HeaderBlock, SignupBlock, FooterBlock},
  computed: {
    ...mapState(useUsersStore, ['user'])
  },
  methods: {
    ...mapActions(useUsersStore, ['login, signUp'])
  }
}
</script>

<style scoped>

</style>