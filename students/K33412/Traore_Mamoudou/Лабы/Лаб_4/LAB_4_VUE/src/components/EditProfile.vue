<template>
    <div>
      <div>
        <v-app-bar color="#653d19" dense dark>
          <v-btn icon @click="goHome">
            <v-icon>mdi-home</v-icon>
          </v-btn>
          <v-toolbar-title>Clinic</v-toolbar-title>
          <v-btn class="ma-2" outlined color="white" @click="goDoctorlist">Список врачей</v-btn>
          <v-spacer></v-spacer>
          <v-btn icon @click="logout">
            <v-icon>mdi-exit-to-app</v-icon>
          </v-btn>
        </v-app-bar>
      </div>
      <div class="block-content">
        <v-card width="600" color="#fff8f2">
          <h1>Изменение пароля</h1>
          <validation-observer ref="observer" v-slot="{ invalid }">
              <validation-provider v-slot="{ errors }" name="Поле" rules="required">
                <v-text-field v-model="current_password" class="input" type="password" :error-messages="errors"
                              label="Предыдущий пароль" required></v-text-field>
              </validation-provider>
              <validation-provider v-slot="{ errors }" name="Поле" rules="required">
                <v-text-field v-model="password" class="input" type="password" :error-messages="errors"
                              label="Новый пароль" required></v-text-field>
              </validation-provider>
              <validation-provider v-slot="{ errors }" name="Поле" rules="required">
                <v-text-field v-model="password2" class="input" type="password" :error-messages="errors"
                              label="Повторите пароль" required></v-text-field>
              </validation-provider>
              <v-btn class="button" type="submit" color="primary" :disabled="invalid" @click="passwordCheck">Сохранить
              </v-btn>
          </validation-observer>
        </v-card>
        <v-card width="600" color="#fff8f2">
          <h1>Редактирование</h1>
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
            <validation-provider v-slot="{ errors }" name="Дата увольнения" rules="required|date_format:yyyy-dd-mm">
              <v-text-field v-model="finish_work_date" class="input" :error-messages="errors" label="Дата увольнения" required></v-text-field>
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
              <v-btn class="button" type="submit" color="primary" :disabled="invalid" @click="correctInfo">Сохранить</v-btn>
        </validation-observer>
        </v-card>
      </div>
    </div>
</template>
  
<script>
  import $ from 'jquery'
  import { required, digits } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  setInteractionMode('eager')
  extend('digits', {
    ...digits,
    message: '{_field_} needs to be {length} digits. ({_value_})'
  })
  extend('required', {
    ...required,
    message: '{_field_} не должно быть пустым'
  })
  export default {
    components: {
      ValidationProvider,
      ValidationObserver
    },
    name: 'EditProfile',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        current_password: '',
        password: '',
        password2: '',
        first_name: '',
        last_name: '',
        middle_name: '',
        sex: '',
        finish_work_date: '',
        date_of_birth: '',
        contract_number: '',
        specialty: '',
        education: ''
      }
    },
    created () {
      $.ajaxSetup({
        headers: { authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.loadInfo()
    },
    methods: {
      passwordCheck () {
        if (this.password === this.password2) {
          this.correctPassword()
        } else {
          alert('Пароли не совпадают')
        }
      },
      correctPassword () {
        $.ajax({
          url: 'http://127.0.0.1:8000/auth/users/set_password/',
          type: 'POST',
          data: {
            new_password: this.password,
            current_password: this.current_password
          },
          success: (response) => {
            console.log(response)
            this.$router.push({ name: 'Profile' })
          }
        })
      },
      correctInfo () {
        $.ajax({
          url: 'http://127.0.0.1:8000/auth/users/me/',
          type: 'PATCH',
          data: {
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
            console.log(response)
            this.$router.push({ name: 'Profile' })
          },
          error: (response) => {
            alert(response)
          }
        })
      },
      loadInfo () {
        $.ajax({
          url: 'http://127.0.0.1:8000/auth/users/me/',
          type: 'GET',
          success: (response) => {
            this.first_name = response.first_name
            this.last_name = response.last_name
            this.middle_name = response.middle_name
            this.sex = response.sex
            this.date_of_birth = response.date_of_birth
            this.contract_number = response.contract_number
            this.specialty = response.specialty
            this.education = response.education
          },
          error: (response) => {
            alert(response)
          }
        })
      },
      goDoctorlist () {
        this.$router.push({ name: 'Doctorlist' })
      },
      goHome () {
        this.$router.push({ name: 'Home' })
      },
      goProfile () {
        this.$router.push({ name: 'Profile' })
      },
      logout () {
        sessionStorage.removeItem('auth_token')
        window.location = '/'
      }
    }
  }
</script>
  
<style scoped>
  .block-content {
    margin: auto;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #FFFFFF; /* Цвет фона */
    padding: 10px; /* Поля вокруг текста */
  }
</style>