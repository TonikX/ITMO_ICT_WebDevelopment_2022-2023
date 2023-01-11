<template>
  <img :src="src" class="card-img-top" width="262" :alt="description" style="height: 11rem;">
  <div class="card-body">
    <h3 class="card-title">{{ title }}</h3>
    <p class="card-text">{{ description }}</p>
    <p class="card-data">{{ date }}</p>
  <form action="" @submit.prevent="deleteCard(primaryId)">
    <button type="submit" class="btn btn-danger mt-3" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Отписаться от мероприятия
    </button>
  </form>
  </div>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useUserEventsStore from "@/stores/userEvents.js"

export default {
  name: 'PersonalCard',
  
  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
  },

  methods: {
    ...mapActions(useUserEventsStore, ['addUserEvents', 'deleteCardById']),

    async deleteCard(id) {
      this.deleteCardById(id)

      location.reload()
    }
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
    primaryId: {
      type: Number,
      required: true
    },
  },
}

</script>