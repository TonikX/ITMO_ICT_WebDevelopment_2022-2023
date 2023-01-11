<template>
    <base-layout>
        <table class="table table-hover table-bordered" style="color: rgb(0, 0, 0)" id="myTable">
        <head-of-table
            head1="Номер комнаты"
            head2="Количество мест"
            head3="Удобства">
        </head-of-table>

        <rooms-card v-for="room in rooms.results"
                    v-bind:facilities="room.type.facilities"
                    v-bind:count_places="room.type.count_places_in_room"
                    v-bind:room_number="room.room_number">
        </rooms-card>

        </table>
    </base-layout>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import BaseLayout from "@/layouts/BaseLayout.vue";
import headOfTable from "@/components/headOfTableRooms.vue";
import roomsCard from "@/components/roomsCard.vue";
import useRoomsStore from "@/stores/rooms";


export default {
    name: "RoomsPage",
    components: {BaseLayout, headOfTable, roomsCard},

    computed: {
        ...mapState(useRoomsStore, ['rooms']),
    },

    methods: {
        ...mapActions(useRoomsStore, ["loadRooms"])
    },

    mounted() {
        this.loadRooms()
    }


}
</script>

<style scoped>

</style>
