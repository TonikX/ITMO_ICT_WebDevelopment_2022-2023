<template>
  <Header/>
  <LogIn/>

</template>

<script>
import LogIn from "../components/LogInForm.vue";
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
export default {
  name: "LogInView",
  components: {Footer, Header, LogIn},
}
</script>
