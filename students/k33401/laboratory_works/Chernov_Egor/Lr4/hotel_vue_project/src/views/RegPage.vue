<template>
  <base-layout>
    <nav-bar />
    <h1>My registrations:</h1>
    <ul v-if="regs.length !== 0">
      <li v-for="reg in regs" :key="reg.id">
        <reg-item :booking="reg.booking_reg" :statusPay="reg.status_pay_reg" :statusReg="reg.status_reg_reg" :roomNumber="reg.room_reg.number_room" :price="reg.rt_reg.price_rt" :roomType="reg.rt_reg.type_rt" :checkOut="reg.check_out_reg" :checkIn="reg.check_in_reg" :nameHotel="reg.hotel_reg.name_hotel" />
      </li>
    </ul>
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

  computed: {
    ...mapState(useRegComStore, ['regs'])
  },

  methods: {
    ...mapActions(useRegComStore, ['loadRegs'])
  },

  mounted() {
    this.loadRegs(localStorage.getItem('accessToken'))
  }
}
</script>

<style scoped>

</style>