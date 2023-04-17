<template>
    <div style='text-align: center'>
        <h1>Please enter your data to sign up</h1>
        Login:
        <input v-model='login' type='text' placeholder='Enter your login'/>
        <br>
        Email:
        <input v-model='email' type='email' placeholder='Enter your email'/>
        <br>
        Password:
        <input v-model='password' type='password' placeholder='Enter your password'/>
        <br>
        <button @click="Signup">Sign up</button>
        <br>
        <br>
        If you have already an account yet, please
        <button @click='GoLogIn'>log in</button>
        !
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Signup",
        data () {
            return {
                login: '',
                password: '',
                email: '',
            }
        },
        methods: {
            Signup() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/users/',
                    type: 'POST',
                    data: {
                        username: this.login,
                        password: this.password,
                        email: this.email
                    },
                    success: (response) => {
                        console.log(response)
                    },
                    error: (response) => {
                        console.log(response)
                    },
                })
            },
            GoLogIn() {
                this.$router.push({name: "Login"})
            }
        }
    }
</script>