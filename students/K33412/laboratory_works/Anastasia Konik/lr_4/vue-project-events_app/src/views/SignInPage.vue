<template>
  <header-block/>
  <signin-block/>
  <footer-block/>
</template>

<script>
import HeaderBlock from "@/components/Header.vue";
import SigninBlock from "@/components/Signin.vue";
import FooterBlock from "@/components/Footer.vue";
import {mapActions, mapState} from "pinia";
import useUsersStore from "@/stores/users";


export default {
  name: "SignInPage",
  components: {HeaderBlock, SigninBlock, FooterBlock},
  computed: {
    ...mapState(useUsersStore, ['user'])
  },
  methods: {
    ...mapActions(useUsersStore, ['login'])
  }
}
</script>

<style scoped>

</style>