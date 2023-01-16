<template>
  <HeaderNavBar/>
  <main>
    <section class="min-vh-100">
      <WelcomeSection/>
    </section>
  </main>
  <FooterBlock/>
</template>

<script>
import HeaderNavBar from "../components/HeaderNavBar.vue";
import FooterBlock from "../components/FooterBlock.vue";
import WelcomeSection from "../components/WelcomeSection.vue";

export default {
  name: "WelcomeView",
  components: {
    HeaderNavBar,
    FooterBlock,
    WelcomeSection
  }
}
</script>

<style scoped>

</style>