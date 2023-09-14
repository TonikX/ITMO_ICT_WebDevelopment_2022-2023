<template>
  <header-block/>
  <event-block
      :address="cards[parseInt($route.params.id) - 1].address"
      :date="cards[parseInt($route.params.id) -1].date"
      :full_description="cards[parseInt($route.params.id) - 1].full_description"
      :id="cards[parseInt($route.params.id) - 1].id"
      :img_src="cards[parseInt($route.params.id) - 1 ].img_src"
      :short_description="cards[parseInt($route.params.id)- 1].short_description"
      :title="cards[parseInt($route.params.id) - 1].title"
      :website="cards[parseInt($route.params.id) - 1].website"/>
  <footer-block/>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import HeaderBlock from '../components/Header.vue'
import EventBlock from '../components/Event.vue'
import FooterBlock from '../components/Footer.vue'
import {useRoute} from "vue-router";
import useUsersStore from "@/stores/users";
import useCardsStore from "@/stores/cards";

export default {
  name: 'EventPage',
  components: {HeaderBlock, EventBlock, FooterBlock},
  computed: {
    ...mapState(useUsersStore, ['user', 'token']),
    ...mapState(useCardsStore, ["cards"]),
    EventId() {
      const route = useRoute();
      return parseInt(route.params.id)
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['addUserEvent']),
    ...mapActions(useCardsStore, ['loadOneCard']),
  },
  mounted() {
    this.loadOneCard(this.EventId);
  }
}
</script>