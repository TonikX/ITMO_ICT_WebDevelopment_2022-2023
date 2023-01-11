<template>
    <nav class="navbar navbar-expand-md navbar-light sidebarNavigation color-me "
         data-sidebarClass="navbar-dark bg-dark" style="background-color: #145ee7;">
        <div class="container-fluid">
            <a class="navbar-brand" href="/" style="color: #ffffff;">IK</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="nav navbar-nav nav-flex-icons ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/" style="color: #ffffff;"> Главаня страница
                        </a>
                    </li>
                    <li v-if="!chechkAuth" class="nav-item">
                        <a class="nav-link" href="/all_workers" style="color: #ffffff;">Сотрудники</a>
                    </li>
                    <li class="nav-item">
                        <a v-if="!chechkAuth" class="nav-link" href="/rooms" style="color: #ffffff;">Номера</a>
                    </li>
                    <li v-if="!chechkAuth" class="nav-item">
                        <a class="nav-link" href="" style="color: #ffffff;">Бронирование</a>
                    </li>
                    <li v-if="!chechkAuth" class="nav-item">
                        <a class="nav-link" href="/client" style="color: #ffffff;">Постояльцы</a>
                    </li>
                    <li v-if="chechkAuth" class="nav-item">
                        <a class="nav-link" href="/login" style="color: #ffffff;">Войти</a>
                    </li>
                    <li v-if="chechkAuth" class="nav-item">
                        <a class="nav-link" href="/singup" style="color: #ffffff;">Регистрация</a>
                    </li>
                    <li v-if="!chechkAuth">
                        <button type="button" class="btn btn-danger" @click="logout">
                            Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <slot/>

</template>


<script>
import {checkTokenApi} from "@/api";

export default {
    data() {
        return {
            answerStatus: null
        };
    },

    computed: {
        chechkAuth() {
            // eslint-disable-next-line vue/no-async-in-computed-properties
            checkTokenApi.checkToken().catch( function(error) { localStorage.setItem("status_answer", error.response.status) });

            if ( localStorage.status_answer === '401'){
                localStorage.removeItem("status_answer")
                return true
            }

            else{
                localStorage.removeItem("status_answer")
                return false
            }

        }
    },

    methods: {
        async logout() {
            localStorage.clear()
            window.location.href = "/"
        },
    },
}
</script>
