<template>
  <full-calendar :options="calendarOptions" />
</template>
  
<script>
  import FullCalendar from '@fullcalendar/vue3'
  import dayGridPlugin from '@fullcalendar/daygrid'
  import interactionPlugin from '@fullcalendar/interaction'
  
  const DEFAULT_OPTIONS = {
    plugins: [ dayGridPlugin, interactionPlugin ],
    initialView: 'dayGridMonth',
    editable: true
  }
  export default {
    components: {
      FullCalendar
    },
    props: {
      options: {
        type: Object,
        default: DEFAULT_OPTIONS
      }
    },
    computed: {
      calendarOptions() {
        return { ...DEFAULT_OPTIONS, ...this.options }
      }
    }
  }
</script>

<style>
  .fc-day {
    cursor: pointer;
  }
</style>