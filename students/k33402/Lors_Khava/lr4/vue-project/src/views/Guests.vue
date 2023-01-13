<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Guests</h1>

                <router-link to="/guests/create">Add guest</router-link>
                
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Passport</th>
                            <th>City</th>
                            <th>Reserved room</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="guest in guests"
                            v-bind:key="guest.id">
                                <td>{{ guest.first_name }}</td>
                                <td>{{ guest.last_name }}</td>
                                <td>{{ guest.passport }}</td>
                                <td>{{ guest.city }}</td>
                                <td>{{ guest.room_book }}</td>
                                <td>
                                    <router-link :to="{ name: 'Guest', params: { id: guest.id }}">Details</router-link>
                                </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Guest',
        data() {
            return {
                guests: []
            }
        },
        mounted() {
            this.getGuests()
        },
        methods: {
            async getGuests() {
                axios
                    .get('/hotel/guests/')
                    .then(response => {
                        this.guests = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>