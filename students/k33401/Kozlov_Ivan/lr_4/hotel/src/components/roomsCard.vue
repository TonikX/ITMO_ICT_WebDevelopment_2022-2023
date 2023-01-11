<template>
    <tbody class="rooms">
    <tr>
        <td>{{ room_number }}</td>
        <td>{{ count_places }}</td>
        <td>{{ facilities }}</td>
        <td>
            <a href="/room_book">
                <button v-bind:id="room_number" type="button" class="btn btn-warning" @click="currRoom">Бронирования</button>
            </a>
        </td>

    </tr>
    </tbody>

</template>

<script>
export default {
    name: "RoomsCard",
    props:{
        room_number:{
            type: Number,
            required: true
        },
        count_places:{
            type: Number,
            required: true
        },
        facilities:{
            type: String,
            required: true
        },
    },
    methods:{
        currRoom: async function (event) {
            localStorage.current_room = event.originalTarget.id
        },
    }
}
</script>
