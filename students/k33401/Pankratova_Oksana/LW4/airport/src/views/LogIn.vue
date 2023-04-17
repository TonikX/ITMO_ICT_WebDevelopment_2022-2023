<template>
    <div style='text-align: center'>
        <h1>Please enter your login and password</h1>
        <br>
        Login:
        <input v-model='login' type='text' placeholder='Enter your login'/>
        <br>
        Password:
        <input v-model='password' type='password' placeholder='Enter your password'/>
        <br>
        <button @click='Login'>Log in</button>
        <br>
        <br>
        If you don't have an account yet, please
        <button @click='GoSignUp'>sign up</button>
        !
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name : "Login",
        data () {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            Login() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/login/',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        console.log(response),
                        this.$router.push({name: "Home"})
                    }
                })
            },
            GoSignUp() {
                this.$router.push({name: "Signup"})
            }
        }
    }
</script>
