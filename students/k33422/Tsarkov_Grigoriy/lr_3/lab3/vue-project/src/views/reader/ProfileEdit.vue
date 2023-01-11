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
            label="ФИО"
            v-model="editForm.name"
            name="name"/>

          <v-text-field
            label="Номер билета"
            v-model="editForm.library_pass"
            name="library_pass"
            type="number"/>

          <v-text-field
            label="Дата рождения"
            v-model="editForm.birth_date"
            name="birth_date"
            type="date"/>

          <v-select
            v-model="editForm.education_level"
            :items="educationOptions"
            name="education_level"
            label="Образование"
          ></v-select>

          <v-checkbox
            v-model="editForm.degree"
            :label="'Учёная степень'"
          ></v-checkbox>

          <v-text-field
            label="Адрес"
            v-model="editForm.address"
            name="address"/>

          <v-text-field
            label="Телефон"
            v-model="editForm.phone_number"
            name="phone_number"/>

          <v-btn type="submit" color="primary" dark>Сохранить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15"><router-link to="/library/profile">Назад</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'ReaderProfileEdit',

  data: () => ({
    reader_old: Object,
    editForm: {
      // password: '',
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
      this.reader_old = response.data

      this.editForm.name = response.data.name
      this.editForm.library_pass = response.data.library_pass
      this.editForm.birth_date = response.data.birth_date
      this.editForm.education_level = response.data.education_level
      this.editForm.degree = response.data.degree
      this.editForm.address = response.data.address
      this.editForm.phone_number = response.data.phone_number
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
        await this.$router.push({ name: 'reader_profile' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
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
