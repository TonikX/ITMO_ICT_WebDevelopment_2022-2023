<template>
  <div class="app">
    <h1>Авторизация</h1>
<!--    <v-form @submit.prevent="Login" ref="LoginForm" class="my-2">-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Логин: </strong>-->
<!--          <input-->
<!--              v-model="LoginForm.username"-->
<!--              class="input"-->
<!--              type="text"-->
<!--              placeholder="Логин"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div style="font-size: 20px; color: royalblue">-->
<!--        <div class="t"><strong>Пароль: </strong>-->
<!--          <input-->
<!--              v-model="LoginForm.password"-->

<!--              class="input"-->
<!--              type="password"-->
<!--              placeholder="Пароль"/>-->
<!--        </div>-->
<!--      </div>-->
<!--      <v-btn variant="outlined" class="mr-4" color="success" rounded="lg" @click="setLogin">Войти</v-btn>-->
<!--    </v-form>-->
    <v-form @submit.prevent="Login" ref="LoginForm" class="my-2">
      <v-row>
        <v-col class="mx-auto">
          <v-text-field
              v-model="LoginForm.username"
              label="Логин"
              class="input"
              type="text"
              placeholder="Логин"/>
          <v-text-field
            v-model="LoginForm.password"
            class="input"
            label="Пароль"
            type="password"
            placeholder="Пароль"/>
          <v-btn variant="outlined" color="success" rounded="lg" @click="setLogin">Войти</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <br>
    <p class="mt-0">Ещё нет аккаунта?<br>
      <router-link to="/registration/">Зарегистрироваться</router-link></p>
  </div>
</template>

<script>
  import $ from "jquery"
  export default {
    name: 'Login',
    data: () => ({
      LoginForm: {
        username: '',
        password: ''
      }
    }),
    methods: {
      setLogin() {
          $.ajax({
            url: "http://127.0.0.1:8000/auth/token/login/",
            type: "POST",
            data: {
              username: this.LoginForm.username,
              password: this.LoginForm.password,
            },
            success: (response) => {
              console.log(response.auth_token)
              sessionStorage.setItem("auth_token", response.auth_token)
              this.$router.push({name: 'home'})
              alert("Вы вошли в аккаунт")
            },
            error: (response) => {
              if (response.status === 400) {
                alert("Невозможно произвести авторизацию с такими данными, попробуйте ещё раз")
              }
            }
          })
        }
    // async Login () {
    //   try {
    //     const response = await this.axios.post('http://127.0.0.1:8000/auth/token/login', {
    //       username: this.LoginForm.username,
    //       password: this.LoginForm.password
    //     })
    //     console.log(response.data)
    //     this.$refs.LoginForm.reset()
    //     localStorage.setItem('auth_token', response.data.auth_token)
    //     await this.$router.push({ name: 'home' })
    //   } catch (e) {
    //     alert('Error')
    //   }
    // }
  }
}
</script>

<style>
</style>
