<template>
    <base-layout>
        <main class="login-form my-2">
            <div class="cotainer">
                <div class="row justify-content-center">
                    <div class="col-md-5">
                        <div class="card">
                            <div class="card-header">Вход</div>
                            <div class="card-body">
                                <form ref="loginForm" @submit.prevent="loginPage">
                                    <div class="form-group row">
                                        <label for="email_address" class="col-md-3 col-form-label text-md-right">Username
                                        </label>
                                        <div class="col-md-6">
                                            <input v-model="form.username" type="text" id="username" class="form-control" name="username" required
                                                   autofocus placeholder="Ник">
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="password" class="col-md-3 col-form-label text-md-right">Пароль</label>
                                        <div class="col-md-6">
                                            <input v-model="form.password" type="password" id="password" class="form-control" name="password"
                                                   required placeholder="Пароль">
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <div class="col-md-6 offset-md-4">
                                            <div class="checkbox">
                                                <label>
                                                    <input  type="checkbox" name="remember" > Запомнить меня
                                                </label>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="col-md-6 offset-md-4">
                                        <button type="submit" class="btn btn-primary">
                                            Войти
                                        </button>
                                        <a href="#" class="btn btn-link">
                                            Забыли пароль?
                                        </a>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </base-layout>
</template>

<script>
import BaseLayout from '@/layouts/BaseLayout.vue'

import useUserStore from "@/stores/user";
import { mapActions } from 'pinia'

export default {
    name: "LoginPage",
    components: {BaseLayout},

    methods: {
        ...mapActions(useUserStore, ['login']),

        async loginPage() {
            await this.login(this.form)
            // this.$refs.loginForm.reset()
            window.location.assign("/")
        }
    },

    data(){
        return {
            form: {
                username : "",
                password : ""
            }

        }
    }
}
</script>

<style scoped>

</style>
