<template>
  <div v-if="isBooked" class="container">
    <h1 class="row my-2">Registration</h1>
    <h4 class="row my-2">Success!</h4>
  </div>
  <div v-else class="container">
    <h1 class="row my-2">Registration</h1>
    <h4 class="row my-2">{{ nameHotel }}</h4>
    <h4 class="row my-2">{{ typeRoom }}</h4>
    <h4 class="row my-2">Number room {{ numberRoom }}</h4>
    <input class="col my-2 me-2" v-model="checkIn" type="date" placeholder="Check in" >
    <input class="col my-2" v-model="checkOut" type="date" placeholder="Check out" >
    <button class="row my-2" @click="book">Book</button>
    <p v-if="isBadReq" class="row my-2">Incorrect data!</p>
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
    }
  }
}
</script>

<style scoped>

</style>