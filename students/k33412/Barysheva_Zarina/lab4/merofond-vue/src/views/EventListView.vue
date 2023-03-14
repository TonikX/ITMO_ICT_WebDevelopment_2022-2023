<template>
    <span><Navbar />
    <div class="m-3 text-center">
      <h1>Календарь мероприятий</h1>
    </div>
    <div class="container my-5">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-3">
          <span v-for="event in events" :key="event.id">
            <div class="col">
              <event-card :event="event" />
            </div>
        </span>
        </div>
    </div>
  </span>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import EventCard from "../components/EventCard.vue";
import axios from "axios";

export default {
  components: { Navbar, EventCard },
  data() {
    return {
      events: [],
      location: []
    };
  },
  // methods: {
  //   },
    mounted() {
      axios
          .get("http://127.0.0.1:7777/event/list", {
              headers: {
                  Authorization: `Token ` + localStorage.getItem("token"),
              },
          })
          .then((res) => {
              this.events = res.data;
          })
          .catch(() => null);
      },
};
</script>
