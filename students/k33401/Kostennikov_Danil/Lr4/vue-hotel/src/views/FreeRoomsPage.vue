<template>
  <HeaderComponent> </HeaderComponent>
  <a></a>
  <h1>Amount of free rooms on current date</h1>

  <form
    ref="noteForm"
    @submit.prevent="createCard"
    class="d-flex flex-column my-5"
  >
    <input type="text" v-model="form.date" class="my-1" />

    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>

  <div class="row row-cols-1 row-cols-md-2 g-4 mt-5" id="notes">
    <div>
      <free-rooms :date="date" :text="rooms" />
    </div>
  </div>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import FreeRooms from "@/components/FreeRooms.vue";
import HeaderComponent from "@/components/Navbar.vue";
import { mapActions, mapState } from "pinia";

import userRoomsStore from "@/stores/rooms";

export default {
  name: "FreeRoomsPage",

  components: { BaseLayout, FreeRooms, HeaderComponent },

  computed: {
    ...mapState(userRoomsStore, ["rooms", "date"]),
  },

  methods: {
    ...mapActions(userRoomsStore, ["loadFreeRooms"]),

    async createCard() {
      console.log(this.form);
      console.log(this.form.date);
      await this.loadFreeRooms(this.form.date);

      this.$refs.noteForm.reset();
      console.log(this.rooms);
    },
  },

  data() {
    return {
      form: {
        date: "",
      },
    };
  },

  mounted() {
    if (localStorage.getItem("reloaded")) {
      // The page was just reloaded. Clear the value from local storage
      // so that it will reload the next time this page is visited.
      localStorage.removeItem("reloaded");
    } else {
      // Set a flag so that we know not to reload the page twice.
      localStorage.setItem("reloaded", "1");
      location.reload();
    }
  },
};
</script>
