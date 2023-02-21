<template>
  <HeaderComponent> </HeaderComponent>
  <a></a>
  <h1>Amount of client from current city</h1>

  <form
    ref="noteForm"
    @submit.prevent="createCard"
    class="d-flex flex-column my-5"
  >
    <input type="text" v-model="form.cityForm" class="my-1" />

    <button type="submit" class="btn btn-primary">Отправить</button>
  </form>

  <div class="row row-cols-1 row-cols-md-2 g-4 mt-5" id="notes">
    <div>
      <client-city :city="this.city" :count="this.count" />
    </div>
  </div>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import ClientCity from "@/components/ClientCity.vue";
import HeaderComponent from "@/components/Navbar.vue";
import { mapActions, mapState } from "pinia";

import clientStore from "@/stores/client";

export default {
  name: "ClientCityPage",

  components: { BaseLayout, ClientCity, HeaderComponent },

  computed: {
    ...mapState(clientStore, ["city", "count"]),
  },

  methods: {
    ...mapActions(clientStore, ["loadClientCityCount"]),

    async createCard() {
      console.log(this.form);
      console.log(this.form.cityForm);
      console.log(this.form.cityForm);
      await this.loadClientCityCount(this.form.cityForm);

      this.$refs.noteForm.reset();
      console.log(this.city);
      console.log(this.count);
    },
  },

  data() {
    return {
      form: {
        cityForm: "",
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
