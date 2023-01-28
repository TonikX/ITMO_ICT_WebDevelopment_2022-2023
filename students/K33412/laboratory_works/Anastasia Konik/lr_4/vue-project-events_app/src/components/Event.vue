<template>
  <main class="container-xl p-5 mb-5">
    <section class="row d-flex" id="event_page">
      <h1 class="row mb-3 ">{{ title }}</h1>
      <div class="row d-flex col-lg-4 col-md-4 col-sm-4">
        <ul>
          <h5 class="text mt-2">Address:</h5>
          <h5 class="text mt-2">{{ address }}</h5>
          <h5 class="text mt-5">Date:</h5>
          <h5 class="text mt-2" id="date"></h5>
          <h5 class="text mt-5"><a :href="website">Website</a></h5>
        </ul>
      </div>
      <div class="row d-flex col-lg-8 col-md-8 col-sm-8">
        <img class="align-self-end" :src="img_src" :alt="title">
      </div>
      <div class="mx-1 mb-5 mt-4">
        <button :id="'event_enroll'+ id" class="btn mt-auto btn-dark purple_button" :disabled="!isActive"
                @click="enroll(this.id)" aria-pressed="true">Enroll
        </button>
      </div>
      <div class="card border-light mb-3 mx-auto">
        <div class="card-header">Description</div>
        <div class="card-body">
          <h5 class="card-title">{{ short_description }}</h5>
          <p class="card-text">{{ full_description }}</p>
        </div>
      </div>
    </section>
  </main>
</template>

<script>

import {mapActions, mapState} from "pinia";
import useUsersStore from "@/stores/users";
import moment from "moment";

export default {
  name: "EventBlock",
  props: {
    title: {
      type: String,
      required: true
    },
    address: {
      type: String,
      required: true
    },
    website: {
      type: String,
      required: true
    },
    img_src: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    },
    full_description: {
      type: String,
      required: true
    },
    short_description: {
      type: String,
      required: true
    },
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      isActive: true,
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user', 'token']),
  },
  mounted() {
    this.convertDate()
  },
  methods: {
    ...mapActions(useUsersStore, ['addUserEvent']),
    async enroll(id) {
      const userEvent = {
        "event": id,
        "user": this.user.username
      }
      console.log(userEvent)
      const response = await this.addUserEvent(userEvent);
      console.log(response)
      this.isActive = false
    },
    convertDate() {
      let form_date = moment(this.date).utc().format('Do MMMM YYYY, HH:mm')
      console.log(form_date)
      document.getElementById('date').innerHTML=form_date
      return form_date
    },
  }
}
</script>

<style scoped>

</style>