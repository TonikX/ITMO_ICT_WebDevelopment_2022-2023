<template>
  <main class="container-fluid background-main">
    <section class="pt-5 pb-5">
      <div class="d-flex flex-column align-items-center pt-5 pb-5">
        <div class="d-flex flex-column align-items-center">
          <h1 class="h2 p-0 mb-2 text-color">Ваш личный кабинет</h1>
          <p class="p-0 m-2 text-color">Ваши записи</p>
          <div class="row justify-content-center pt-5 pb-5">
            <div class="card me-4 card-colors background text-color mb-3" style="width: 18rem;" data-event-id="{{ id }}" v-for="card in personalCards" :key="card.id">
              <personal-card :title="card.title" :src="card.src" :description="card.description" :date="card.date" :primaryId="card.primaryId"></personal-card>
            </div>
          </div>
        </div>
        <div class="row justify-content-center" id="container">
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h2 class="modal-title" id="exampleModalLabel">Оповещение</h2>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  Вы были отписаны от мероприятия
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { mapActions, mapState } from "pinia";

import useCardsStore from "@/stores/cards.js"
import useUserEventsStore from "@/stores/userEvents.js"

import PersonalCard from "@/components/PersonalCard.vue"

export default {
  name: 'PersonalBlock',

  components: { PersonalCard },

  computed: {
    ...mapState(useUserEventsStore, ['userEvents']),
    ...mapState(useCardsStore, ['personalCards']),
  },

  methods: {
    ...mapActions(useUserEventsStore, ['getUserEventsById']),
    ...mapActions(useCardsStore, ['loadCardById', 'doClear']),

    async loadPage() {
      const response = await this.getUserEventsById(JSON.parse(localStorage.user).id);

      const result = Array.from(response.data);

      this.doClear();
      result.forEach((item) => {
        this.loadCardById(item.eventId, item.id)
      })
    }
  },

  mounted() {
    this.loadPage();
  }
}
</script>