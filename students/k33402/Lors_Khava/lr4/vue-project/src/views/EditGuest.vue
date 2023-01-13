<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{ guest.first_name }} {{ guest.last_name }}</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="guest.first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="guest.last_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Passport</label>
                        <div class="control">
                            <input type="text" class="input" v-model="guest.passport">
                        </div>
                    </div>

                    <div class="field">
                        <label>City</label>
                        <div class="control">
                            <input type="text" class="input" v-model="guest.city">
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
        name: 'EditGuest',
        data() {
            return {
                guest: {}
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
                
                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const guestID = this.$route.params.id
                await axios
                    .patch(`/hotel/guests/update/${guestID}/`, this.guest)
                    .then(response => {
                        toast({
                            message: 'The guest was updated',
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