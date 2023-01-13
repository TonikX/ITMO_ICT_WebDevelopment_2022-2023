<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Create booking</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Room</label>
                        <br>
                        <div class="select is-primary">
                            <select v-model="room">
                                <template v-for="room in rooms" :value="room.id">
                                    <option 
                                    v-if="room.status === '+'" :class="room.status"
                                    >{{ room.id }}
                                    </option>
                                </template>
                            </select>
                        </div>
                    </div>

                    <div class="field">
                        <label>Guest</label>
                        <br>
                        <div class="select is-primary">
                            <select v-model="guest">
                                <option v-for="guest in guests"
                                    :value="guest.id">
                                    {{ guest.first_name }} {{ guest.last_name }}
                                </option>
                            </select>
                        </div>
                        
                    </div>

                    <div class="field">
                        <label>Check in</label>
                        <div class="control">
                            <input type="date" class="input" v-model="check_in">
                        </div>
                    </div>

                    <div class="field">
                        <label>Check out</label>
                        <div class="control">
                            <input type="date" class="input" v-model="check_out">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
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
        name: 'AddBooking',
        data() {
            return {
                
                guest: '',
                room: '',
                check_in: '',
                check_out: '',
                guests: [],
                rooms: []
            }
        },
        mounted() {
            this.getGuests(),
            this.getRooms()
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
            },
            async getRooms() {
                axios
                    .get('/hotel/rooms/')
                    .then(response => {
                        this.rooms = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const booking = {
                    guest: this.guest,
                    room: this.room,
                    check_in: this.check_in,
                    check_out: this.check_out
                }

                await axios
                    .post('/hotel/bookings/create/', booking)
                    .then(response => {
                        toast({
                            message: 'The booking was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/guests')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            
            
        }
    }
</script>