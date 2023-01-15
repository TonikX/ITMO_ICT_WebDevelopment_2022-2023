<template>
  <div class="signup">
    <h2>Регистрация</h2>
    <v-form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">
          <v-text-field
            label="Логин"
            v-model="signUpForm.username"/>

          <v-text-field
            label="Пароль"
            v-model="signUpForm.password"
            type="password"/>

          <v-text-field
            label="ФИО"
            v-model="signUpForm.name"
            name="name"/>

          <v-text-field
            label="Номер билета"
            v-model="signUpForm.library_pass"
            name="library_pass"
            type="number"/>

          <v-text-field
            label="Дата рождения"
            v-model="signUpForm.birth_date"
            name="birth_date"
            type="date"/>

          <v-select
            v-model="signUpForm.education_level"
            :items="educationOptions"
            label="Образование"
          ></v-select>

          <v-checkbox
            v-model="signUpForm.degree"
            :label="'Учёная степень'"
          ></v-checkbox>

          <v-text-field
            label="Адрес"
            v-model="signUpForm.address"
            name="address"/>

          <v-text-field
            label="Телефон"
            v-model="signUpForm.phone_number"
            name="phone"/>

          <v-btn type="submit" color="primary" dark>Зарегистрироваться</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15">Уже зарегистрированы? <router-link to="/library/signin">Войти</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'SignUp',

  data: () => ({
    signUpForm: {
      username: '',
      name: '',
      library_pass: '',
      birth_date: '',
      education_level: '',
      degree: '',
      address: '',
      phone_number: ''
    },
    educationOptions: ['e', 's', 'c']
  }),

  methods: {
    async signUp () {
      try {
        await this.axios.post('http://127.0.0.1:8000/auth/users/', this.signUpForm)
        this.$refs.signUpForm.reset()
        await this.$router.push({ name: 'signin' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.username) {
          alert('Логин: ' + e.response.data.username)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.name) {
          alert('Имя: ' + e.response.data.name)
        } else if (e.response.data.library_pass) {
          alert('Номер билета: ' + e.response.data.library_pass)
        } else if (e.response.data.birth_date) {
          alert('Дата рождения: ' + e.response.data.birth_date)
        } else if (e.response.data.education_level) {
          alert('Образование: ' + e.response.data.education_level)
        } else if (e.response.data.degree) {
          alert('Учёная степень: ' + e.response.data.degree)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone_number) {
          alert('Телефон: ' + e.response.data.phone_number)
        } else {
          console.error(e.message)
        }
      }
    }
  }
}
</script>

<style>
</style>
