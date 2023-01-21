<template>
  <div class="room-wrapper mt-4 p-3">
    <h1>Гость № {{ guest.id }}
    </h1>
    <div class="d-flex justify-content-between mt-4 status-wrapper">
      <h3 class="fw-bold">Статус:
        <span
            :class="[guest.curr_booking ? 'text-success' : 'text-danger']">{{
            guest.curr_booking ? 'Заселен' : 'Выселен'
          }}</span>
      </h3>
      <button class="btn btn-toggle btn-danger" v-if="guest.curr_booking" @click="checkOut">
        {{ 'Выселить' }}
      </button>
    </div>
    <div class="room-body mt-3">
      <p>ФИО: <strong>{{ guest.last_name }} {{ guest.first_name }} {{ guest.middle_name }}</strong></p>
      <p>Город: <strong>{{ guest.city }}</strong></p>
      <p>Пасспорт: <strong>{{ guest.passport }}</strong></p>
      <h3>История бронирований</h3>
      <div class="history-wrapper mb-5">
        <div class="mb-4" v-for="booking in guest.bookings_guest">
          <p>
            <span><b>ID комнаты:</b> {{ booking.room }}</span><br>
            <span><b>ID Администратора:</b> {{ booking.admin }}</span><br>
            <span><b>Дата заезда:</b> {{ dateParser(booking.check_in) }}</span><br>
            <span><b>Дата выезда:</b> {{ dateParser(booking.check_out) }}</span>
          </p>
        </div>
      </div>
      <button class="btn btn-secondary" @click="getBack">Назад</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useRoomsStore from "@/stores/rooms";
import useGuestsStore from "@/stores/guests";
import useUsersStore from "@/stores/users";

export default {
  components: {},
  props: {
    id: String
  },
  data() {
    return {
      guest: {},
      isVisible: false,
      free_time: null,
      adminUsername: null
    }
  },
  methods: {
    ...mapActions(useRoomsStore, ['loadAllRooms', "loadFreeRooms"]),
    ...mapActions(useGuestsStore, ['getSelectedGuest', "sendClosed"]),
    ...mapActions(useUsersStore, ["getAdmin"]),
    async getGuest() {
      this.guest = await this.getSelectedGuest(this.id)
    },

    async checkOut() {
      if (confirm("Вы уверены что хотите выселить гостя?")) {
        await this.sendClosed(this.guest.curr_booking)
        window.location.reload()
      }
    },

    dateParser(string) {
      let date = new Date(string)
      return date.toUTCString()
    },
    getBack() {
      this.$router.push('/guests')
    }
  },
  mounted() {
    this.getGuest()
  }
}
</script>

<style scoped>
p {
  padding: 0;
  margin: 0 0 10px;
}

.history-wrapper {
  margin-top: 30px;
  height: 200px;
  width: 400px;
  display: block;
  overflow-y: scroll;
}

.status-wrapper {
  width: 400px;
}
</style>