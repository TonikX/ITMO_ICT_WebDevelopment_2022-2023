# Мухина_Lr4





# Реализованы три основные страницы:
`Login.vue` - Вход в аккаунт
`Personal.vue` - Страница с погодой выьранных городов
`Registration.vue` - Страница регистрации


# Personal.vue
```
<template>
    <main>
        <div class="justify-content-center row">
            <div class="col-sm-5 my-3 mx-5 justify-content-center row">
                <RegistrationForm />
            </div>
        </div>
        <div class="justify-content-center row">
        <div class="col-sm-5 my-3 mx-5 justify-content-center row">
            <img src="../assets/regist.jpg" class="card-img-top" alt="...">
        </div>
    </div>
    </main>
</template>

<script>
    import RegistrationForm from "@/components/RegistrationForm";
    export default {
        name: "Registration",
        components: {RegistrationForm}
    }
</script>

<style scoped>

</style>
```
В скрипт мы передаём компонент RegistrationForm, в котором и написана вся форма регистрации


# Login.vue
```
<template>
    <main>
       <div class="justify-content-center row">
        <div class="justify-content-center row">
            <div class="justify-content-center col-sm-5 my-3 mx-5 ">
                <LoginForm />
            </div>
        </div>
        <div class="col-sm-5 my-3 mx-5 justify-content-center row">
            <img src="../assets/img21.jpg" class="card-img-top" alt="...">
        </div>
    
     </div>
    </main>
</template>

<script>
    import LoginForm from "@/components/LoginForm";
    export default {
        name: "Login",
        components: {LoginForm}
    }
</script>

<style scoped>

</style>
```
В скрипт мы передаём компонент LoginForm, в котором и написана вся форма входа


# Registration.vue

```
<template>
    <form @submit.prevent="registration">
        <div class="form-group my-3 mx-5">
            <label for="username">Ваш ник</label>
            <input required v-model="form.username" type="text" class="form-control" id="username" placeholder="Введите ваш ник">
        </div>
        <div class="form-group my-3 mx-5">
            <label for="Name">Ваше имя</label>
            <input v-model="form.first_name" type="text" class="form-control" id="Name" placeholder="Введите имя">
        </div>
        <div class="form-group my-3 mx-5">
            <label for="lastName">Ваша фамилия</label>
            <input v-model="form.last_name" type="text" class="form-control" id="lastName" placeholder="Введите фамилию">
        </div>
        <div class="form-group my-3 mx-5">
            <label for="city">Ваш город</label>
            <v-select
                    id="city"
                    @input="setSelected"
                    :options="cities"
                    :value="selectedCity"
                    label="name"
                    placeholder="Город"></v-select>
        </div>
        <div class="form-group my-3 mx-5">
            <label for="Password">Пароль</label>
            <input required v-model="form.password" type="password" class="form-control" id="Password" placeholder="Введите пароль">
        </div>
        <button type="submit" class="btn btn-primary my-3 mx-5 buttom-my">Зарегистрироваться</button>
        <router-link class="btn btn-outline-primary my-3 buttom-my" to="/login">Войти</router-link>
    </form>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "RegistrationForm",
        data() {
            return {
                form: {
                    username: "",
                    first_name: "",
                    last_name: "",
                    password: "",
                    city: ""
                },
                selectedCity: ''
            };
        },
        computed: {
            ...mapGetters({
                cities: 'cities',
            })
        },
        mounted() {
            this.$store.dispatch('getCities')
        },
        methods: {
            registration() {
                this.$store.dispatch('Registration', this.form);
            },
            setSelected(val) {
                this.selectedCity = val.name
                this.form.city = val.id
            }
        }
    }
</script>

<style scoped>
    .buttom-my {
        background-color: #DC143C !important;
        color: #000 !important;
        border:#DC143C !important;
    }
</style>
```
В скрипт мы передаём компонент RegistrationForm, в котором форма регистрации
Записываем всё в базу
Функции для отображения городов: списка и названия
Функция регистрации объявлена в methods
Там же функция для города


## Videos

[Videos](https://drive.google.com/drive/folders/1jAS5c_T15Ac0HnWsUDuKHo8e8bArSbRT?usp=sharing)