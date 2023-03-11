<template>
  <div v-if="user" class="container w-75">
    <h1 class="m-5">Staff</h1>
    <table class="table bg-secondary-own text-main-own">
      <thead>
      <tr>
        <th scope="col">Username</th>
        <th scope="col">Email</th>
        <th scope="col">Is Moderator</th>
        <th v-if="user.is_staff" scope="col">Edit</th>
      </tr>
      </thead>
      <tbody id="staffTable">
      <tr v-for="s in staff">
        <td>{{ s.username }}</td>
        <td>{{ s.email }}</td>
        <td>{{ s.is_staff }}</td>
        <td v-if="user.is_staff">
          <button class="btn btn-primary" data-bs-toggle="modal" v-on:click="fillModal(s.username)" data-bs-target="#editModal">Edit</button>
        </td>
      </tr>
      </tbody>
    </table>
    <staff-modal></staff-modal>
  </div>

</template>

<script>

import StaffModal from "@/components/StaffModal.vue";
import {mapActions, mapState} from "pinia/dist/pinia";
import useBazzarStore from "@/stores/bazzar";

export default {
  name: "Staff",
  components: {StaffModal},

  computed: {
    ...mapState(useBazzarStore, ['staff', 'user'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['loadStaff']),
    fillModal: function (username) {
      document.getElementById('editModalLabel').textContent = username
    }
  },
  mounted() {
    this.loadStaff()
    if (!this.user) {
      document.location = document.location.origin
    }
  }
}
</script>

<style scoped>

</style>