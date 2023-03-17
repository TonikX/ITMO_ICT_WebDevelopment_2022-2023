<template>
    <Head />
    <EventAbout 
                :id="event.id"
                :about = "event.about"
                :category_name = "event.category.name"
                :date = "event.date"
                :time = "event.time"
                :city = "event.place.city"
                :place_name = "event.place.place_name"
                :street = "event.place.street"
                :organizer = "event.organizer"
                :name = "event.name"
    
    />
</template>

<script>

import Head from "@/components/Head.vue"
import EventAbout from "@/components/EventAbout.vue"
import { mapActions, mapState } from "pinia"
import { useRoute } from "vue-router"
import eventsStore from "@/store/event_store"

export default {
  name: 'EventView',
  components: {
    EventAbout,
    Head
  },
  computed: {
    ...mapState(eventsStore, ['event']),
    
    eventId() {
      const route = useRoute();
      return parseInt(route.params.id)
    }
  },
  methods: {
    ...mapActions(eventsStore, ['getCertainEvent']),
  },
  mounted() {
    this.getCertainEvent(this.eventId)
  }

}
</script>
