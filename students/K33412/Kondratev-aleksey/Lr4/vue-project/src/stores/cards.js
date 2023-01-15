import { defineStore } from 'pinia'
import { cardApi } from '@/api'

const useCardsStore = defineStore('cards', {
  state: () => ({
    cards: [],
    personalCards: []
  }),

  actions: {
    async loadCards() {
      const response = await cardApi.getAll();

      this.cards = response.data;

      return response;
    },

    async loadCardById(eventId, id) {
      const response = await cardApi.getById(eventId);

      response.data.primaryId = id;

      this.personalCards.push(response.data)

      return response
    },

    async doClear() {
      this.personalCards = []
    }
  }
})

export default useCardsStore