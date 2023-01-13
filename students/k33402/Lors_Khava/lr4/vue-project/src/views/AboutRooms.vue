<template>
  <div class="mb-5">
    <h1 class="has-text-centered">This is page about available rooms</h1>
  </div>
  <div class="container">
    <div class="columns is-multiline">
      
      <RoomList v-for="room in rooms" :key="room.id" :room="room" class="column is-one-third"/>
    
    </div>
  </div>
</template>

<script>
import RoomList from '@/components/RoomList.vue';
import axios from 'axios'

export default {
  name: "Rooms",
  data() {
    return {
      rooms: []
    }
  },
  mounted() {
    this.getRooms()
  },
  components: {RoomList},
  methods: {
    async getRooms() {
      axios
        .get('/hotel/rooms/')
        .then(response => {
            this.rooms = response.data
        })
        .catch(error => {
            console.log(error)
        })
    }
  }
}
</script>
