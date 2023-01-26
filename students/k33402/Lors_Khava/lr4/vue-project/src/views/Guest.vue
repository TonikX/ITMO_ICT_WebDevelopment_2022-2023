<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ guest.first_name }} {{ guest.last_name }}</h1>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>
                    <p><strong>First Name: </strong>{{ guest.first_name }}</p>
                    <p><strong>Last Name: </strong>{{ guest.last_name }}</p>
                    <p><strong>City: </strong>{{ guest.city }}</p>
                    <p><strong>Passport: </strong>{{ guest.passport }}</p>
                    <div class="buttons mt-4">
                        <router-link v-if="typeof guest.id !== 'undefined'" 
                        :to="{ name: 'EditGuest', params: { id: guest.id }}" class="button is-light">Edit guest</router-link>
                    </div>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Room book</h2>

                    <p><strong>Reserved room: </strong>{{ guest.room_book }}</p>
                    <p><strong>Check in: </strong>{{ booking.check_in }}</p>
                    <p><strong>Check out: </strong>{{ booking.check_out }}</p>
                    <div class="buttons mt-4">
                        <router-link v-if="typeof guest.id !== 'undefined'" 
                        :to="{ name: 'EditBook', params: { id: guest.id }}" class="button is-light">Edit booking</router-link>
                    </div>
                </div>
            </div>
            <!-- когда сделаешь букинги добавь в mounted getBook, дальше получи get данные о бронировании -->
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Guest',
        data() {
            return {
                guest: {},
                booking: {}
            }
        },
        mounted() {
            this.getGuest()
        },
        methods: {
            async getGuest() {
                this.$store.commit('setIsLoading', true)
                const guestID = this.$route.params.id
                await axios
                    .get(`/hotel/guests/${guestID}/`)
                    .then(response => {
                        this.guest = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                await axios
                    .get(`/hotel/bookings/${guestID}/`)
                    .then(response => {
                        this.booking = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>