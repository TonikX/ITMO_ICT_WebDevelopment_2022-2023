<template>
  <base-layout>
    <nav-bar />
    <h1>My registrations:</h1>
    <ul v-if="isLoad">
      <li v-for="reg in regs" :key="reg.id">
        <reg-item v-if="reg.user_reg.id.toString() === idUser" :booking="reg.booking_reg" :statusPay="reg.status_pay_reg" :statusReg="reg.status_reg_reg" :roomNumber="reg.room_reg.number_room" :price="reg.rt_reg.price_rt" :roomType="reg.rt_reg.type_rt" :checkOut="reg.check_out_reg" :checkIn="reg.check_in_reg" :nameHotel="reg.hotel_reg.name_hotel" />
      </li>
    </ul>
    <div v-if="isStaff">
      <h1>All registrations:</h1>
      <ul v-if="isLoad">
        <li v-for="reg in regs" :key="reg.id">
          <reg-item v-if="reg.user_reg.id.toString() !== idUser" :booking="reg.booking_reg" :statusPay="reg.status_pay_reg" :statusReg="reg.status_reg_reg" :roomNumber="reg.room_reg.number_room" :price="reg.rt_reg.price_rt" :roomType="reg.rt_reg.type_rt" :checkOut="reg.check_out_reg" :checkIn="reg.check_in_reg" :nameHotel="reg.hotel_reg.name_hotel" />
        </li>
      </ul>
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
      idUser: localStorage.getItem('idUser'),
      isStaff: localStorage.getItem('isStaff') === "true",
      isLoad: 0
    }
  },

  computed: {
    ...mapState(useRegComStore, ['regs'])
  },

  methods: {
    ...mapActions(useRegComStore, ['loadRegs'])
  },

  async mounted() {
    await this.loadRegs(localStorage.getItem('accessToken'))
    this.isLoad = this.regs.length
  }
}
</script>

<style scoped>

</style>