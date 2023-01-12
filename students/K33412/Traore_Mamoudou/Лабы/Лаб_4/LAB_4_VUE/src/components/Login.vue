<template>
    <div class="block-content">
      <v-card width="600" height="250" color="#fff8f2">
        <h1>Авторизация</h1>
        <validation-observer ref="observer" v-slot="{ invalid }">
            <validation-provider name="Никнейм">
              <v-text-field class="input" v-model="login" label="Никнейм"></v-text-field>
            </validation-provider>
            <validation-provider name="Поле">
              <v-text-field class="input" v-model="password" type="password" label="Пароль"></v-text-field>
            </validation-provider>
            <v-btn class="button" type="submit" :disabled="invalid" color="primary" @click="setLogin">Вход</v-btn>
        </validation-observer>
      </v-card>
    </div>
</template>
  
<script>
  import { ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  import $ from 'jquery'
  setInteractionMode('eager')
  export default {
    components: {
      ValidationProvider,
      ValidationObserver
    },
    name: 'Login',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        login: '',
        password: ''
      }
    },
    methods: {
      setLogin () {
        $.ajax({
          url: 'http://127.0.0.1:8000/auth/token/login/',
          type: 'POST',
          data: {
            username: this.login,
            password: this.password
          },
          success: (response) => {
            sessionStorage.setItem('auth_token', response.auth_token)
            this.$router.push({ name: 'Profile' })
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Логин или пароль не верен')
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
  .label{
    margin-top: 10px;
  }
</style>