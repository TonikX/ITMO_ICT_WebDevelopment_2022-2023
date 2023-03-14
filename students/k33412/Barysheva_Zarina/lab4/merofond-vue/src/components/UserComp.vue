<template>
  <div class="my-3">
    <div class="mb-3 text-center">
    <img src="avatar.jpg" id="av" />
    <p class="m-3 fs-1">{{ user.username }}</p>
  </div>
    <div class="container-md">
      <span v-if="count() === 0">
        Вы не зарегистрированы ни на одно мероприятие
      </span>
      <span v-else>
        <div
          class="accordion accordion-flush border"
          id="accordionFlushExample"
        >
          <span v-for="event in user_regs" :key="event.id">
            <div class="accordion-item">
              <h2 class="accordion-header" id="flush-headingOne">
                <button
                  class="accordion-button collapsed"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#flush-collapseOne"
                  aria-expanded="false"
                  aria-controls="flush-collapseOne"
                >
                  <h5>Мероприятие # {{ event.id }}</h5>
                </button>
              </h2>
              <div
                id="flush-collapseOne"
                class="accordion-collapse collapse"
                aria-labelledby="flush-headingOne"
                data-bs-parent="#accordionFlushExample"
              >
                <div class="accordion-body">
                  <div class="card mb-3" style="width: 100%">
                    <div class="row g-0">
                      <div class="col-md-4">
                        <img
                          src="eventcard.jpg"
                          class="img-fluid rounded-start"
                          alt="..."
                        />
                      </div>
                      <div class="col-md-8">
                        <div class="card-body">
                          <h5 class="card-title">{{ event.title }}</h5>
                          <p class="card-text">{{ event.description }}</p>
                        </div>
                        <ul class="list-group list-group-flush">
                          <li class="list-group-item">
                            <h6>Дата: {{ event.datetime }}</h6>
                          </li>
                          <li class="list-group-item">
                            <h6>Тип мероприятия:</h6>
                            <span
                              v-for="theevent_type in event_types"
                              :key="theevent_type.id"
                            >
                              <span
                                v-if="theevent_type.id === event.event_type"
                              >
                                {{ theevent_type.title }}
                              </span>
                            </span>
                          </li>
                          <li class="list-group-item">
                            <h6>Место проведения:</h6>
                            Театр
                          </li>
                        </ul>
                        <div class="card-body justify-content-end">
                          <button
                            @click="goEvent(event.id)"
                            class="btn text-light"
                            style="background-color: #2a9d8f; width: 100%"
                            >Перейти на страницу мероприятия</button
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </span>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: [],
      user_regs: [],
      event_types: [],
      event_locations: [],
    };
  },
  mounted() {
    const token = localStorage.getItem("token");
    if (!token) {
      console.log("No user logged");
      return;
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
        axios.get(`http://127.0.0.1:7777/user/${resp.data.id}/events`, {
          headers: {
            accept: "application/json",
            Authorization: `Token ${token}`,
          },
        }).then((r) => this.user_regs = r.data);
      });

    // this.user_regs = await axios
    //   .get(`http://127.0.0.1:7777/user/${this.user.id}`, {
    //     headers: {
    //       accept: "application/json",
    //       Authorization: `Token ${token}`,
    //     },
    //   })
    //   .then((resp) => {
    //     this.user_regs = resp.data;
    //   });

    axios
      .get("http://127.0.0.1:7777/event/type", {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.event_types = resp.data;
      });

    axios
      .get(`http://127.0.0.1:7777/event/location`, {
        headers: {
          accept: "application/json",
          Authorization: `Token ${token}`,
        },
      })
      .then((resp) => {
        this.event_locations = resp.data;
      });
  },

  methods: {
    goEvent(event_id) {
      localStorage.setItem("event", event_id);
      this.$router.replace({ path: "/event" });
    },
    goLogin() {
      localStorage.clear();
      this.$router.replace({ path: "/login" });
    },
    count() {
      return this.user_regs.length;
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
