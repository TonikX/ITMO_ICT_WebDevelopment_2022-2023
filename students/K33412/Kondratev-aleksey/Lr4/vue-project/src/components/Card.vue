<template>
  <img :src="src" class="card-img-top" width="262" :alt="description" style="height: 11rem;">
  <div class="card-body">
    <h3 class="card-title">{{ title }}</h3>
    <p class="card-text">{{ description }}</p>
    <p class="card-data">{{ date }}</p>
  <a href="./event.html" class="btn btn-primary">На сайт мероприятия</a>
  <form action="" @submit.prevent="subscribe(id)">
    <button type="submit" class="btn btn-primary mt-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
      <svg class="icon-main"><use xlink:href="#register-icon"></use></svg>
      Записаться
    </button>
  </form>
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useUserEventsStore from "@/stores/userEvents.js"

export default {
  name: 'CardNote',

  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
  },

  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    },
    src: {
      type: String,
      required: true
    },
    id: {
      type: Number,
      required: true
    },
  },

  methods: {
    ...mapActions(useUserEventsStore, ['addUserEvents']),

    async subscribe(id) {
      const userEvents = {
        "userId": JSON.parse(localStorage.user).id,
        "eventId": id
      }

      console.log(userEvents)

      const response = await this.addUserEvents(userEvents);

      console.log(response)
    }
  }
}

</script>