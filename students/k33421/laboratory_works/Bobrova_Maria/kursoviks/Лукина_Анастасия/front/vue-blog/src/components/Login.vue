<template>
    <div class="" id="loginModal">
        <div class="modal-dialog modal-dialog-centered auth-modal">
            <div class="modal-content">
                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title">Вход</h4>
                    <button @click="close" type="button" class="close" data-dismiss="modal">
                        &times;
                    </button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <p>{{mess}}</p>
                    <input type="text" placeholder="Логин" value="" v-model="user.username">
                    <input type="password" placeholder="Пароль" value="" v-model="user.password">
                    <button type="button" @click="setLogin">Войти</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                user: {
                    username: "",
                    password: ""
                },
                mess: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: this.$store.getters.get_url_server + 'auth/token/login/',
                    type: "POST",
                    data: {
                        username: this.user.username,
                        password: this.user.password
                    },
                    success: (response) => {
                        sessionStorage.setItem("token", response.auth_token)
                        this.$store.commit("set_auth", true)

                        $.ajaxSetup({
                            headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
                        });
                        this.close()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            this.mess = response.responseJSON.non_field_errors[0]
                        }
                    }
                })
            },
            close() {
                this.$emit("hideLogin")
            }
        }
    }
</script>

<style scoped>
    #loginModal {
        position: fixed;
        z-index: 1000;
        top: -150px;
        left: 40%;
    }
</style>