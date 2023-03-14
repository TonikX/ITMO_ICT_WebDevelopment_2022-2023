<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <RegistrationNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Информация о читателе </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Номер читательского билета"
                v-model="form.ticket"
                name="ticket"
                placeholder="12345"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Серия и номер паспорта"
                v-model="form.passport_number"
                name="passport_number"
                placeholder="12345678910"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Дата рождения"
                v-model="form.birth_date"
                name="birth_date"
                placeholder="2002-07-31"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Номер телефона"
                v-model="form.phone_number"
                name="phone_number"
                placeholder="+79516571701"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Адрес"
                v-model="form.address"
                name="address"
                placeholder="Russia, Saint-Petersburg, Bolshaya Moskovskaya 1-3"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-select
                v-model="form.education"
                :items="educationOptions"
                label="Образование"
                name="education"
              ></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="4" class="mx-auto"></v-col>
            <v-checkbox
              v-model="form.is_has_academic_degree"
              name="is_has_academic_degree"
              :label="'Наличие учёной степени'"
            ></v-checkbox>
          </v-row>

          <v-col cols="5" class="mx-auto">
            <v-btn block color="blue" @click.prevent="finish()"> Завершить</v-btn>
          </v-col>
          <br>
        </v-card>
      </v-col>
      <br><br>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import RegistrationNavigationBar from '@/components/RegistrationNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'FinishCompleteInfoView',
  components: {BarLayout, RegistrationNavigationBar},
  data: () => ({
    form: {
      ticket: '',
      name: '',
      passport_number: '',
      birth_date: '',
      phone_number: '',
      address: '',
      education: '',
      is_has_academic_degree: ''
    },
    educationOptions: ['primary', 'secondary', 'higher']
  }),
  methods: {
    async finish() {
      try {
        const user_response = await axios.get(
          'http://127.0.0.1:8000/auth/users/me/',
          {
            headers: {Authorization: `Token ${localStorage.auth_token}`}
          }
        )
        const user = user_response.data

        this.form.name = user.first_name + user.last_name
        this.form.education = this.form.education[0]

        const reader_create_response = await axios.post('http://127.0.0.1:8000/library/readers/create', this.form)
        const reader = reader_create_response.data

        await axios.post(
          'http://127.0.0.1:8000/library/userreaders/create',
          {user: user.id, reader: reader.ticket}
        )

        window.location = '/home'

        this.$router.push({name: 'Home'})
      } catch (e) {
        console.log(e)
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.ticket) {
          alert('Номер билета: ' + e.response.data.ticket)
        } else if (e.response.data.birth_date) {
          alert('Дата рождения: ' + e.response.data.birth_date)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.is_has_academic_degree) {
          alert('Учёная степень: ' + e.response.data.is_has_academic_degree)
        } else if (e.response.data.passport_number) {
          alert('Паспортные данные: ' + e.response.data.passport_number)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone_number) {
          alert('Телефон: ' + e.response.data.phone_number)
        } else {
          alert(e.error.message)
        }
      }
    }
  }
}
</script>
