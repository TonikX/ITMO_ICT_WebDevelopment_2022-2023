<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add cleaning</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Room</label>
                        <br>
                        <div class="select is-primary">
                            <select v-model="clean_room">
                                
                                <option v-for="clean_room in rooms" :value="clean_room.id"
                                >{{ clean_room.id }}
                                </option>
                                   
                            </select>
                        </div>
                    </div>

                    <div class="field">
                        <label>Cleaner</label>
                        <br>
                        <div class="select is-primary">
                            <select v-model="cleaner_id">
                                <option v-for="cleaner_id in cleaners"
                                    :value="cleaner_id.cleaner_id">
                                    {{ cleaner_id.cleaner_id }} 
                                </option>
                            </select>
                        </div>
                        
                    </div>

                    <div class="field">
                        <label>Date</label>
                        <div class="control">
                            <input type="date" class="input" v-model="date_time">
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
        name: 'AddCleaning',
        data() {
            return {
                
                cleaner_id: '',
                clean_room: '',
                date_time: '',
                cleaners: [],
                rooms: []
            }
        },
        mounted() {
            this.getCleaners(),
            this.getRooms()
        },
        methods: {
            async getCleaners() {
                await axios
                    .get('/hotel/cleaners/')
                    .then(response => {
                        this.cleaners = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            async getRooms() {
                await axios
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

                const cleaning = {
                    cleaner_id: this.cleaner_id,
                    clean_room: this.clean_room,
                    date_time: this.date_time,
                }
                
                await axios
                    .post('/hotel/cleanings/create/', cleaning)
                    .then(response => {
                        toast({
                            message: 'The cleaning was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/cleanings')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            
            
        }
    }
</script>