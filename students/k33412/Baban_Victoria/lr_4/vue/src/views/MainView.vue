<template>
  <Header/>
  <div class="min-vh-100">
    <Filter/>
    <ListEvents/>
  </div>
  <Footer/>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Filter from "../components/Filter.vue";
import EventCard from "../components/EventCard.vue";
import ListEvents from "../components/ListEvents.vue";

export default {
  name: "MainView",
  components: {ListEvents, EventCard, Filter, Footer, Header},
}
</script>

