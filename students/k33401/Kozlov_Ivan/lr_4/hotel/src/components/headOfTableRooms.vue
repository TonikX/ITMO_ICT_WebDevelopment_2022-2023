<template>
    <col style="width:20%">
    <col style="width:30%">
    <col style="width:30%">
    <col style="width:10%">
    <thead>
    <tr>
        <th scope="col">{{ head1 }}</th>
        <th scope="col">
            {{ head2 }}
            <input v-model="room.places" placeholder="сколько мест?" type="number" class="form-outline mx-1" style="width:30%">
            <button class="btn btn-info btn-sm" @click="sortRoomPage()">Отсортировать</button>
        </th>
        <th scope="col">{{ head3 }}</th>
        <th scope="col">Действия</th>
    </tr>
    </thead>
</template>

<script>
import {mapActions} from 'pinia'
import useRoomsStore from "@/stores/rooms";

export default {
    name: "headOfTableRooms.vue",
    props:{
        head1:{
            type: String,
            required: false,
        },
        head2:{
            type: String,
            required: false,
        },
        head3:{
            type: String,
            required: false,
        },
    },

    data(){
        return{
            room: {
                places: "",
            }
        }
    },

    methods:{
        ...mapActions(useRoomsStore, ["sortRooms"]),

        async sortRoomPage(){
            await this.sortRooms(this.room.places)
        }
    }

}
</script>


