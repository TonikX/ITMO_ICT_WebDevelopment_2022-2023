<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>
            
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="first_name" name="first_name" class="input" v-model="first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="last_name" name="last_name" class="input" v-model="last_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="phone" name="phone" class="input" v-model="phone">
                        </div>
                    </div>
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="username" name="usernsme" class="input" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
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

    import {toast} from 'bulma-toast'

    export default {
        name: 'SignUp',
        data() {
            return {
                first_name: '',
                last_name: '',
                phone: '',
                username: '', 
                password1: '',
                password2: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                this.errors = []
                if (this.username === '') {
                    this.errors.push('The username is missing')
                }
                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }
                if (this.password1 !== this.password2) {
                    this.errors.push('The password are not matching')
                }
                if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)
                    const formData = {
                        first_name: this.first_name,
                        last_name: this.last_name,
                        phone: this.phone,
                        username: this.username,
                        password: this.password1
                    }
                    await axios
                        .post('/auth/users/', formData)
                        .then(response => {
                            toast({
                                message: 'Account was created, please log in',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })
                            this.$router.push('/log-in')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                            } else if (error.message) {
                                this.errors.push('Something went wrong. Please try again!')
                            }
                        })
                    
                    this.$store.commit('setIsLoading', false)
                }
            }
        }
    }
</script>