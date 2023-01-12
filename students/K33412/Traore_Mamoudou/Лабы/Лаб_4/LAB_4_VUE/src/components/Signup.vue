<template>
    <div class="block-content">
      <v-card width="600" color="#fff8f2">
        <h1>Регистрация</h1>
        <validation-observer ref="observer" v-slot="{ invalid }">
          <validation-provider v-slot="{ errors }" name="Никнейм" rules="required">
            <v-text-field v-model="username" class="input" :counter="10" :error-messages="errors" label="Никнейм" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Поле" rules="required">
            <v-text-field v-model="password" class="input" type="password" :error-messages="errors" label="Пароль" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Поле" rules="required">
            <v-text-field v-model="password2" class="input" type="password" :error-messages="errors" label="Повторите пароль" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Имя" rules="required">
            <v-text-field v-model="first_name" class="input" :error-messages="errors" label="Имя" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Фамилия" rules="required">
            <v-text-field v-model="last_name" class="input" :error-messages="errors" label="Фамилия" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Отчество" rules="required">
            <v-text-field v-model="middle_name" class="input" :error-messages="errors" label="Отчество" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Пол" rules="required">
            <v-select-field class="select-line" v-model="sex" :error-messages="errors" :items="SEXES" label="Пол" required></v-select-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Дата рождения" rules="required">
            <v-text-field v-model="date_of_birth" class="input" :error-messages="errors" label="Дата рождения" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Номер трудового договора" rules="required|digits">
            <v-text-field v-model="contract_number" class="input" :error-messages="errors" label="Номер трудового договора" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Специализация" rules="required">
            <v-text-field v-model="specialty" class="input" :error-messages="errors" label="Специализация" required></v-text-field>
          </validation-provider>
          <validation-provider v-slot="{ errors }" name="Образование" rules="required">
            <v-text-field v-model="education" class="input" :error-messages="errors" label="Образование" required></v-text-field>
          </validation-provider>
          <v-btn class="button" type="submit" :disabled="invalid" @click="passwordCheck">Регистрация</v-btn>
      </validation-observer>
      </v-card>
    </div>
</template>
  
<script>
  import { digits, required } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  import $ from 'jquery'
  setInteractionMode('eager')
  extend('digits', {
    ...digits,
    message: '{_field_} needs to be digits.'
  })
  extend('required', {
    ...required,
    message: '{_field_} must not be empty'
  })
  export default {
    components: {
      ValidationProvider,
      ValidationObserver
    },
    name: 'Signup',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        username: '',
        password: '',
        password2: '',
        first_name: '',
        last_name: '',
        middle_name: '',
        sex: '',
        date_of_birth: '',
        contract_number: '',
        specialty: '',
        education: '',
        errors: '',
        SEXES: ['Мужчина', 'Женщина']
      }
    },
    methods: {
      passwordCheck () {
        if (this.password === this.password2) {
          this.signUp()
        } else {
          alert('Пароли не совпадают')
        }
      },
      signUp () {
        $.ajax({
          url: 'http://127.0.0.1:8000/auth/users/',
          type: 'POST',
          data: {
            username: this.username,
            password: this.password,
            password2: this.password2,
            first_name: this.first_name,
            last_name: this.last_name,
            middle_name: this.middle_name,
            sex: this.sex,
            date_of_birth: this.date_of_birth,
            contract_number: this.contract_number,
            specialty: this.specialty,
            education: this.education
          },
          success: (response) => {
            alert('Регистрация прошла успешно')
            sessionStorage.setItem('auth_token', response.auth_token)
            this.$router.push({ name: 'Login' })
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Некорректное имя пользователя и/или пароль')
            }
          }
        })
      }
   }
 }
</script>
  
<style scoped>
.block-content {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #FFFFFF; /* Цвет фона */
    padding: 10px; /* Поля вокруг текста */
}
.button{
    width:150px;
    margin: 10px;
}
.input{
    width:300px;
    margin: auto;
}
</style>