<template>
    <div id="app">
        <Menu @showLogin="setLogin(true)"></Menu>
        <Login v-if="login" @hideLogin="setLogin(false)"></Login>
        <Achievement v-if="achievement" @hideLogin="setLogin(false)"></Achievement>
        <router-view/>
    </div>
</template>

<script>
    import Menu from '@/components/Menu.vue'
    import Login from '@/components/Login.vue'
    import Competition from '@/components/Competition.vue'

    export default {
        name: 'app',
        components: {
            Menu,
            Login,
            Competition,
        },
        data() {
            return {
                login: false,
                comp: false,
            }
        },
        created() {
            if (sessionStorage.getItem("token")) {
                this.$store.commit("set_auth", true)
                $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
                });
                this.$store.dispatch('user_info')
            } else {
                this.$store.commit("set_auth", false)
            }
        },
        methods: {
            setLogin(value) {
                this.login = value
            }

        }
    }
</script>

<style>
    body {
        background: #e6ecf0;
    }
</style>
