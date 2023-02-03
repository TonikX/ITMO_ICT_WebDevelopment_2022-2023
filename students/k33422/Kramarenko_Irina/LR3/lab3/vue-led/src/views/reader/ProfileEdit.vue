<template>
  <div class="edit">
    <h2>Редактирование профиля</h2>
    <v-form
      @submit.prevent="saveChanges"
      ref="editForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

<!--          <v-text-field-->
<!--            label="Пароль"-->
<!--            v-model="editForm.password"-->
<!--            type="password"/>-->

          <v-text-field
            label="Имя"
            v-model="editForm.first_name"
            name="first_name"/>

          <v-text-field
            label="Фамилия"
            v-model="editForm.last_name"
            name="last_name"/>


          <v-text-field
            label="Адрес электронной почты"
            v-model="editForm.email"
            name="email"/>

          <v-btn type="submit" color="primary" dark>Сохранить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15"><router-link to="/show/profile">Назад</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'ProfileEdit',

  data: () => ({
    manager: Object,
    editForm: {
      first_name: '',
      last_name: '',
      email: ''
    }
  }),

  created () {
    this.loadReaderData()
  },

  methods: {
    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.manager = response.data
      this.editForm.first_name = response.data.first_name
      this.editForm.last_name = response.data.last_name
      this.editForm.email = response.data.email
    },

    async saveChanges () {
      for (const [key, value] of Object.entries(this.editForm)) {
        if (value === '') {
          delete this.editForm[key]
        }
      }

      try {
        const response = await this.axios
          .patch('http://127.0.0.1:8000/auth/users/me/',
            this.editForm, {
              headers: {
                Authorization: `Token ${localStorage.getItem('auth_token')}`
              }
            })
        console.log(response)

        this.$refs.editForm.reset()
        await this.$router.push({ name: 'profile' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.first_name) {
          alert('Имя: ' + e.response.data.first_name)
        } else if (e.response.data.last_name) {
          alert('Фамилия: ' + e.response.data.last_name)
        } else if (e.response.data.email) {
          alert('Адрес электронной почты: ' + e.response.data.email)
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
