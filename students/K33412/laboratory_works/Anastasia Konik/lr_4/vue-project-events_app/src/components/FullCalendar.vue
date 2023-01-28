<template>
  <div class="container p-5 mb-5">
    <full-calendar :options="calendarOptions"/>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

const DEFAULT_OPTIONS = {
  plugins: [dayGridPlugin, interactionPlugin],
  initialView: 'dayGridMonth',
  editable: true,
  timeZone: 'UTC',
  eventTimeFormat: {
    hour: '2-digit',
    minute: '2-digit',
    meridiem: false,
    hour12: false,
  }
}


export default {
  components: {
    FullCalendar
  },

  props: {
    options: {
      type: Object,
      default: DEFAULT_OPTIONS,
    }
  },

  computed: {
    calendarOptions() {
      return {...DEFAULT_OPTIONS, ...this.options}
    }
  }
}
</script>

<style>
.fc-event-title {
  white-space: normal;
  margin-left: 5px;
}


</style>