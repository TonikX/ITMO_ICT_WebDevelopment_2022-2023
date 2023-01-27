<template>
  <Header/>
  <EventInfo/>
  <Footer/>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import EventInfo from "../components/EventInfo.vue";
export default {
  name: "CardView",
  components: {EventInfo, Footer, Header}
}
</script>
