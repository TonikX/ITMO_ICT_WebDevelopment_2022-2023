<template>
    <Head />
    <FullCalendar />
</template>

<script>

import FullCalendar from "@/components/FullCalendar.vue"
import Head from "@/components/Head.vue"

export default {
  name: 'EventsView',
  components: {
    FullCalendar,
    Head
  }
}
</script>