<template>
  <div class="p-3 pt-2" id="regRoomForm">
    <div v-if="isBooked" class="">
      <p class="text-center fs-2 m-0">Success!</p>
      <a class="nav-link py-1 px-2 fs-5 mt-3 text-center" @click="goHome" id="actButton">Home</a>
    </div>
    <div v-else class="text-center">
      <p class="fs-2">{{ nameHotel }}</p>
      <p class="fs-2">Type: <span class="fs-3">{{ typeRoom }}</span></p>
      <p class="fs-2">Number room: <span class="fs-3">{{ numberRoom }}</span></p>
      <div class="input-group mb-3">
        <span class="input-group-text" style="width: 110px" id="checkIn">Check in</span>
        <input v-model="checkIn" type="date" class="form-control" aria-describedby="checkIn">
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" style="width: 110px" id="checkOut">Check out</span>
        <input v-model="checkOut" type="date" class="form-control" aria-describedby="checkOut">
      </div>
      <a class="nav-link py-1 px-2 fs-5 mt-3" @click="book" id="actButton">Book</a>
      <p v-if="isBadReq" class="row my-2">Incorrect data!</p>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useRegComStore from "@/stores/regCom";

export default {
  name: "RegRoomForm",

  props: {
    idHotel: {
      type: Number,
      required: true
    },
    nameHotel: {
      type: String,
      required: true
    },
    idRoomType: {
      type: Number,
      required: true
    },
    typeRoom: {
      type: String,
      required: true
    },
    numberRoom: {
      type: Number,
      required: true
    },
  },

  data() {
    return {
      checkIn: "",
      checkOut: "",
      isBooked: false,
      isBadReq: false
    }
  },

  computed: {
    ...mapState(useRegComStore, ['regs'])
  },

  methods: {
    ...mapActions(useRegComStore, ['createReg']),

    book() {
      const accessToken = localStorage.getItem('accessToken')
      const idUser = localStorage.getItem('idUser')
      const idRoom = localStorage.getItem('idBookRoom')
      const statusReg = "B"
      const statusPay = "NP"
      const booking = new Date().toJSON().slice(0, 10)

      this.createReg(accessToken, idUser, this.idHotel, this.idRoomType, idRoom, statusReg, statusPay, this.checkIn, this.checkOut, booking)

      if (this.regs) {
        this.isBooked = true
        this.isBadReq = false
      } else {
        this.isBadReq = true
      }
    },

    goHome() {
      this.$router.push({name: "hotels"})
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
}

#regRoomForm {
  background-color: rgba(253, 246, 236, 0.4);
  border-radius: 8px 8px 8px 8px;
  color: black;
}

#actButton {
  background-color: #E0E7E9;
  border-radius: 8px 8px 8px 8px;
}
</style>