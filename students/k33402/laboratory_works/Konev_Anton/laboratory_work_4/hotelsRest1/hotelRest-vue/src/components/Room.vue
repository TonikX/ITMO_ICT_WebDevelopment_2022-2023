<template>
  <div class="room-wrapper mt-4 p-3">
    <h1>Комната № {{ room.number }}
    </h1>
    <div class="d-flex justify-content-between mt-4 status-wrapper">
      <h3 class="fw-bold">Статус:
        <span :class="[room.is_free ? 'text-success' : 'text-danger']">{{ room.is_free ? 'Свободно' : 'Занято' }}</span>
      </h3>
      <button v-if="room.is_free" class="btn btn-toggle btn-primary" @click="isVisible = true"
              :class="[room.is_free ? 'btn-primary' : 'btn-danger']">
        {{ 'Заселить' }}
      </button>
      <button v-if="!room.is_free" class="btn btn-toggle btn-danger" @click="checkOut">
        {{ 'Выселить' }}
      </button>
    </div>
    <div class="room-body mt-3">
      <p>Тип: <strong>{{ room.room_type }}</strong></p>
      <p>Этаж: <strong>{{ room.floor }}</strong></p>
      <p>Номер телефона: <strong>{{ room.phone }}</strong></p>
      <p class="mb-5">Цена/день: <strong>₽ {{ parseFloat(room.price).toFixed(2) }}</strong></p>
      <h3>История бронирований</h3>
      <div class="history-wrapper mb-5">
        <div v-for="booking in room.bookings" class="mb-4">
          <h5>{{ booking.guest.last_name }} {{ booking.guest.first_name }} {{ booking.guest.middle_name }}</h5>
          <p>
            <span><b>Номер паспорта:</b> {{ booking.guest.passport }}</span><br>
            <span><b>Город:</b> {{ booking.guest.city }}</span><br>
            <span><b>Дата заезда:</b> {{ dateParser(booking.check_in) }}</span><br>
            <span><b>Дата выезда:</b> {{ dateParser(booking.check_out) }}</span>
          </p>
        </div>
      </div>
      <button class="btn btn-secondary" @click="getBack">Назад</button>
    </div>

  </div>
  <CheckIn v-show="isVisible" @close-modal="isVisible = false"
           :room="[room.id, JSON.parse(JSON.stringify(free_time))]"/>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useRoomsStore from "@/stores/rooms";
import CheckIn from "@/components/modal/CheckIn.vue";
import useGuestsStore from "@/stores/guests";

export default {
  components: {
    CheckIn
  },
  props: {
    id: String
  },
  data() {
    return {
      room: {},
      isVisible: false,
      free_time: null
    }
  },
  methods: {
    ...mapActions(useRoomsStore, ['loadAllRooms', "loadFreeRooms"]),
    ...mapActions(useGuestsStore, ['getGuestsList', "sendClosed"]),
    async getSelectedRoom() {
      const rooms = await this.loadAllRooms()
      for (let i = 0; i < rooms.length; i++) {
        if (rooms[i].id === parseInt(this.id)) {
          this.room = rooms[i]
          break
        }
      }
    },
    async getFreeRange() {
      let free = await this.loadFreeRooms()
      free = free.filter(room => room.id == this.id)
      this.free_time = free[0].free_time[0]
    },
    dateParser(string) {
      let date = new Date(string)
      return date.toUTCString()
    },
    getBack() {
      this.$router.push('/')
    },
    async checkOut() {
      if (confirm('Вы действительно хотите выселить гостя?')) {
        await this.sendClosed(this.room.curr_booking)
        window.location.reload()
      }
      //
    }
  },

  mounted() {
    this.getSelectedRoom()
    this.getFreeRange()
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