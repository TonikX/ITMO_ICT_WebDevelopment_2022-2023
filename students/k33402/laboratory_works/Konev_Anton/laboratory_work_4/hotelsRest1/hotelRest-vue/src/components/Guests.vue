<template>
  <div class="content">
    <div class="mb-2 d-flex justify-content-between align-items-center">
      <div class="position-relative">
        <custom-input v-model="searchQuery" @send-search="findGuest"></custom-input>
      </div>

      <div class="px-2">
        <button class="btn btn-secondary" @click="isVisible = true">Добавить нового гостя +</button>
      </div>

    </div>
    <div class="table-responsive">
      <table class="table table-responsive table-borderless">

        <thead>
        <tr class="bg-light">
          <th scope="col" width="50%">ФИО</th>
          <th scope="col" width="35%">Статус</th>
          <th scope="col" class="text-end" width="15%">Подробнее...</th>
        </tr>
        </thead>
        <tbody v-for="guest in guests">
        <tr class="">
          <td>
            {{ guest.last_name }} {{ guest.first_name }} {{ guest.middle_name }}
          </td>
          <td :class="[guest.curr_booking !==null ? 'text-success' : 'text-danger']">
            {{ guest.curr_booking !== null ? "заселен" : "выселен" }}
          </td>
          <td class="text-end">
            <button class="btn btn-info" @click="openGuest(guest.id)">Детали</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
  <new-guest v-show="isVisible" @close-modal="isVisible = false"/>
</template>

<script>
import {mapActions} from "pinia";
import useGuestsStore from "@/stores/guests";
import newGuest from "@/components/modal/newGuest.vue"


export default {
  name: 'Guests',
  components: {
    newGuest
  },
  data() {
    return {
      FILTERS: "Фильтры",
      guests: [],
      searchQuery: '',
      isVisible: false,
    }
  },
  methods: {
    ...mapActions(useGuestsStore, ['getGuestsList']),

    async getGuests() {
      this.guests = await this.getGuestsList();
    },

    openGuest(guestId) {
      this.$router.push({name: 'guest', params: {id: guestId}})
    },

    async findGuest() {
      if (this.searchQuery == '') {
        this.guests = await this.getGuestsList();
      } else {
        this.guests = this.guests.filter(guest => (guest.first_name.includes(this.searchQuery) || guest.last_name.includes(this.searchQuery)))
      }
    },

  },
  mounted() {
    this.getGuests()
  }
}
</script>

<style scoped>
.content {
  margin-top: 20px;
  padding: 30px;
}
</style>