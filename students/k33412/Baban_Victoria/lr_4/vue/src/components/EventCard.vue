<template>
  <div class="col-4">
    <div class="card h-100" :event_id="id">
      <img :src="photo" class="card-img-top img-fluid" :alt="name">
      <div class="card-header d-flex justify-content-between align-content-center">
        <a class="btn btn-outline-secondary btn-sm">{{ category }}</a>
        <p class="card-text">{{ date }}</p>
      </div>
      <div class="card-body text-center d-flex flex-column justify-content-around p-3">
        <h5 class="card-title">{{ name }}</h5>
        <div class="card-text d-flex justify-content-around ">
          <p class="card-text">{{ place }}</p>
          <p class="card-text text-success">{{ price }}</p>
        </div>
        <div class="card-text d-flex justify-content-around ">
          <RouterLink :to="`/events/${id}`" class="text-black nav-link">
            <a href="#" class="btn  align-self-center" style="background-color: #20c997;" >Подробнее...</a>
          </RouterLink>
          <!--
          <form >
            <button type="button" class="btn btn-outline-danger align-self-center" @click="addUserEvent">Записаться</button>
          </form>
          -->
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useUserEventsStore from "@/stores/users_events";
import useUserStore from "@/stores/user";

export default {
  name: "EventCard",

  props: {
      id: {type: Number, required: true},
      name: {type: String, required: true},
      price: {type: String, required: true},
      photo: {type: String, required: true},
      category: {type: String, required: true},
      district: {type: String, required: true},
      place: {type: String, required: true},
      type_event: {type: String, required: true},
      date: {type: Date, required: true},
      description: {type: String}
  },
}
</script>

<style scoped>

</style>