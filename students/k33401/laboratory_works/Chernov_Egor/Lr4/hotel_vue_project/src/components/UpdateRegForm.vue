<template>
  <div class="mt-4 p-4" id="updateRegForm">
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="nameHotel">Hotel</span>
      <input v-model="nameHotel" type="text" class="form-control" aria-describedby="nameHotel">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="type">Type</span>
      <input v-model="roomType" type="text" class="form-control" aria-describedby="type">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="numberRoom">Room №</span>
      <input v-model="numberRoom" type="text" class="form-control" aria-describedby="numberRoom">
    </div>
    <div v-if="isStaff" class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="idEmployee">ID Employee</span>
      <input v-model="idEmployee" type="text" class="form-control" aria-describedby="idEmployee">
    </div>
    <div v-if="isStaff" class="input-group mb-3">
      <label class="input-group-text" style="width: 110px" for="statusReg">Status reg</label>
      <select v-model="statusReg" class="form-select" id="statusReg">
        <option value="Taken">Taken</option>
        <option value="Booked">Booked</option>
      </select>
    </div>
    <div class="input-group mb-3">
      <label class="input-group-text" style="width: 110px" for="statusPay">Status pay</label>
      <select v-model="statusPay" class="form-select" id="statusPay">
        <option value="Paid for">Paid for</option>
        <option value="Not paid for">Not paid for</option>
      </select>
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="checkIn">Check in</span>
      <input v-model="checkIn" type="date" class="form-control" aria-describedby="checkIn">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text" style="width: 110px" id="checkOut">Check out</span>
      <input v-model="checkOut" type="date" class="form-control" aria-describedby="checkOut">
    </div>
    <p v-if="!isValid" class="text-center fs-5">You entered the wrong data!</p>
    <a class="nav-link py-1 px-2 fs-5 mt-3 text-center" @click="saveBook" id="saveButton">Save</a>
    <a class="nav-link py-1 px-2 fs-5 mt-3 text-center" @click="deleteBook" id="delButton">Delete</a>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useRegComStore from "@/stores/regCom";
import useHotelsStore from "@/stores/hotels";

export default {
  name: "UpdateRegForm",

  data() {
    return {
      isValid: true,
      idReg: "",
      idHotel: "",
      nameHotel: "",
      idRoomType: "",
      roomType: "",
      idRoom: "",
      numberRoom: "",
      idEmployee: "",
      statusReg: "",
      statusPay: "",
      checkIn: "",
      checkOut: "",
      isStaff: localStorage.getItem('isStaff') === "true"
    }
  },

  computed: {
    ...mapState(useRegComStore, ['regs']),
    ...mapState(useHotelsStore, ['hotels', 'rooms'])
  },

  methods: {
    ...mapActions(useRegComStore, ['loadRegs', 'delReg']),
    ...mapActions(useHotelsStore, ['loadHotels', 'loadRooms']),

    async saveBook() {
      await this.loadHotels()
      for (let hotel of this.hotels) {
        if (this.nameHotel === hotel.name_hotel) {
          this.idHotel = hotel.id
          for (let roomType of hotel.hotel_room_type) {
            if (this.roomType === roomType.type_rt) {
              this.idRoomType = roomType.id
              break
            }
            this.idRoomType = 0
          }
          break
        }
        this.idHotel = 0
      }

      await this.loadRooms(this.idRoomType)
      for (let room of this.rooms.rt_room) {
        if (this.numberRoom.toString() === room.number_room.toString()) {
          this.idRoom = room.id
          break
        }
        this.idRoom = 0
      }

      if (this.idHotel === 0 || this.idRoomType === 0 || this.idRoom === 0) {
        this.isValid = false
        return
      }

      this.isValid = true

      const stReg = (this.statusReg === "Booked") ? "B" : "T"
      const stPay = (this.statusPay === "Not paid for") ? "NP" : "YP"

      this.$emit('saveBook', {
        id_hotel: this.idHotel,
        name_hotel: this.nameHotel,
        id_rt: this.idRoomType,
        rt: this.roomType,
        id_room: this.idRoom,
        number_room: this.numberRoom,
        id_employee: this.idEmployee,
        status_reg: stReg,
        status_pay: stPay,
        check_in: this.checkIn,
        check_out: this.checkOut
      })
    },

    async deleteBook() {
      const accessToken = localStorage.getItem('accessToken')
      const idReg = this.$route.params['id']
      await this.delReg(accessToken, idReg)
      this.$router.push({name: "registrations"})
    }
  },

  async mounted() {
    await this.loadRegs(localStorage.getItem('accessToken'))
    this.idReg = this.$route.params['id']
    for (let reg of this.regs) {
      if (reg.id.toString() === this.idReg) {
        this.idHotel = reg.hotel_reg.id
        this.nameHotel = reg.hotel_reg.name_hotel
        this.idRoomType = reg.rt_reg.id
        this.roomType = reg.rt_reg.type_rt
        this.idRoom = reg.room_reg.id
        this.numberRoom = reg.room_reg.number_room
        this.idEmployee = reg.employee_reg
        this.statusReg = reg.status_reg_reg
        this.statusPay = reg.status_pay_reg
        this.checkIn = reg.check_in_reg
        this.checkOut = reg.check_out_reg
        break
      }
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
}

#updateRegForm {
  background-color: rgba(253, 246, 236, 0.4);
  border-radius: 8px 8px 8px 8px;
  color: black;
}

#saveButton {
  background-color: #E0E7E9;
  border-radius: 8px 8px 8px 8px;
}

#delButton {
  background-color: #ffdfd4;
  border-radius: 8px 8px 8px 8px;
}
</style>