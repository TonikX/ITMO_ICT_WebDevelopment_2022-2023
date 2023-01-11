<template>
  <main class="container-xl p-5 mb-5">
    <h1 class="row mb-3 justify-content-center">Events in Saint-Petersburg</h1>
    <div class="text-center">
      <img src="src/assets/img/spb.jpg" class="rounded col-6" alt="Photo of Saint-Petersburg">
    </div>
    <section class="filtration" @change="filter">
      <div class="form text-center col-sm-6 col-lg-4 col-xl-3 mt-3 mx-auto">
        <select class="filter form-select-sm" aria-label=".form-select-sm example" id="filter_by_type">
          <option selected>Event type</option>
          <option value="theater">Theaters</option>
          <option value="concert">Concerts</option>
          <option value="exhibition">Exhibitions</option>
          <option value="activity">Outdoor activities</option>
          <option value="festival">Festivals</option>
        </select>
      </div>
      <div class="form text-center col-sm-6 col-lg-4 col-xl-3 mt-3 mx-auto">
        <select class="filter form-select-sm" aria-label=".form-select-sm example" id="filter_by_place">
          <option selected>Choose district</option>
          <option value="admiralteysky">Admiralteysky</option>
          <option value="petrogradsky">Petrogradsky</option>
          <option value="moskovsky">Moskovsky</option>
          <option value="tsentralny">Tsentralny</option>
          <option value="vasileostrovsky">Vasileostrovsky</option>
        </select>
      </div>
    </section>
    <section id="event_cards" class="container justify-content-center row mx-auto mt-3">
      <div class="card event col-xl-4 col-lg-4 col-md-4 col-sm-6 card mx-3 mt-3" :class="[card.district, card.type]"
           v-for="card in Cards" :key="card.id">
        <card :title="card.title" :address="card.address" :img_src="card.img_src"
              :short_description="card.short_description" :id="card.id"></card>
      </div>
    </section>
  </main>
</template>

<script>
import {mapActions, mapState} from "pinia";
import Card from "@/components/Card.vue"
import useCardsStore from "@/stores/cards.js";

export default {
  name: "MainBlock",
  components: {Card},
  computed: {
    ...mapState(useCardsStore, ['cards']),
    Cards() {
      return this.cards
    }
  },
  methods: {
    ...mapActions(useCardsStore, ['loadCards']),
    async filter() {
      let selectedPlace = document.getElementById("filter_by_place").value;
      let selectedType = document.getElementById("filter_by_type").value;
      const cards = document.getElementsByClassName("event");
      console.log(cards)
      for (let i = 0; i < cards.length; i++) {
        if ((cards[i].classList.contains(selectedPlace) || selectedPlace === "Choose district") &&
            (cards[i].classList.contains(selectedType) || selectedType === "Event type")) {
          cards[i].classList.remove("d-none");
        } else {
          cards[i].classList.add("d-none");
        }
      }
      console.log(cards)
    }
  },
  mounted() {
    this.loadCards();
  }
}
</script>

<style scoped>

</style>