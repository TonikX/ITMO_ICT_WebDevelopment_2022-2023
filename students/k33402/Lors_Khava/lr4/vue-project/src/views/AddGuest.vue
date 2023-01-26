<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add guest</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="last_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Passport</label>
                        <div class="control">
                            <input type="text" class="input" v-model="passport">
                        </div>
                    </div>

                    <div class="field">
                        <label>City</label>
                        <div class="control">
                            <input type="text" class="input" v-model="city">
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
        name: 'AddGuest',
        data() {
            return {
                first_name: '',
                last_name: '',
                passport: '',
                city: ''
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const guest = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    passport: this.passport,
                    city: this.city
                }
                await axios
                    .post('/hotel/guests/create/', guest)
                    .then(response => {
                        toast({
                            message: 'The guest was added',
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
            }
        }
    }
</script>