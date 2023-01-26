<template>
  <HeaderNavBar/>
  <main class="min-vh-100">
    <slot/>
  </main>
  <FooterBlock/>
</template>

<script>
import HeaderNavBar from "../components/HeaderNavBar.vue";
import FooterBlock from "../components/FooterBlock.vue";

export default {
  name: "DefaultLayout",
  components: {
    HeaderNavBar,
    FooterBlock
  }
}
</script>

<style scoped>

</style>