<template>
    <div style='text-align: center'>
        <input v-model='numbers' type='text' placeholder='number'/>
        <br>
        <input v-model='distance' type='text' placeholder='distance'/>
        <br>
        <input v-model='air_departure' type='text' placeholder='airport departure'/>
        <br>
        <input v-model='air_arrival' type='text' placeholder='airport arrival'/>
        <br>
        <input v-model='dep_dt' type='datetime' placeholder='departure date and time'/>
        <br>
        <input v-model='arr_dt' type='datetime' placeholder='arrival date and time'/>
        <br>
        <input v-model='plane' placeholder='plane'/>
        <br>
        <input v-model='transit_land' placeholder='transit landings'/>
        <br>
        <button @click="AddFlight">Add</button>
    </div>
</template>
<script>
    import $ from 'jquery'

    export default {
        name: "FlightAdd",
        data() {
            return {
                numbers: null,
                distance: null,
                air_departure: null,
                air_arrival: null,
                dep_dt: null,
                arr_dt: null,
                plane: null,
                transit_land: null,
            }
        },
        methods: {
            AddFlight() {

                $.ajax({
                    url: 'http://127.0.0.1:8000/flight/create/',
                    type: 'POST',
                    data: {
                        numbers: this.numbers,
                        distance: this.distance,
                        air_departure: this.air_departure,
                        air_arrival: this.air_arrival,
                        dep_dt: this.dep_dt,
                        arr_dt: this.arr_dt,
                        plane: this.plane,
                        transit_land: this.transit_land,
                    },
                })
            },
        }
    }
</script>