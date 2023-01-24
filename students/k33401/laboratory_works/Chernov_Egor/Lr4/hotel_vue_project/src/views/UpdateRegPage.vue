<template>
  <base-layout>
    <nav-bar />
    <div class="container col-5 py-4" id="updateRegPage">
      <h1 class="text-center">Change registration</h1>
      <update-reg-form @saveBook='onSaveBook' />
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import NavBar from "@/components/NavBar.vue";
import UpdateRegForm from "@/components/UpdateRegForm.vue";
import {mapActions, mapState} from "pinia";
import useRegComStore from "@/stores/regCom";

export default {
  name: "UpdateRegPage",

  components: { NavBar, UpdateRegForm, BaseLayout },

  computed: {
    ...mapState(useRegComStore, ['regs'])
  },

  methods: {
    ...mapActions(useRegComStore, ['updateReg']),

    async onSaveBook(data) {
      const accessToken = localStorage.getItem('accessToken')
      const idReg = this.$route.params['id']
      const idUser = localStorage.getItem('idUser')
      const booking = new Date().toJSON().slice(0, 10)
      await this.updateReg(accessToken, idReg, idUser, data.id_hotel, data.id_rt, data.id_room, data.id_employee, data.status_reg, data.status_pay, data.check_in, data.check_out, booking)
    }
  }
}
</script>

<style scoped>
#updateRegPage {
  min-height: 100vh;
}
</style>