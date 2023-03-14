<template>
    <div class="card" style="width: 100%; height: 45rem;">
        <img src="eventcard.jpg" class="card-img-top" alt="...">
        <div class="card-body" style="height: 100%;">
            <h5 class="card-title"> {{ event.title }}</h5>
            <p class="card-text">{{ event.description }}</p>
        </div>
        <ul class="list-group list-group-flush" style="height: 30%;">
            <li class="list-group-item">
                <h6> Дата: {{ event.datetime }}</h6>
            </li>
            <li class="list-group-item">
                <h6> Тип мероприятия:</h6>
                <span v-for="event_type in type" :key="event_type.id" >
                    {{ event_type.title }}
                </span>
            </li>
            <li class="list-group-item">
                <h6> Место проведения:</h6>
                <span v-for="event_location in location" :key="event_location.id" >
                    {{ event_location.title }}
                </span>
            </li>
        </ul>
        <div class="card-body" style="height: 10%;">
            <a id="clickable" @click="goEvent(event.id)" class="btn text-light" style="background-color: #2A9D8F; width:100%;">Перейти на страницу мероприятия</a>
        </div>
    </div>
</template>

<script>

import axios from "axios";
export default {
  props: {
    event: Object,
  },

  data(){
    return {
        location: Object,
        type: Object,
    }
  },

  methods: {
    goEvent(event_id) {
      localStorage.setItem("event", event_id);
      this.$router.replace({ path: "/event" });
    },
    },
    mounted() {
        axios
          .get(`http://127.0.0.1:7777/event/type/${this.event.event_type}`, {
              headers: {
                  Authorization: `Token ` + localStorage.getItem("token"),
              },
          })
          .then((res) => {
              this.type = res.data;
          })
          .catch(() => null);
        axios
          .get(`http://127.0.0.1:7777/event/location/${this.event.location}`, {
              headers: {
                  Authorization: `Token ` + localStorage.getItem("token"),
              },
          })
          .then((res) => {
              this.location = res.data;
          })
          .catch(() => null);
    },
};
</script>

<style>

</style>
