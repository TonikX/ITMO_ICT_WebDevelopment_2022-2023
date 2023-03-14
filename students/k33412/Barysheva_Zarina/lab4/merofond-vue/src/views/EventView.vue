<template>
    <span>
        <navbar />
        <div class="container-fluid">
            <span v-for="theevent in event" :key="theevent.id">
        <div class="my-3 text-center">
            <img src="eventcard.jpg" style="width: 20%; height: 20%;" />
            
            <p class="m-3 fs-1">{{ theevent.title }}</p>
        </div>
        <div class="container-md my-3">
            <p class="m-3 fs-2">Описание</p>
            <p class="fs-4">{{ theevent.description }}</p>
            <p class="m-3 fs-2">Дата: {{ theevent.datetime }}</p>
            <p class="m-3 fs-2">Тип мероприятия:</p>
            <p class="fs-4">{{ theevent.event_type }}</p>
            <p class="m-3 fs-2">Место проведения:</p>
            <p class="fs-4">{{ theevent.location }}</p>
        </div>
    </span>
    <div class="text-center">
    <button @click="goRegEvent" class="btn text-light" style="background-color: #2A9D8F; width:50%;">Зарегистрироваться на мероприятие</button>
</div>
  </div>

    </span>
</template>

<script>
import axios from "axios";
import Navbar from '../components/Navbar.vue';


export default {
  components: { Navbar },
  data() {
    return {
      user: {},
      event: {},
    //   event_id_: null,
    };
  },
  mounted() {
    const token = localStorage.getItem("token");
    const event_id = localStorage.getItem("event");
    if (!token) {
      console.log("No user logged");
      return;
    }
    if (event_id) {
    axios
      .get(`http://127.0.0.1:7777/event/${event_id}`, {
        headers: {
          accept: "application/json",
           Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.event = resp.data;
      });

    }
    axios
      .get("http://127.0.0.1:7777/auth/users/me", {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.user = resp.data;
      });
  },

  methods: {
    goRegEvent() {
      const event_id = localStorage.getItem("event");
      //localStorage.removeItem("event");
      const token = localStorage.getItem("token");
      if (event_id) {
        axios
          .get(`http://127.0.0.1:7777/event/${event_id}`, {
            headers: {
              accept: "application/json",
              Authorization: `Token ${token}`,
            },
          })
          .then((resp_event) => {
            axios
              .get("http://127.0.0.1:7777/auth/users/me", {
                headers: {
                  accept: "application/json",
                  Authorization: `Token ${token}`,
                },
              })
              .then((resp_user) => {
                this.axios
                    .post("http://127.0.0.1:7777/event/reg", {
                      headers: {
                        accept: "application/json",
                        Authorization: `Token ${token}`,
                      },

                      user: resp_user,
                      event: resp_event,
                    })
                    .then(() => {
                      this.$router.replace({ path: "/event" });
                    });
              });
          });

    }
      
      
    },

  },
};
</script>

<style>
#av {
  width: 15%;
  height: 15%;
  border-radius: 25px;
}
</style>
