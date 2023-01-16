<template>
  <HeaderNavBar/>
  <FooterBlock/>
</template>

<script>
import HeaderNavBar from "../components/HeaderNavBar.vue";
import FooterBlock from "../components/FooterBlock.vue";

export default {
  name: "WelcomeView",
  components: {
    HeaderNavBar,
    FooterBlock
  }
}
</script>

<style scoped>

</style>