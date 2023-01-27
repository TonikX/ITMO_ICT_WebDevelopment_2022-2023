<template>
  <div class="content ">
    <div class="mb-2 d-flex justify-content-between align-items-center">

      <div class="position-relative">
        <custom-input v-model="searchQuery" @send-search="findRoom"></custom-input>
      </div>

      <div class="px-2">
        <select-list
            style="width: 120px"
            class="mx-5 border-0"
            v-model="sortName"
            :options="sortOptions"
        >
        </select-list>
        <filters-list
            style="width: 100px"
            class=" border-0"
            v-model="filterName"
            :options="filterOptions"
        >
        </filters-list>

      </div>

    </div>
    <div class="table-responsive">
      <table class="table table-responsive table-borderless">

        <thead>
        <tr class="bg-light">
          <th scope="col" width="10%">№ комнаты</th>
          <th scope="col" width="15%">Этаж</th>
          <th scope="col" width="15%">Тип</th>
          <th scope="col" width="20%">Телефон</th>
          <th scope="col" class="text-start" width="15%"><span>Цена/день</span></th>
          <th scope="col" width="20%">Статус</th>
          <th scope="col" class="text-end" width="15%">Подробнее...</th>
        </tr>
        </thead>
        <tbody v-for="room in rooms">
        <tr class="">
          <td>{{ room.number }}</td>
          <td>{{ room.floor }}</td>
          <td>{{ room.room_type }}</td>
          <td>{{ room.phone }}</td>
          <td class="text-start"><span class="fw-bolder">₽ {{ parseFloat(room.price).toFixed(2) }}</span></td>
          <td class="fw-bold" :class="[room.is_free ? 'text-success' : 'text-danger']">
            {{ room.is_free ? 'Свободно' : 'Занято' }}
          </td>
          <td class="text-end">
            <button class="btn btn-info" @click="openRoom(room.id)">Детали</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {mapActions} from "pinia";
import useRoomsStore from "@/stores/rooms";
import useUsersStore from "@/stores/users";
import FiltersList from "@/components/my-components/FiltersList.vue";
import Guest from "@/components/modal/newGuest.vue";


export default {
  name: 'Rooms',
  components: {Guest},
  data() {
    return {
      rooms: [],
      searchQuery: '',
      sortName: '',
      filterName: '',
      filterOptions: [
        {value: 'ANY', name: 'Любой'},
        {value: 'TRIPLE', name: 'TRIPLE'},
        {value: 'DOUBLE', name: 'DOUBLE'},
        {value: 'SINGLE', name: 'SINGLE'},
      ],
      sortOptions: [
        {value: 'default', name: 'Default'},
        {value: 'number ASC', name: 'По номеру (ASC)'},
        {value: 'number DESC', name: 'По номеру (DESC)'},
        {value: 'floor ASC', name: 'По этажу (ASC)'},
        {value: 'floor DESC', name: 'По этажу (DESC)'},
        {value: 'price ASC', name: 'По цене (ASC)'},
        {value: 'price DESC', name: 'По цене (DESC)'},
      ],
    }
  },
  methods: {
    ...mapActions(useRoomsStore, ['loadAllRooms']),
    ...mapActions(useUsersStore, ['fetchUser']),

    async getRooms() {
      this.rooms = await this.loadAllRooms();
      // console.log(this.rooms)
    },

    openRoom(roomId) {
      this.$router.push({name: 'room', params: {id: roomId}})
    },

    async findRoom() {
      if (this.searchQuery == '') {
        this.rooms = await this.loadAllRooms();
      } else {
        this.rooms = this.rooms.filter(room => room.number.includes(this.searchQuery))
      }
    },

  },
  mounted() {
    this.getRooms()
    this.fetchUser()

  },
  watch: {
    async sortName(sortName) {
      if (sortName == 'default') {
        this.rooms = await this.loadAllRooms()
      } else {
        const sortSplit = sortName.split(' ')
        const type = sortSplit[0]
        const order = sortSplit[1]
        this.rooms.sort((a, b) => a[type] - b[type])
        if (order === 'DESC') {
          this.rooms.reverse()
        }
      }
    },

    async filterName(filterName) {
      this.rooms = await this.loadAllRooms()
      if (filterName !== 'ANY') {

        this.rooms = this.rooms.filter(room => room.room_type == filterName)
      } else {
        this.rooms = await this.loadAllRooms()
      }

    },

  }
}
</script>

<style scoped>
.content {
  margin-top: 20px;
  padding: 30px;
}

.dropdown-input label {
  display: block;
  padding: 3px 20px 0 20px;
  clear: both;
  font-weight: 400;
  line-height: 1.42857143;
  color: #333;
  white-space: nowrap;
}


</style>