<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit booking</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Room</label>
                        <div class="control">
                            <input type="text" class="input" v-model="booking.room">
                        </div>
                    </div>

                    <div class="field">
                        <label>Check in</label>
                        <div class="control">
                            <input type="date" class="input" v-model="booking.check_in">
                        </div>
                    </div>

                    <div class="field">
                        <label>Check out</label>
                        <div class="control">
                            <input type="date" class="input" v-model="booking.check_out">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'EditBook',
        data() {
            return {
                booking: {}
            }
        },
        mounted() {
            this.getBooking()
        },
        methods: {
            async getBooking() {
                this.$store.commit('setIsLoading', true)
                const bookingID = this.$route.params.id
                await axios
                    .get(`/hotel/bookings/${bookingID}/`)
                    .then(response => {
                        this.booking = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const bookingID = this.$route.params.id
                await axios
                    .patch(`/hotel/bookings/update/${bookingID}/`, this.booking)
                    .then(response => {
                        toast({
                            message: 'The booking was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push(`/guests/${bookingID}`)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>