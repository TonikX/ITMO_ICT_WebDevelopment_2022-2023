<template>
  <div class="signup">
    <v-form
      @submit.prevent="signUp"
      ref="signUpForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Введите имя"
            v-model="signUpForm.first_name"
            :rules="rules.required"
          />
          <v-text-field
            label="Введите фамилию"
            v-model="signUpForm.last_name"
            :rules="rules.required"
          />
          <v-text-field
            label="Введите номер телефона"
            v-model="signUpForm.tel"
            :rules="rules.required"
          />
          <v-text-field
            label="Введите email"
            v-model="signUpForm.email"
            :rules="rules.required"
          />
          <v-text-field
            label="Введите имя пользователя"
            v-model="signUpForm.username"
            :rules="rules.required"
          />
          <v-text-field
            label="Введите пароль"
            v-model="signUpForm.password"
            type="password"
            :rules="rules.required"
          />
          <v-layout justify-center>
                <v-card-actions>
                        <v-btn primary>
                        <v-btn type="submit" color="primary" dark>Зарегистрироваться</v-btn>
                              </v-btn>
                </v-card-actions>
          </v-layout>
          <p class="mt-lg-5">Уже зарегистрированы? <router-link to="/signin">Войти</router-link></p>
          <p class="mt-lg-5"><router-link to="/">На главную</router-link></p>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',

  data: () => ({
    signUpForm: {
      first_name: '',
      last_name: '',
      role: '',
      tel: '',
      email: '',
      username: '',
      password: ''
    },

    rules: {
      required: value => !!value || 'Required.',
    }

  }),

  methods: {
    async signUp () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)

        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.signUpForm.reset()
        await this.$router.push({ name: 'signin' })
      } catch (e) {
        console.error('ERROR', e)
      }
    }
  }
}
</script>
