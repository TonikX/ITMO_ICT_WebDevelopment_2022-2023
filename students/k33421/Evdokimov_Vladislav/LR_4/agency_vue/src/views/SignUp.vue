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
          <v-select
            :items="roles"
            label="Выберите роль"
            v-model="signUpForm.role"
            :rules="rules.required"
          ></v-select>
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
            :rules="[rules.required, rules.counter9]"
          />
          <v-btn type="submit" color="primary" dark>Зарегистрироваться</v-btn>
          <p class="mt-5">Уже зарегистрированы? <router-link to="/signin">Войти</router-link></p>
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

    roles: ['Администратор', 'Менеджер', 'Бухгалтер'],
    rules: {
      required: value => !!value || 'Required.',
      counter9: value => value.length <= 9 || 'Min 9 characters'
    }

  }),

  methods: {
    async signUp () {
      if (this.signUpForm.role === 'Администратор') {
        this.signUpForm.role = 'Администратор'
      } else if (this.signUpForm.role === 'Менеджер') {
        this.signUpForm.role = 'Менеджер'
      } else if (this.signUpForm.role === 'Бухгалтер') {
        this.signUpForm.role = 'Бухгалтер'
      }
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/auth/users/', this.signUpForm)

        if (response.status !== 201) {
          throw new Error(response.status)
        }
        this.$refs.signUpForm.reset()
        await this.$router.push({ name: 'signin' })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
