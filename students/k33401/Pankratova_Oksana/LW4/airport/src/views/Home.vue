<template>
    <div>
        <h1 style='text-align: center'>Info</h1>
        <button @click="ShowFlight">Show Flights</button>
        <button @click="ShowPlane">Show Planes</button>
        <button @click="ShowEmployee">Show Employees</button>

        <div v-if="flight_show">
            <h2>Flights</h2>
            <ul v-for="flight in flights">
                <li>Number: <button @click="DetailFlight(flight.id)">{{flight.numbers}}</button> <button @click="DeleteFlight(flight.id)">Delete</button></li>
                <ul>
                    <li>From: {{flight.air_departure}} at {{flight.dep_dt}}</li>
                    <li>To: {{flight.air_arrival}} at {{flight.arr_dt}}</li>
                </ul>
            </ul>
            <a href="/fladd/">Add</a>
        </div>

        <div v-if="flight_detail">
            <h2>Flight number: {{fl.numbers}}</h2>
            <ul>
                <li>Distance: {{fl.distance}}</li>
                <li>From: {{fl.air_departure}} at {{fl.dep_dt}}</li>
                <li>To: {{fl.air_arrival}} at {{fl.arr_dt}}</li>
                <div v-if="fl.plane!=null">
                    <li>Plane: {{fl.plane.number}}</li>
                        <ul>
                            <li>type: {{fl.plane.type}}</li>
                            <li>number of seats: {{fl.plane.num_seats}}</li>
                            <li>company: {{fl.plane.company}}</li>
                        </ul>
                </div>
                <li>Transit landings:</li>
                <ul v-for="tl in fl.transit_land">
                    <li>airport: {{tl.airport}}</li>
                    <li>from {{tl.arr_dt}} till {{tl.dep_dt}}</li>
                </ul>
                <li>Crew:</li>
                <ul v-for="em in fl.employee">
                    <li>{{em.full_name}} - position {{em.position}}</li>
                </ul>

            </ul>


        </div>

        <hr v-if="flight_show && plane_show || flight_show && employee_show">

        <div v-if="plane_show">
            <h2>Planes</h2>
            <ul v-for="plane in planes">
                <li>Number: <button @click="DetailPlane(plane.id)">{{plane.number}}</button> <button @click="DeletePlane(plane.id)">Delete</button></li>
                <ul>
                    <li>Type: {{plane.type}}</li>
                    <li>Number of seats: {{plane.num_seats}}</li>
                    <li>Company: {{plane.company}}</li>
                </ul>
            </ul>
        </div>

        <div v-if="plane_detail">
            <h2>Plane number: {{pl.number}}</h2>
            <ul>
                <li>type: {{pl.type}}</li>
                <li>number of seats: {{pl.num_seats}}</li>
                <li>company: {{pl.company}}</li>
                <li>Flights:</li>
                <ul v-for="fl in pl.flight">
                    <li>flight number: {{fl.numbers}}</li>
                </ul>
            </ul>
        </div>

        <hr v-if="plane_show && employee_show">

        <div v-if="employee_show">
            <h2>Employees</h2>
            <ul v-for="emp in employees">
                <li>Full name: <button @click="DetailEmployee(emp.id)">{{emp.full_name}}</button> <button @click="DeleteEmp(emp.id)">Delete</button></li>
                <ul>
                    <li>Age: {{emp.age}}</li>
                    <li>Passport: {{emp.passport}}</li>
                    <li>In position {{emp.position}} for {{emp.experience}}</li>
                </ul>
            </ul>
        </div>

        <div v-if="employee_detail">
            <h2>{{em.full_name}}</h2>
            <ul>
                <li>passport: {{em.passport}}</li>
                <li>age: {{em.age}}</li>
                <li>position {{em.position}} for {{em.experience}}</li>
                <li>education: {{em.education}}</li>
                <li>Flights:</li>
                <ul v-for="fl in em.flight">
                    <li>flight number: {{fl.numbers}}</li>
                </ul>
            </ul>
        </div>
    </div>
</template>
<script>
    import $ from 'jquery'

    export default {
        name: "Home",
        data() {
            return {
                flights: [],
                fl: null,
                planes: [],
                pl: null,
                employees: [],
                em: null,
                flight_show: false,
                plane_show: false,
                employee_show: false,
                flight_detail: false,
                plane_detail: false,
                employee_detail: false,
            }
        },
        methods: {
            ShowFlight() {
                this.flight_show = !this.flight_show,
                this.flight_detail = false,
                this.plane_detail = false,
                this.employee_detail = false
            },
            ShowPlane() {
                this.plane_show = !this.plane_show,
                this.flight_detail = false,
                this.plane_detail = false,
                this.employee_detail = false
            },
            ShowEmployee() {
                this.employee_show = !this.employee_show,
                this.flight_detail = false,
                this.plane_detail = false,
                this.employee_detail = false
            },
            DetailFlight: function(id) {
                this.flight_show = false,
                this.plane_show = false,
                this.employee_show = false,
                this.flight_detail = true,

                $.ajax({
                    url: 'http://127.0.0.1:8000/flight/'+id.toString()+'/',
                    type: 'GET',
                    success: (response) => {
                        this.fl = response
                    }
                })
            },
            DetailPlane: function(id) {
                this.flight_show = false,
                this.plane_show = false,
                this.employee_show = false,
                this.plane_detail = true,

                $.ajax({
                    url: 'http://127.0.0.1:8000/plane/'+id.toString()+'/',
                    type: 'GET',
                    success: (response) => {
                        this.pl = response
                    }
                })
            },
            DetailEmployee: function(id) {
                this.flight_show = false,
                this.plane_show = false,
                this.employee_show = false,
                this.employee_detail = true,

                $.ajax({
                    url: 'http://127.0.0.1:8000/employee/'+id.toString()+'/',
                    type: 'GET',
                    success: (response) => {
                        this.em = response
                    }
                })
            },
            DeleteFlight: function(id) {
                $.ajax({
                    url: 'http://127.0.0.1:8000/flight/upd_del/'+id.toString()+'/',
                    type: 'DELETE'
                })
            },
            DeletePlane: function(id) {
                $.ajax({
                    url: 'http://127.0.0.1:8000/plane/upd_del/'+id.toString()+'/',
                    type: 'DELETE'
                })
            },
            DeleteEmp: function(id) {
                $.ajax({
                    url: 'http://127.0.0.1:8000/employee/upd_del/'+id.toString()+'/',
                    type: 'DELETE'
                })
            },
        },
        mounted() {

            $.ajax({
                url: 'http://127.0.0.1:8000/flights/',
                type: 'GET',
                success: (response) => {
                    this.flights = response
                }
            }),
            $.ajax({
                url: 'http://127.0.0.1:8000/planes/',
                type: 'GET',
                success: (response) => {
                    this.planes=response
                }
            }),
            $.ajax({
                url: 'http://127.0.0.1:8000/employees/',
                type: 'GET',
                success: (response) => {
                    this.employees=response
                }
            })
        }
    }
</script>