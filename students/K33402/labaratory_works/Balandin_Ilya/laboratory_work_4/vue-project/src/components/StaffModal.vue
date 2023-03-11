<template>
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="editModalLabel">Ivanov Ivan</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <select class="form-select" aria-label="Default select example" id="positionModal">
            <option value="true">moderator</option>
            <option value="false">support</option>
          </select>
        </div>
        <div class="modal-footer">
          <p id="staffIdModal" hidden></p>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" id="dismissModal" v-on:click="dismissModal()" class="btn btn-danger">Dismiss</button>
          <button type="button" id="saveModal" v-on:click="updateModal()" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useBazzarStore from "@/stores/bazzar";
import {mapActions, mapState} from 'pinia'
export default {
  name: "StaffModal",
  computed: {
    ...mapState(useBazzarStore, ['staff', 'token'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['deleteStaff', 'updateStaff']),
    dismissModal: async function () {
      const username = document.getElementById('editModalLabel').textContent
      const response = await this.deleteStaff(username, this.token)
      window.location.reload()
    },
    updateModal: async function () {
      const username = document.getElementById('editModalLabel').textContent
      const position = Boolean(document.getElementById('positionModal').value)
      const response = await this.updateStaff(username, this.token, position)
      window.location.reload()
    }
  },
}
</script>

<style scoped>

</style>