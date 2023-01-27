<template>
  <transition name="modal">
    <div class="modal-mask" @click="$emit('close-modal')" @mouseenter="getFreeRoom">
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <form type="submit" @submit.prevent="sendForm">
            <span class=""><b>Выберите гостя</b></span>
            <div style="height: 70px; overflow-y: scroll; margin-bottom: 30px">
              <div v-for="guest in freeGuests" class="my-2">
                <input type="radio"
                       class="choice"
                       name="radButton"
                       :value="guest.id"
                       v-model="guestId"
                       required
                >
                <label class="mx-3">{{ guest.last_name }} {{ guest.first_name }} {{ guest.middle_name }}</label>
              </div>
            </div>

            <div class="d-flex">
              <div class="w-50 me-4">
                <label class="my-3"><b>Дата и время заезда</b></label>
                <input type="date"
                       class="form-control"
                       :max="rangeEnd" :min="rangeStart"
                       v-model="chosenStart.dateStart"
                       autocomplete="off"
                       required
                >
                <input type="time"
                       class="form-control my-4"
                       v-model="chosenStart.timeStart"
                       autocomplete="off"
                       required
                >
              </div>
              <div class="w-50">
                <label class="my-3"><b>Дата и время выезда</b></label>
                <input type="date"
                       class="form-control"
                       :max="rangeEnd" :min="rangeStart"
                       v-model="chosenEnd.dateEnd"
                       autocomplete="off"
                       required
                >
                <input type="time"
                       class="form-control my-4"
                       v-model="chosenEnd.timeEnd"
                       autocomplete="off"
                       required
                >
              </div>
            </div>

            <div class="d-grid gap-2">
              <button type="submit" class="btn btn-primary btn-block p-2 my-4 fw-semibold"
                      @click="$emit('close-modal')">Заселить
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>

import {mapActions, mapState} from "pinia";
import useGuestsStore from "@/stores/guests";
import useRoomsStore from "@/stores/rooms";
import useUsersStore from "@/stores/users";

export default {
  name: 'CheckIn',
  props: {
    room: {
      roomId: {
        type: Number
      },
      free_time: {
        type: Array
      }
    }
  },
  data() {
    return {
      freeGuests: [],
      guestId: null,
      checkinGuest: null,
      rangeStart: null,
      rangeEnd: null,
      chosenStart: {
        dateStart: null,
        timeStart: null,
      },
      chosenEnd: {
        dateEnd: null,
        timeEnd: null,
      },
      booking: {
        guest: {},
        check_in: null,
        check_out: null,
        room: null,
        admin: null,
      }
    }
  },
  methods: {
    ...mapActions(useGuestsStore, ['getGuestsList', "getSelectedGuest", "sendBooking"]),
    ...mapActions(useRoomsStore, ['loadFreeRooms']),
    ...mapActions(useUsersStore, ['fetchUser']),
    async getFreeGuests() {
      let tmp = await this.getGuestsList()
      this.freeGuests = JSON.parse(JSON.stringify(tmp.filter(guest => !guest.curr_booking)))
    },
    getFreeRoom() {
      this.rangeStart = this.handleDate(this.room[1][0])
      this.rangeEnd = this.handleDate(this.room[1][1])
      this.booking.room = parseInt(this.room[0])
    },
    handleDate(timestamp) {
      return (new Date(timestamp)).toISOString().substring(0, 10)
    },
    async sendForm() {
      await this.buildData()
      let data = JSON.parse(JSON.stringify(this.booking))
      const res = await this.sendBooking(data, this.token)
      window.location.reload()
    },
    async buildData() {
      await this.defineGuest()
      await this.defineAdmin()
      this.booking.check_in = this.mergeDate(this.chosenStart.dateStart, this.chosenStart.timeStart)
      this.booking.check_out = this.mergeDate(this.chosenEnd.dateEnd, this.chosenEnd.timeEnd)
    },
    async defineAdmin() {
      const {id} = await this.fetchUser()
      this.booking.admin = parseInt(id)
    },
    mergeDate(date, time) {
      return `${date}T${time}Z`
    },
    async defineGuest() {
      this.booking.guest = this.guestId
    }
  },
  computed: {
    ...mapState(useUsersStore, ["token"])
  },
  created() {
    this.getFreeGuests()
  }
}
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 35%;
  height: fit-content;
  margin: 0 auto;
  padding: 50px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

h1 {
  margin-bottom: 30px;
}

.choice {
  margin-left: 2px;
  transform: scale(1.3);
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

</style>

