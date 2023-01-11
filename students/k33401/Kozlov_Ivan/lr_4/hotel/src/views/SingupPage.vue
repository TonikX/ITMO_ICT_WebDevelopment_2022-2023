<template>
    <base-layout>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card">
                        <header class="card-header">
                            <h4 class="card-title mt-2">Регистрация</h4>
                        </header>
                        <article class="card-body">
                            <form @submit.prevent="singupPage">

                                <label>Username </label>
                                <input v-model="form.username" type="text" class="form-control" placeholder="Ник" name="Username" id="last_name" required>

                                <label>Email </label>
                                <input v-model="form.email" type="email" class="form-control" placeholder="example@ex.com" name="email" id="email">

                                <label>Создать пароль</label>
                                <input v-model="form.password" class="form-control" type="password" name="password" id="password">

                                <div class="form-group d-flex flex-column justify-content-start my-1">
                                    <br>
                                    <button class="btn btn-primary">
                                        Регистрация
                                    </button>

                                </div> <!-- form-group// -->

                            </form>
                        </article> <!-- card-body end .// -->
                        <div class=" border-top card-body text-center">Уже есть аккаунт? <a href="/login">Войти</a>
                        </div>
                    </div> <!-- card.// -->
                </div> <!-- col.//-->

            </div> <!-- row.//-->

        </div>
    </base-layout>

</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import useSingUpStore from "@/stores/singup";
import {mapActions} from "pinia";

export default {
    name: "SingupPage.vue",

    components: { BaseLayout },

    methods: {
        ...mapActions(useSingUpStore, ['singup']),

        async singupPage() {
            await this.singup(this.form)
            // this.$refs.loginForm.reset()
            if (localStorage.token) {
                window.location.assign("/login")
            }
        }
    },


    data() {
        return {
            form: {
                username: "",
                email: "",
                password: ""
            }

        }
    }
}
</script>

