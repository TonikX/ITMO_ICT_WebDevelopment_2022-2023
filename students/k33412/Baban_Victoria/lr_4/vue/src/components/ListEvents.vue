<template>
  <div class="container p-3">
    <div v-for="(eventRow, eventRowIndex) in eventRows"
         :key="`event-row-${eventRowIndex}`"
         class="event-row row py-2"
    >
      <EventCard v-for="(event) in eventRow"
                 :key="`event-${event.id}`"
                 :id="event.id"
                 :photo="event.photo"
                 :name="event.name"
                 :price="event.price"
                 :category="event.category"
                 :district="event.district"
                 :place="event.place"
                 :type_event="event.type_event"
                 :date="event.date"
      />
    </div>
  </div>

</template>

<script>
import {mapActions, mapState} from 'pinia'
import useEventsStore from "@/stores/event";
import EventCard from "./EventCard.vue";

export default {
  name: "ListEvents",
  components: {EventCard},
  computed: {
    ...mapState(useEventsStore, ['events']),
    eventRows() {
      return this.getEventsRows(3)
    },

  },
  methods: {
    ...mapActions(useEventsStore, ['fetchEvents']),
    getEventsRows(rowSize) {
      const eventRows = [];
      for (let i = 0; i < this.events.length; i += rowSize) {
        const row = this.events.slice(i, i + rowSize);
        eventRows.push(row);
      }
      return eventRows;
    },

  },
  mounted() {
    this.fetchEvents()
  }
}
</script>

<style scoped>

</style>