<template>
    <Head />
    <EventsList />
</template>

<script>

import EventsList from "@/components/EventList.vue"
import Head from "@/components/Head.vue"

export default {
  name: 'EventsView',
  components: {
    EventsList,
    Head
  }
}
</script>
