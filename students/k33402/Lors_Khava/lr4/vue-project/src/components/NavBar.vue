<template>
    <nav class="navbar is-dark">
        
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <h1><strong>Hotel</strong></h1>
            </router-link>
        </div>  

        <div class="navbar-menu">
            <router-link to="/guests" class="navbar-item"><strong>Guests</strong></router-link>
            <router-link to="/cleanings" class="navbar-item"><strong>Cleanings</strong></router-link>
            <div class="navbar-end">
                <template v-if="$store.state.isAuthenticated">
                    <router-link to="/guests/create" class="navbar-item"><strong>Add guest</strong></router-link>
                    <router-link to="/cleanings/create" class="navbar-item"><strong>Add cleaning</strong></router-link>
                    <router-link to="/bookings/create" class="navbar-item"><strong>Create booking</strong></router-link>
                </template>
                
                <div class="navbar-item">
                    <div class="buttons">

                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-success"><strong>Sign up</strong></router-link>
                            <router-link to="/log-in" class="button is-light">Log in</router-link>
                        </template>
                        
                        <template v-else>
                            <router-link to="/my-account" class="button-success"><strong>My account</strong></router-link>
                        </template>

                    </div>
                </div>
            </div>
        </div>
        
    </nav>
</template>

<script>
    export default {
        name: 'NavBar'
    }
</script>