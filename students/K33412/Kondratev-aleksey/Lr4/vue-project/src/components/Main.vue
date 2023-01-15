<template>
  <svg display="none">
    <symbol id="search-icon" viewBox="0 0 16 16">
      <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
    </symbol>
  </svg>

  <main class="container-fluid background-main">
    <section class="row row-cols-2 pt-5">
      <div class="d-flex flex-column justify-content-center align-items-end col-5">
        <h1 class="w-75 h1 pb-3 text-color">События обьединяют</h1>
        <p class="w-75 pt-6 text-color">Посещайте конференции и лекции, ходите на выставки и концерты, занимайтесь саморазвитием и ищите единомышленников</p>
      </div>
      <img class="w-50" src="../assets/image/people.png" alt="Радующиеся люди">
    </section>

    <section class="d-flex flex-column align-items-center pt-5">
      <h2 class="h2 mb-4 text-color">Актуальные мероприятия</h2>
      <div class="d-flex justify-content-center m-0">
        <p class="fs-5 pe-3 text-color">Сортировать</p>
        <div class="dropdown me-3">
          <select class="form-select-sm event-type" aria-label=".form-select-lg example">
            <option value="ALL">Выберите, чем хотите заняться</option>
            <option value="Спорт">Спорт</option>
            <option value="Музыка">Музыка</option>
          </select>
        </div>
        <div class="dropdown me-3">
          <select class="form-select-sm city-type" aria-label=".form-select-lg example">
            <option value="ALL">Выберите город</option>
            <option value="Москва">Москва</option>
            <option value="Санкт-Петербург">Санкт-Петербург</option>
          </select>
        </div>
        <form class="search-form d-flex justify-content-end col-12 col-sm-2 col-lg-4 col-xl-6" @submit.prevent="filter">
          <button type="submit" id="search" class="btn btn-info btn-sm" style="background-color:#d2cb60; border: 1px solid #d2cb60;">
            Поиск
            <svg class="icon-main"><use xlink:href="#search-icon"></use></svg>
          </button>
        </form>
      </div>
      <div class="row justify-content-center pt-5">
        <div class="card me-4 card-colors background text-color mb-3" style="width: 18rem;" data-event-id="{{ id }}" v-for="card in filteredCards" :key="card.id">
          <card-note :title="card.title" :src="card.src" :description="card.description" :date="card.date" :id="card.id"></card-note>
        </div>
      </div>
    </section>
    
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h3 class="modal-title" id="exampleModalLabel">Вы записаны</h3>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Ждем вас на нашем мероприятие с хорошим настроением
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useCardsStore from "@/stores/cards.js"

import CardNote from "@/components/Card.vue"

export default {
  name: 'MainBlock',

  components: { CardNote },

  computed: {
    ...mapState(useCardsStore, ['cards']),

    filteredCards() {
      if (this.selectedCards.length) {
        return this.selectedCards;
      } else {
        return this.cards
      }
    }
  },

  methods: {
    ...mapActions(useCardsStore, ['loadCards']),

    async filter() {
      const eventT = document.querySelector('.event-type')
      const cityT = document.querySelector('.city-type')
      this.selectedCards = []

      console.log(eventT.value, cityT.value)
      this.cards.forEach((card) => {
        if ((eventT.value === card.mero && cityT.value === card.city) || (eventT.value === "ALL" && cityT.value === card.city) || (eventT.value === card.mero && cityT.value === "ALL")) {
          this.selectedCards.push(card);
        }
      })
    }
  },

  data() {
    return {
      selectedCards: []
    }
  },

  mounted() {
    this.loadCards();
  }
}
</script>
