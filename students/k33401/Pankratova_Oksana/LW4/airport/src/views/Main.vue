<template>
    <div class="app">
        <div style="text-align: center">
            <h1> Welcome to FlightControl App!!! </h1>
            <div>
                <button @click=GoLogIn() >Log In</button>   <button @click=GoSignUp() >Sign Up</button>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: "Main",
        components: {
        },
        methods: {
            GoLogIn() {
                this.$router.push({name: "Login"})
            },
            GoSignUp() {
                this.$router.push({name: "Signup"})
            }
        }
    }
</script>