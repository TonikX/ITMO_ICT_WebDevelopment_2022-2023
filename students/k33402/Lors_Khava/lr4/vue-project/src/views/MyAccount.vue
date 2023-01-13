<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>
            <div class="column is-12">
                <div class="buttons">
                    <button @click="logout()" class="button is-danger">Log out</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'MyAccount',
        methods: {
            async logout() {
                await axios
                    .post('/auth/token/logout/')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                this.$store.commit('removeToken')
                
                this.$router.push('/')
            }
        }
    }
</script>