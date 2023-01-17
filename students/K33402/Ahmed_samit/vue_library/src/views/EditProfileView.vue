<template>
    <v-app>
        <bar-layout> 
            <EditProfile />
      </bar-layout>
<v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
    <v-row class="mx-3.5">
     <v-col cols="4" class="mx-auto">
<br><br>

<div class="edit">
    <h2 style = "text-align: center">Редактирование профиля</h2>
    <v-form
      @submit.prevent="saveChanges"
      ref="editForm"
      class="my-2">
      <v-card max-width = 800 color = "#f7f4ef">
      <v-row>
        <v-col cols="5" class="mx-auto">
          <v-text-field
            label="Имя"
            v-model="editForm.first_name"
            name="first_name"/>

          <v-text-field
            label="Фамилия"
            v-model="editForm.last_name"
            name="last_name"/>

          <v-text-field
            label="Номер билета"
            v-model="editForm.card_number"
            name="card_number"
            type="number"/>

          <v-text-field
            label="Дата рождения"
            v-model="editForm.date_of_birth"
            name="date_of_birth"
            type="date"/>

          <v-select
            v-model="editForm.education"
            :items="educationOptions"
            label="Образование"
          ></v-select>

          <v-checkbox
            v-model="editForm.degree"
            :label="'Учёная степень'"
          ></v-checkbox>

          <v-text-field
            label="Паспортные данные"
            v-model="editForm.passport"
            name="passport"/>

          <v-text-field
            label="Адрес"
            v-model="editForm.address"
            name="address"/>

          <v-text-field
            label="Телефон"
            v-model="editForm.phone"
            name="phone"/>       
        </v-col>
      </v-row>
    </v-card>
    <v-btn block type="submit" color="primary" dark>Сохранить</v-btn>
    </v-form>

  </div>
     </v-col>
     </v-row>
</v-main>
    </v-app>
</template>
<script>
import BarLayout from '@/layouts/BarLayout.vue'
import EditProfile from '@/components/EditProfile.vue'
import axios from 'axios'
export default {
name: 'EditReader',
components:{ BarLayout, EditProfile},  
data: () => ({
    reader_old: Object,
    editForm: {
      first_name: '',
      last_name: '',
      card_number: '',
      date_of_birth: '',
      education: '',
      degree: '',
      passport: '',
      address: '',
      phone: ''
    },
    educationOptions: ['Среднее общее', 'Среднее специальное',
      'Высшее', 'Неоконченное высшее', 'Неоконченное среднее']
  }),
  created () {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData () {
      const response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.auth_token}`
          }
        })
      this.reader_old = response.data
      this.editForm.first_name = response.data.first_name
      this.editForm.last_name = response.data.last_name
      this.editForm.card_number = response.data.card_number
      this.editForm.date_of_birth = response.data.date_of_birth
      this.editForm.education = response.data.education
      this.editForm.degree = response.data.degree
      this.editForm.passport = response.data.passport
      this.editForm.address = response.data.address
      this.editForm.phone = response.data.phone
    },
    async saveChanges () {
      for (const [key, value] of Object.entries(this.editForm)) {
        if (value === '') {
          delete this.editForm[key]
        }
      }
      try {
        await axios
          .patch('http://127.0.0.1:8000/auth/users/me/',
            this.editForm, {
              headers: {
                Authorization: `Token ${localStorage.auth_token}`
              }
            })
        await this.$router.push({ name: 'Reader' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.username) {
          alert('Логин: ' + e.response.data.username)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.first_name) {
          alert('Имя: ' + e.response.data.first_name)
        } else if (e.response.data.last_name) {
          alert('Фамилия: ' + e.response.data.last_name)
        } else if (e.response.data.card_number) {
          alert('Номер билета: ' + e.response.data.card_number)
        } else if (e.response.data.date_of_birth) {
          alert('Дата рождения: ' + e.response.data.date_of_birth)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.degree) {
          alert('Учёная степень: ' + e.response.data.degree)
        } else if (e.response.data.passport) {
          alert('Паспортные данные: ' + e.response.data.passport)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone) {
          alert('Телефон: ' + e.response.data.phone)
        } else {
          console.error(e.message)
        }
      }
    }
  }
}
</script>