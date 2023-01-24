<template>
  <base-layout>
    <nav-bar />
    <div class="container col-8 justify-content-center py-4" id="regPage">
      <h1 class="text-center">My registrations:</h1>
      <ul v-if="isLoad" class="navbar-nav p-3">
        <li class="nav-item" v-for="reg in regs" :key="reg.id">
          <a @click="updateReg(reg.id)">
            <reg-item v-if="idsReg.includes(reg.id)" :booking="reg.booking_reg" :statusPay="reg.status_pay_reg" :statusReg="reg.status_reg_reg" :roomNumber="reg.room_reg.number_room" :price="reg.rt_reg.price_rt" :roomType="reg.rt_reg.type_rt" :checkOut="reg.check_out_reg" :checkIn="reg.check_in_reg" :nameHotel="reg.hotel_reg.name_hotel" />
          </a>
        </li>
      </ul>
      <div v-if="isStaff">
        <h2 class="text-center">All registrations:</h2>
        <ul v-if="isLoad" class="navbar-nav p-3">
          <li class="nav-item" v-for="reg in regs" :key="reg.id">
            <a @click="updateReg(reg.id)">
              <reg-item v-if="!idsReg.includes(reg.id)" :booking="reg.booking_reg" :statusPay="reg.status_pay_reg" :statusReg="reg.status_reg_reg" :roomNumber="reg.room_reg.number_room" :price="reg.rt_reg.price_rt" :roomType="reg.rt_reg.type_rt" :checkOut="reg.check_out_reg" :checkIn="reg.check_in_reg" :nameHotel="reg.hotel_reg.name_hotel" />
            </a>
          </li>
        </ul>
      </div>
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import NavBar from "@/components/NavBar.vue";
import RegItem from "@/components/RegItem.vue";
import {mapActions, mapState} from "pinia";
import useRegComStore from "@/stores/regCom";

export default {
  name: "RegPage",

  components: { BaseLayout, NavBar, RegItem },

  data() {
    return {
      idsReg: [],
      idUser: localStorage.getItem('idUser'),
      isStaff: localStorage.getItem('isStaff') === "true",
      isLoad: 0
    }
  },

  computed: {
    ...mapState(useRegComStore, ['regs'])
  },

  methods: {
    ...mapActions(useRegComStore, ['loadRegs']),

    updateReg(id) {
      this.$router.push({name: 'update_reg', params: {id}})
    }
  },

  async mounted() {
    await this.loadRegs(localStorage.getItem('accessToken'))
    this.isLoad = this.regs.length

    for (let reg of this.regs) {
      if (reg.user_reg?.id.toString() === this.idUser) {
        this.idsReg.push(reg.id)
      }
    }
  }
}
</script>

<style scoped>
a {
  cursor: pointer;
}

#regPage {
  min-height: 100vh;
}
</style>