<template>
  <div class="col row-1 col-12  g-4 py-3">
    <UserEventCard v-for="(event) in userEvents"
                   :key="`user-event-${event.id}`"
                   :id="event.id"
                   :event_id="event.event_id"

    />
  </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useUserEventsStore from "@/stores/users_events";
import useUserStore from "@/stores/user";
import UserEventCard from "./UserEventCard.vue";


export default {
  name: "MyEvents",
  components: {UserEventCard},
  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
    ...mapState(useUserStore, ['token']),
  },
  methods: {
    ...mapActions(useUserEventsStore, ['fetchUsersEvents']),
  },
  mounted() {
    this.fetchUsersEvents(this.token)
  }
}
</script>
